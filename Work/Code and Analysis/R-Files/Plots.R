################################################################################
# Preamble
################################################################################

### Clear workspace
rm(list = ls())

### Set general file path
setwd('~/Documents/GSE/Term 3/Master_Project/Master-Project/Work/')

### Load Packages 
if (!require("RColorBrewer")) install.packages("RColorBrewer"); library(RColorBrewer)

### Get auxilliary functions
source('Code and Analysis/R-Files/Auxlliary_Functions.R')

### Get Data 

b00 <- read.csv('Code and Analysis/Results/Real data/00/b00.csv')
b01 <- read.csv('Code and Analysis/Results/Real data/01/b01.csv')
b02 <- read.csv('Code and Analysis/Results/Real data/02/b02.csv')
b03 <- read.csv('Code and Analysis/Results/Real data/03/b03.csv')
b04 <- read.csv('Code and Analysis/Results/Real data/04/b04.csv')
b05 <- read.csv('Code and Analysis/Results/Real data/05/b05.csv')
b06 <- read.csv('Code and Analysis/Results/Real data/06/b06.csv')
b07 <- read.csv('Code and Analysis/Results/Real data/07/b07.csv')
#b08 <- read.csv('Code and Analysis/Results/Real data/08/b08.csv')
b09 <- read.csv('Code and Analysis/Results/Real data/09/b09.csv')
#b10 <- read.csv('Code and Analysis/Results/Real data/10/b10.csv')
b20 <- read.csv('Code and Analysis/Results/Real data/20/b20.csv')
b21 <- read.csv('Code and Analysis/Results/Real data/21/b21.csv')
b66 <- read.csv('Code and Analysis/Results/Real data/66/b66.csv')
### Reset wd to report 
setwd('Report/TeX/Pictures/')

################################################################################

################################################################################
N <- 12
M <- ncol(b00)

variables   <- ls()[1:12]
my.env      <- new.env()
col.average <- matrix( NA , nrow = N , ncol = (M-1) )
for( i in 1:N ){
  temp.frame <- get( variables[i], envir = my.env )
  temp.mean  <- colMeans( temp.frame[,2:M] )
  col.average[i,] <- temp.mean
}


x <- 1:(M-1)
plot(x,col.average[1,],type="l",ylim=c(0,1))
for( i in 2:nrow(col.average)){
  
  lines(x,col.average[i,])
}



plot(x,col.average[N,],type="l",ylim=c(0,1))

################################################################################

################################################################################