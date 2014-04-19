## This reads a directory full of files and reports 
## the number of completely observed cases in each data file

## Author: Kevin Beland (belandbioinfo@gmail.com)

complete <- function(directory, id = 1:332) {
    ## 'directory' is a character vector of length 1 indicating
    ## the location of the CSV files

    ## 'id' is an integer vector indicating the monitor ID numbers
    ## to be used
    
    ## Return a data frame of the form:
    ## id nobs
    ## 1  117
    ## 2  1041
    ## ...
    ## where 'id' is the monitor ID number and 'nobs' is the
    ## number of complete cases


    # This function returns the number of complete cases in 
    # a specified file id
    getComplete <- function(fileID) {
        fileName <- paste(fileID,".csv",sep="")
        data <- read.csv(fileName)
        complData <- complete.cases(data)
        numOK <- sum(complData)
    }
    
    # This function takes the ID numeric vector supplied in argument
    # list and converts it to a character vector used for opening 
    # specified filed
    convIDToChar <- function(fileID) {

        #initialize new vector to contain character ID for opening files
        newIDVector <- vector()

        for (i in fileID) {
            tmpName <- as.character(i)
            if (nchar(tmpName) == 1) {
                newID <- paste("00",tmpName,sep="")
            }
            else if (nchar(tmpName) == 2) {
                newID <- paste("0",tmpName,sep="")
            }
            else {
                newID <- tmpName
            }
            
            newIDVector = c(newIDVector, newID)

        }
        
        #return new character id vector
        newIDVector
    }

    # Save old working directory, Set working directory 
    oldwd <- getwd()
    setwd(directory)

    # Determine the valid CSV file names in specified directory, and truncate
    # argument ID list to only contain those that will open a file
    inDir <- list.files()
    goodID <- unlist(strsplit(inDir, "\\.csv"))

    # Convert argument ID list to characters as seen in data directory
    argID <- convIDToChar(id)

    # Initialize vector for holding correct values
    numCorrect <- vector()
 
    # For each specified id determine the number of correct cases
    for (idNum in argID) {
        numCorrect <- c(numCorrect,getComplete(idNum))
    }  

    # Create data frame 
    corrDF = data.frame(id=id, nobs=numCorrect)

    # Set working directory back to old
    setwd(oldwd)

    # Return data frame
    print(corrDF)

}
