corr <- function(directory, threshold = 0) {
    ## 'directory' is a character vector of length 1 indicating
    ## the location of the CSV files

    ## 'threshold' is a numeric vector of length 1 indicating the
    ## number of completely observed observations (on all
    ## variables) required to compute the correlation between
    ## nitrate and sulfate; the default is 0

    ## Return a numeric vector of correlations

    # This function returns TRUE if the monitor contains enough complete
    # cases determined by the threshold value
    getComplete <- function(fileName) {
        data <- read.csv(fileName)
        complData <- complete.cases(data)
        numOK <- sum(complData)
        dataOK <- data[complData,]
        if (numOK > threshold) {
            retCor <- cor(dataOK$nitrate, dataOK$sulfate)
            retVal <- retCor
        }
        else {
            retVal <- NULL
        }
            
        retVal
    }

    # Save old working directory, Set working directory 
    oldwd <- getwd()
    setwd(directory)

    # Determine the valid CSV file names in specified directory
    inDir <- list.files()

    # Initialize vector for holding correct vector ID 
    corrVector <- vector()
 
    # For each specified id determine the number of correct cases
    for (fileN in inDir) {

        # getComplete returns FALSE if there are not enough complete
        # cases specified by threshold, else it returns a dataframe 
        # containing two columns, sulfate and nitrate values
        corrResult <- getComplete(fileN)
        if (is.null(corrResult)) {
            next
        }
        else {
            corrVector <- c(corrVector, corrResult)
        }
    }  

    # Set working directory back to old
    setwd(oldwd)
    
    corrVector
}
