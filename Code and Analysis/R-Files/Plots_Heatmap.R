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

e00 <- read.csv('Code and Analysis/Results/Real data/00/e00.csv')
e01 <- read.csv('Code and Analysis/Results/Real data/01/e01.csv')
e02 <- read.csv('Code and Analysis/Results/Real data/02/e02.csv')
e03 <- read.csv('Code and Analysis/Results/Real data/03/e03.csv')
e04 <- read.csv('Code and Analysis/Results/Real data/04/e04.csv')
e05 <- read.csv('Code and Analysis/Results/Real data/05/e05.csv')
e06 <- read.csv('Code and Analysis/Results/Real data/06/e06.csv')
e07 <- read.csv('Code and Analysis/Results/Real data/07/e07.csv')
#b08 <- read.csv('Code and Analysis/Results/Real data/08/e08.csv')
e09 <- read.csv('Code and Analysis/Results/Real data/09/e09.csv')
#b10 <- read.csv('Code and Analysis/Results/Real data/10/e10.csv')
e20 <- read.csv('Code and Analysis/Results/Real data/20/e20.csv')
e21 <- read.csv('Code and Analysis/Results/Real data/21/e21.csv')
e66 <- read.csv('Code and Analysis/Results/Real data/66/e66.csv')
### Reset wd to report 
setwd('Report/TeX/Pictures/')

################################################################################

################################################################################

# Compute Basic variables
N <- 12
M <- ncol(e00)
variables   <- ls()[1:12]
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
cols <- brewer.pal(12, 'Set3')

plot(x,col.average[2,],type="l",ylim=c(0,2), col = cols[1], 
     xlab = "Steps", ylab= "Avergage entropy accross groups" )
for( i in 3:nrow(col.average)){
  lines(x,col.average[i,],col = cols[i])
}
legend("bottomright",
       c("Theft","Robbery","Sex", "Drug","OWI","Assault/Murder","Escape","Forgery","Other","Healthy"),
       lty = 1,
       col = cols[1:10],
       cex = 1,
       bty = "n",
       ncol = 2,
       y.intersp = 2,
)
title(main ="Average Entropy of Criminals vs. Controll Group")

# 2) Full average
M02 <- nrow(col.average)
plot(x, col.average[1,],type="l",ylim=c(0,2), col = 'red',
     xlab = "Steps", ylab= "Avergage entropy choice")
lines(x,col.average[M02,],col ='blue')
legend("bottomright",
       c("Criminals","Controll"),
       lty = 1,
       col = c('red','blue'),
       cex = 1,
       bty = "n",
       ncol = 1,
       y.intersp = 2,
)
title(main ="Average Entropy of Criminals vs. Controll Group")
################################################################################

################################################################################

# 3) Individual entropies




