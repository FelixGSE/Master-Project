
#Load Packages
if (!require("rjson")) install.packages("rjson"); library(rjson)
if (!require("tikzDevice"))   install.packages("tikzDevice");   library(tikzDevice)

# Set working directory
setwd('/Users/felix/Documents/GSE/Term 3/Master_Project/Master-Project/Work/Code and Analysis/R-Files/bandits/')
cr <- read.csv("~/Documents/GSE/Term 3/Master_Project/Master-Project/Work/Code and Analysis/R-Files/bandits/hrvoje_multiarm_choicerank.csv", sep=",")
e  <-read.csv("~/Documents/GSE/Term 3/Master_Project/Master-Project/Work/Code and Analysis/R-Files/bandits/hrvoje_multiarm_entropy_block.csv", sep=",")
 
e01c02 <- fromJSON(file='JSON_exp1_2_CL2.txt', method='C')
e01c03 <- fromJSON(file='JSON_exp1_2_CL3.txt', method='C') 
e02c02 <- fromJSON(file='JSON_exp2_1_CL2.txt', method='C')
e02c03 <- fromJSON(file='JSON_exp2_1_CL3.txt', method='C') 


setwd('~/Documents/GSE/Term 3/Master_Project/Master-Project/Work/')
setwd('Report/TeX/Pictures/')


105:205

cre1 <- cr[1:104,]
ee1  <- e[1:104,]
inde1c2  <- which(filter.cluster(e01c02,45)==1)
inde1com <- setdiff(1:104,inde1c2) 
avg01 <- colMeans(ee1[inde1c2,])
avg02 <- colMeans(ee1[inde1com,])
x <- 1:10


cols <- c(rainbow(20)[19],rainbow(20)[15])

tikz("entblbe1c1.tex", width = 3.5, height =3.5)
plot(x,avg01[-c(1)], col = cols[1], 
     type='b', 
     ylim = c(0,3.5),
     xlab = "Steps", 
     ylab= "Avergage entropy accross groups",
     lwd=2,
     cex.lab=0.9,
     cex.axis = 0.6,
     pch = 16,
     cex = 0.6,
     tck=-0.03,
     las=1,
     mgp = c(2, 0.5, 0) )  
lines(x,avg02[-c(1)],col=cols[2],lwd=2,pch=8,type='b',cex=0.6)
legend("bottomleft",
       c('First Cluster','Second Cluster'),
       lty = 1,
       pch = 1:2,
       col = cols[c(1,2)],
       cex = 0.6,
       bty = "n",
       ncol = 4,
       y.intersp = 2
)
dev.off()

# Choice 

avg03 <- colMeans(cre1[inde1c2,])
avg04 <- colMeans(cre1[inde1com,])


x <- 1:100
tikz("crange1c1.tex", width = 3.5, height =3.5)
plot(x,avg03,type="l",ylim=c(0,12), col = cols[1], 
     xlab = "Steps", ylab= "Average choice rank",
     lwd=2,
     cex.lab=0.9,
     cex.axis = 0.6,
     pch = 1,
     cex = 0.6,
     tck=-0.03,
     las=1,
     mgp = c(2, 0.5, 0) ) 
lines(x,avg04,col = cols[2],lwd=2,lty=3,cex=0.6)
dev.off()
############################################################################


cre1 <- cr[105:205,]
ee1  <- e[105:205,]
inde1c2  <- which(filter.cluster(e02c02,37)==1)
inde1com <- setdiff(1:101,inde1c2) 
avg01 <- colMeans(ee1[inde1c2,])
avg02 <- colMeans(ee1[inde1com,])
x <- 1:10
cols <- c(rainbow(20)[19],rainbow(20)[15])


tikz("entblbe2c1.tex", width = 3.5, height =3.5)
plot(x,avg01[-c(1)], col = cols[1], 
     type='b', 
     ylim = c(0,3.5),
     xlab = "Steps", 
     ylab= "Avergage entropy accross groups",
     lwd=2,
     cex.lab=0.9,
     cex.axis = 0.6,
     pch = 16,
     cex = 0.6,
     tck=-0.03,
     las=1,
     mgp = c(2, 0.5, 0) )  
lines(x,avg02[-c(1)],col=cols[2],lwd=2,pch=8,type='b',cex=0.6)
legend("bottomleft",
       c('First Cluster','Second Cluster'),
       lty = 1,
       pch = 1:2,
       col = cols[c(1,3)],
       cex = 0.6,
       bty = "n",
       ncol = 4,
       y.intersp = 2
)
dev.off()

# Choice 

avg03 <- colMeans(cre1[inde1c2,])
avg04 <- colMeans(cre1[inde1com,])


x <- 1:100
tikz("crange2c1.tex", width = 3.5, height =3.5)
plot(x,avg03,type="l",ylim=c(0,12), col = cols[1], 
     xlab = "Steps", ylab= "Average choice rank",
     lwd=2,
     cex.lab=0.9,
     cex.axis = 0.6,
     pch = 1,
     cex = 0.6,
     tck=-0.03,
     las=1,
     mgp = c(2, 0.5, 0) ) 
lines(x,avg04,col = cols[2],lwd=2,lty=3,cex=0.6)
dev.off()






###############################################


