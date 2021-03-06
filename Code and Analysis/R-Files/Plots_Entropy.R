################################################################################
# Preamble
################################################################################

### Clear workspace
rm(list = ls())

### Set general file path
setwd('~/Documents/GSE/Term 3/Master_Project/Master-Project/Work/')

### Load Packages 
if (!require("RColorBrewer")) install.packages("RColorBrewer"); library(RColorBrewer)
if (!require("tikzDevice"))   install.packages("tikzDevice");   library(tikzDevice)

### Get auxilliary functions
source('Code and Analysis/R-Files/Auxlliary_Functions.R')

### Get Data 

#e00  <- read.csv('Code and Analysis/Results/Real data/00/e00_SOLO.csv')
e01  <- read.csv('Code and Analysis/Results/Real data/01/e01_SOLO.csv')
e02 <- read.csv('Code and Analysis/Results/Real data/02/e02_SOLO.csv')
e03 <- read.csv('Code and Analysis/Results/Real data/03/e03_SOLO.csv')
e04 <- read.csv('Code and Analysis/Results/Real data/04/e04_SOLO.csv')
#e05 <- read.csv('Code and Analysis/Results/Real data/05/e05_SOLO.csv')
e06 <- read.csv('Code and Analysis/Results/Real data/06/e06_SOLO.csv')
#e07 <- read.csv('Code and Analysis/Results/Real data/07/e07.csv')
#b08 <- read.csv('Code and Analysis/Results/Real data/08/e08.csv')
e09 <- read.csv('Code and Analysis/Results/Real data/09/e09_SOLO.csv')
#b10 <- read.csv('Code and Analysis/Results/Real data/10/e10.csv')
#e20 <- read.csv('Code and Analysis/Results/Real data/20/e20.csv')
#e21 <- read.csv('Code and Analysis/Results/Real data/21/e21.csv')
#e66 <- read.csv('Code and Analysis/Results/Real data/66/e66.csv')
### Reset wd to report 
setwd('Report/TeX/Pictures/')

################################################################################

################################################################################

# Compute Basic variables
N <- 6
M <- ncol(e01)
variables   <- ls()[1:6]
my.env      <- new.env()

# Compute average over columns
col.average <- matrix( NA , nrow = N , ncol = (M-1) )
for( i in 1:N ){
  temp.frame <- get( variables[i], envir = my.env )
  temp.mean  <- colMeans( temp.frame[,2:M] )
  col.average[i,] <- temp.mean
}


# 1) Plot acrros groups
x    <- 1:(M-1)
cols <- brewer.pal(11, 'Set3')

tikz("avgent.tex", width = 3.5, height =3.5)
  plot(x,col.average[1,],type="l",ylim=c(0,2), col = cols[1], 
       xlab = "Steps", ylab= "Avergage entropy",
       lwd=2,
       cex.lab=0.9,
       cex.axis = 0.6,
       pch = 1,
       cex = 0.6,
       tck=-0.03,
       las=1,
       mgp = c(2, 0.5, 0) ) 
  for( i in 2:nrow(col.average)){
    lines(x,col.average[i,],col = cols[i],lwd=2,lty=i,cex=0.6)
  }
dev.off()

# 2) Full average
M02 <- nrow(col.average)

tikz("fullavg.tex", width = 3.5, height =3.5)
  plot(x, col.average[1,],type="l",ylim=c(0,2), col = 'red',
       xlab = "Steps", ylab= "Avergage entropy", 
       lwd=1.5,
       cex.lab=0.8,
       cex.axis = 0.5,
       tck=-0.03,
       las=1,
       mgp = c(2, 0.5, 0) )
  lines(x,col.average[M02,],col ='blue')
  legend("bottomright",
         c("Criminals","Controll"),
         lty = 1,
         col = c('red','blue'),
         cex = 0.4,
         bty = "n",
         ncol = 1,
         y.intersp = 2,
  )
dev.off()

