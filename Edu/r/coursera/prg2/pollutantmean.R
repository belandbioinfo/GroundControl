"""function named 'pollutantmean' that calculates the mean of a pollutant 
(sulfate or nitrate) across a specified list of monitors.

Author: Kevin Beland (belandbioinfo@gmail.com)
Assignment 2 Part 1

"""

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
        goodValues <- data[!naValues]
    }

    vectorToMean <-  
}