cre1 <- cr[1:104,]
ee1  <- e[1:104,]
inde1c31  <- which(filter.cluster(e01c03,38)==0)
inde1c32  <- which(filter.cluster(e01c03,38)==1)
inde1c33  <- which(filter.cluster(e01c03,38)==2)

avg01 <- colMeans(ee1[inde1c31,])
avg02 <- colMeans(ee1[inde1c32,])
avg03 <- colMeans(ee1[inde1c33,])
x <- 1:10
cols <- c(rainbow(20)[15],rainbow(20)[19],rainbow(20)[6])


tikz("entblbe1c2.tex", width = 3.5, height =3.5)
plot(x,avg01[-c(1)], col = cols[2], 
     type='b', 
     ylim = c(0,3.5),
     xlab = "Steps", 
     ylab= "Avergage entropy accross groups",
     lwd=2,
     cex.lab=0.9,
     cex.axis = 0.6,
     pch = 8,
     cex = 0.6,
     tck=-0.03,
     las=1,
     mgp = c(2, 0.5, 0) )  
lines(x,avg02[-c(1)],col=cols[1],lwd=2,pch=7,type='b',cex=0.6)
lines(x,avg03[-c(1)],col=cols[3],lwd=2,pch=16,type='b',cex=0.6)

legend("bottomleft",
       c('First Cluster','Second Cluster','Third Cluster'),
       lty = 1,
       pch = c(8,7,6),
       col = cols[c(2,1,3)],
       cex = 0.6,
       bty = "n",
       ncol = 1,
       y.intersp = 2
)
dev.off()

# Choice 

avg03 <- colMeans(cre1[inde1c31,])
avg04 <- colMeans(cre1[inde1c32,])
avg05 <- colMeans(cre1[inde1c33,])

x <- 1:100
tikz("crange1c2.tex", width = 3.5, height =3.5)
plot(x,avg03,type="l",ylim=c(0,12), col = cols[2], 
     xlab = "Steps", ylab= "Average choice rank",
     lwd=2,
     cex.lab=0.9,
     cex.axis = 0.6,
     pch = 1,
     cex = 0.6,
     tck=-0.03,
     las=1,
     mgp = c(2, 0.5, 0) ) 
lines(x,avg04,col = cols[1],lwd=2,lty=3,cex=0.6)
lines(x,avg05,col = cols[3],lwd=2,lty=4,cex=0.6)
legend("bottomleft",
       c('First Cluster','Second Cluster','Third Cluster'),
       lty = 1,
       pch = c(8,7,6),
       col =cols[c(2,1,3)],
       cex = 0.6,
       bty = "n",
       ncol = 1,
       y.intersp = 2
)
dev.off()




cre1 <- cr[105:205,]
ee1  <- e[105:205,]
inde1c31  <- which(filter.cluster(e02c03,28)==0)
inde1c32  <- which(filter.cluster(e02c03,28)==1)
inde1c33  <- which(filter.cluster(e02c03,28)==2)

avg01 <- colMeans(ee1[inde1c31,])
avg02 <- colMeans(ee1[inde1c32,])
avg03 <- colMeans(ee1[inde1c33,])
x <- 1:10
cols <- c(rainbow(20)[15],rainbow(20)[19],rainbow(20)[6])
c(8,7,6)
tikz("entblbe2c2.tex", width = 3.5, height =3.5)
plot(x,avg01[-c(1)], col = cols[1], 
     type='b', 
     ylim = c(0,3.5),
     xlab = "Steps", 
     ylab= "Avergage entropy accross groups",
     lwd=2,
     cex.lab=0.9,
     cex.axis = 0.6,
     cex = 0.6,
     tck=-0.03,
     las=1,
     pch=8,
     mgp = c(2, 0.5, 0) )  
lines(x,avg02[-c(1)],col=cols[2],lwd=2,pch=7,type='b',cex=0.6)
lines(x,avg03[-c(1)],col=cols[3],lwd=2,pch=6,type='b',cex=0.6)

legend("bottomleft",
       c('First Cluster','Second Cluster','Third Cluster'),
       lty = 1,
       pch = 1:3,
       col = cols[c(1,3,4)],
       cex = 0.6,
       bty = "n",
       ncol = 1,
       y.intersp = 2
)
dev.off()

# Choice 

avg03 <- colMeans(cre1[inde1c31,])
avg04 <- colMeans(cre1[inde1c32,])
avg05 <- colMeans(cre1[inde1c33,])

x <- 1:100
tikz("crange2c2.tex", width = 3.5, height =3.5)
plot(x,avg03,type="l",ylim=c(5,12), col = cols[1], 
     xlab = "Steps", ylab= "Average choice rank",
     lwd=2,
     cex.lab=0.9,
     cex.axis = 0.6,
     pch = 1,
     cex = 0.6,
     tck=-0.03,
     las=1,
     mgp = c(2, 0.5, 0) ) 
lines(x,avg04,col = cols[2],lwd=2,lty=3,cex=0.6)
lines(x,avg05,col = cols[3],lwd=2,lty=4,cex=0.6)
dev.off()








filter.cluster <- function(lst,index){
  
  
  res <- as.numeric(unlist(lst$predictions[index]))
  return(res)
}
 

