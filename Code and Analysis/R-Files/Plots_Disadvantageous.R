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

#b00 <- read.csv('Code and Analysis/Results/Real data/00/b00.csv')
b01 <- read.csv('Code and Analysis/Results/Real data/01/b01_SOLO.csv')
b02 <- read.csv('Code and Analysis/Results/Real data/02/b02_SOLO.csv')
b03 <- read.csv('Code and Analysis/Results/Real data/03/b03_SOLO.csv')
b04 <- read.csv('Code and Analysis/Results/Real data/04/b04_SOLO.csv')
#b05 <- read.csv('Code and Analysis/Results/Real data/05/b05.csv')
b06 <- read.csv('Code and Analysis/Results/Real data/06/b06_SOLO.csv')
#b07 <- read.csv('Code and Analysis/Results/Real data/07/b07.csv')
#b08 <- read.csv('Code and Analysis/Results/Real data/08/b08.csv')
b09 <- read.csv('Code and Analysis/Results/Real data/09/b09_SOLO.csv')
#b10 <- read.csv('Code and Analysis/Results/Real data/10/b10.csv')
#b20 <- read.csv('Code and Analysis/Results/Real data/20/b20.csv')
#b21 <- read.csv('Code and Analysis/Results/Real data/21/b21.csv')
#b66 <- read.csv('Code and Analysis/Results/Real data/66/b66.csv')
### Reset wd to report 
setwd('Report/TeX/Pictures/')

################################################################################

################################################################################

N <- 6
M <- ncol(b01)

variables   <- ls()[1:6]

my.env      <- new.env()
col.average <- matrix( NA , nrow = N , ncol = (M-1) )
for( i in 1:N ){
  temp.frame <- get( variables[i], envir = my.env )
  temp.mean  <- colMeans( temp.frame[,2:M] )
  col.average[i,] <- temp.mean
}


x    <- 1:(M-1)
cols <- brewer.pal(12, 'Set3')

tikz("disad.tex", width = 3.5, height =3.5)
    plot(x,col.average[1,],type="b",ylim=c(0,1), col = cols[1], 
         xlab = "Steps", ylab= "Avergage disadvantage choice",
         lwd=2,
         cex.lab=0.9,
         cex.axis = 0.6,
         pch = 1,
         cex = 0.6,
         tck=-0.03,
         las=1,
         mgp = c(2, 0.5, 0) ) 
    for( i in 2:nrow(col.average)){
      lines(x,col.average[i,],col = cols[i],lwd=2,pch=i,type='b',cex=0.6)
    }
    legend("bottomleft",
           c("Theft","Robbery","Sex", "Drug","Assault","Forgery"),
           lty = 1,
           pch = 1:16,
           col = cols[1:6],
           cex = 0.6,
           bty = "n",
           ncol = 4,
           y.intersp = 2
    )
dev.off()

# Average 
plot(x, col.average[1,],type="l",ylim=c(0,1), col = 'red',
     xlab = "Steps", ylab= "Avergage disadvantage choice")
lines(x,col.average[M,],col ='blue')
axis(1, at = seq(1, 10, by = 2), las=1)
legend("bottomleft",
       c("Criminals","Healthy"),
       lty = 1,
       col = c('red','blue'),
       cex = 1,
       bty = "n",
       ncol = 2,
       y.intersp = 2,
)

################################################################################

################################################################################