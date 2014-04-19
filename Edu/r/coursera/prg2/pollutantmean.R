## function named 'pollutantmean' that calculates the mean of a pollutant 
## (sulfate or nitrate) across a specified list of monitors.
## 
## Author: Kevin Beland (belandbioinfo@gmail.com)
## Assignment 2 Part 1
## 
## 

pollutantmean <- function(directory, pollutant, id = 1:332) {
    ## 'directory' is a character vector of length 1 indicating
    ## the location of the CSV files

    ## 'pollutant' is a character vector of length 1 indicating
    ## the name of the pollutant for which we will calculate the
    ## mean; either "sulfate" or "nitrate".

    ## 'id' is an integer vector indicating the monitor ID numbers
    ## to be used

    ## Return the mean of the pollutant across all monitors list
    ## in the 'id' vector (ignoring NA values)
    
    # This function returns the no null values from a specified file id
    getValues <- function(fileID) {
        fileName <- paste(fileID,".csv",sep="")
        data <- read.table(fileName)
        naValues <- is.na(data$pollutant)
        goodValues <- data$pollutant[!naValues]
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
    
    # Initialize empty vector destined to hold pollutant data
    fullVector <- vector()

    # For each specified id, open the corresponding monitor data file
    # and append the specified pollutant data to a single vector
    for (idNum in argID) {
        fullVector <- c(fullVector,getValues(idNum))
    }  

    # Set working directory back to old
    setwd(oldwd)

    # Return the mean of all specified pollutant data
    fullMean <- mean(fullVector)
}
