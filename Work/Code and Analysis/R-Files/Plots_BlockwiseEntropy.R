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

e00  <- read.csv('Code and Analysis/Results/Real data/00/eb00.csv')
e01  <- read.csv('Code and Analysis/Results/Real data/01/eb01.csv')
e02 <- read.csv('Code and Analysis/Results/Real data/02/eb02.csv')
e03 <- read.csv('Code and Analysis/Results/Real data/03/eb03.csv')
e04 <- read.csv('Code and Analysis/Results/Real data/04/eb04.csv')
e05 <- read.csv('Code and Analysis/Results/Real data/05/eb05.csv')
e06 <- read.csv('Code and Analysis/Results/Real data/06/eb06.csv')
e07 <- read.csv('Code and Analysis/Results/Real data/07/eb07.csv')
#b08 <- read.csv('Code and Analysis/Results/Real data/08/e08.csv')
e09 <- read.csv('Code and Analysis/Results/Real data/09/eb09.csv')
#b10 <- read.csv('Code and Analysis/Results/Real data/10/e10.csv')
e20 <- read.csv('Code and Analysis/Results/Real data/20/eb20.csv')
e21 <- read.csv('Code and Analysis/Results/Real data/21/eb21.csv')
e66 <- read.csv('Code and Analysis/Results/Real data/66/eb66.csv')
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

tikz("entbl.tex", width = 3.5, height =3.5)
plot(x,col.average[2,],type="l",ylim=c(0,2), col = cols[1], 
     xlab = "Steps", ylab= "Avergage entropy", lwd=1.5,
     cex.lab=0.8,
     cex.axis = 0.5,
     tck=-0.03,
     las=1,
     mgp = c(2, 0.5, 0) )
for( i in 3:nrow(col.average)){
  lines(x,col.average[i,],col = cols[i],lwd=1.5)
}
legend("bottomright",
       c("Theft","Robbery","Sex", "Drug","OWI","Assault/Murder","Escape","Forgery","Other","Healthy"),
       lty = 1,
       col = cols[1:10],
       cex = 0.4,
       bty = "n",
       ncol = 2,
       y.intersp = 2
)
dev.off()


