################################################################################
# Preamble
################################################################################

### Clear workspace
rm(list = ls())

### Set general file path
setwd('~/Documents/GSE/Term 3/Master_Project/Master-Project/Work/')

### Load Packages 
if (!require("RColorBrewer")) install.packages("RColorBrewer"); library(RColorBrewer)
if (!require("rjson"))        install.packages("rjson");        library(rjson)
if (!require("tikzDevice")) install.packages("tikzDevice"); library(tikzDevice)

### Get auxilliary functions
source('Code and Analysis/R-Files/Auxlliary_Functions.R')

### Get Data 
entropy.sim <- json.unlist(fromJSON(file='Code and Analysis/Data/Artificial Data Sets/d05/entropy_softmax_21_23_53.txt', method='C'))

### Reset wd to report 
setwd('Report/TeX/Pictures/')

### Styling options

################################################################################

################################################################################

cols <- c(rep('red',20),rep('green',20),rep('blue',20))
x    <- 1:ncol(entropy.sim)
tikz("tikz-example.tex", width = 3.5, height =3.5)
plot(x,entropy.sim[1,],type="l",ylim=c(0,1.6), col = cols[1], xlab = "Steps", ylab= "Sequentiel Entropy" )
for( i in 2:nrow(entropy.sim)){
  lines(x,entropy.sim[i,],col = cols[i])
}
legend("bottomright",
       c("alpha = 0.5 | tau = 0.1","alpha = 0.5 | tau = 0.7"," alpha = 0.5 | tau = 1.8"),
       lty = 1,
       col = c('red','green','blue'),
       cex = 1,
       bty = "n",
       ncol = 1,
       y.intersp = 2,
)
title(main="$p(x)=\\frac{1}{\\sqrt{2\\pi}}e^{-\\frac{x^2}{2}}$")
dev.off()
