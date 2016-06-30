# ----------------------------------------------------------------------
# Preamble
# ----------------------------------------------------------------------

# Load Packages
if (!require("rjson")) install.packages("rjson"); library(rjson)
if (!require("tikzDevice"))   install.packages("tikzDevice");   library(tikzDevice)
# Set working directory
setwd('/Users/felix/Documents/GSE/Term 3/Master_Project/Master-Project/Work/Code and Analysis/R-Files/bandits/')
list.files()
# Load Experiment 1 Data 
exp01  <- read.table('exp01.csv',sep=',',header = FALSE)
e01c02 <- fromJSON(file='JSON_exp1_2_CL2.txt', method='C')
e01c03 <- fromJSON(file='JSON_exp1_2_CL3.txt', method='C') 

# Load Experiment 2 Data 
exp02 <- read.table('exp02.csv',sep=',',header = FALSE)
e02c02 <- fromJSON(file='JSON_exp2_1_CL2.txt', method='C')
e02c03 <- fromJSON(file='JSON_exp2_1_CL3.txt', method='C') 

# Load Experiment 3 Data 
exp03 <- read.table('exp03.csv',sep=',',header = FALSE)
e02c02 <- fromJSON(file='JSON_exp2_2_CL2.txt', method='C')
e02c03 <- fromJSON(file='JSON_exp2_2_CL3.txt', method='C') 

# Load Experiment 4 Data 
exp04 <- read.table('exp04.csv',sep=',',header = FALSE)
e02c02 <- fromJSON(file='JSON_exp2_2_CL2.txt', method='C')
e02c03 <- fromJSON(file='JSON_exp2_2_CL3.txt', method='C') 

# Reset directort
setwd('~/Documents/GSE/Term 3/Master_Project/Master-Project/Work/')
setwd('Report/TeX/Pictures/')

# ----------------------------------------------------------------------
# Init functions for clustering inspection
# ----------------------------------------------------------------------

# Plot clustering based on cluster id
plot.cluster <- function(data,cluster.list,cluster.id){
  
  # Define data
  exp01 <- data
  
  # Reset super high values
  for( i in 1:nrow(exp01)){
    
    if(exp01[i,2] > 6 ){
      
        exp01[i,2] <- 6+runif(1)
       }
  }
  
  # Define colors for dots
  col = unlist(cluster.list$predictions[cluster.id])
  
  # Set title
  title = unlist(cluster.list$algorithm[cluster.id])
  
  # Plot data
  plot(exp01[,1],exp01[,2],ylim=c(0,7),cex=1,col=col+2,xlab='Alpha',ylab ='Theta',
       cex.lab=0.5,cex.axis=0.7, mgp=c(1,0.1,0),tck=-0.01,pch=1,main=title)
  
}

# Automize procedure with define sleeping time
dynamic.clust.plot <- function(dat,alist,sys.t=3){
  
  # Check how many clusters there are
  n <- length(unlist(alist$algorithm))
  
  # Plot data automatically - updating after t seconds
  for( i in 1:n){
    
    Sys.sleep(sys.t)
    plot.cluster(dat,alist,i)
    print(i)
    
  }

}

# ----------------------------------------------------------------------
# Init functions for clustering inspection
# ----------------------------------------------------------------------

# Experiment 1

dynamic.clust.plot(exp01,e01c02,5)
dynamic.clust.plot(exp01,e01c03,5)

# Experiment 2

dynamic.clust.plot(exp02,e02c02,37)
dynamic.clust.plot(exp02,e02c03,5)

# ----------------------------------------------------------------------
# Plots for report
# ----------------------------------------------------------------------

x <- exp01[,1]
y <- exp01[,2]

x1 <- x[as.numeric(test)]
y1 <- y[test]

plot(x1,y1)
head(x1)
as.numeric(test)

length(x)

for( i in 1:nrow(exp01)){
  
  if(y[i] > 6 ){
    
    y[i] <- 6+runif(1, min = 0, max = 0.1)
  }

}
cols <- unlist(e01c02$predictions[45])
cols2 <- ifelse(cols==0,rainbow(20)[15],rainbow(20)[19])
unlist(e01c02$algorithm[45])
pchs <- as.numeric(ifelse(cols==0,8,16))
tikz("e1c2.tex", width = 3.5, height =3.5)
plot(x,y,
     pch=pchs,
     cex=1.3,
     col=cols2, 
     xlab = "Estimated alpha/eta", 
     ylab= "Estimated theta / tau-inverse",
     cex.lab=0.9,
     cex.axis = 0.6,
     tck=-0.02,
     las=1,
     mgp = c(2.1, 1, 0) 
     )
dev.off()

cols <- unlist(e01c03$predictions[38])
cols2 <- cols
test <- which(cols==0)
cols[cols==0] <- rainbow(20)[15] 
cols[cols==1] <- rainbow(20)[19]
cols[cols==2] <- rainbow(20)[6]
unlist(e01c02$algorithm[38])
pchs <- cols2
pchs[pchs==0] <- 7
pchs[pchs==1] <- 8
pchs[pchs==2] <- 16
tikz("e1c3.tex", width = 3.5, height =3.5)
plot(x,y,
     pch=pchs,
     cex=1.3,
     col=cols, 
     xlab = "Estimated alpha/eta", 
     ylab= "Estimated theta / tau-inverse",
     cex.lab=0.9,
     cex.axis = 0.6,
     tck=-0.02,
     las=1,
     mgp = c(2.1, 1, 0) 
)
dev.off()

# Experiment 2

x <- exp02[,1]
y <- exp02[,2]


for( i in 1:nrow(exp02)){
  
  if(y[i] > 6 ){
    
    y[i] <- 6+runif(1, min = 0, max = 0.1)
  }
  
}
cols <- unlist(e02c02$predictions[37])
cols2 <- ifelse(cols==0,rainbow(20)[15],rainbow(20)[19])
unlist(e02c02$algorithm[37])
pchs <- as.numeric(ifelse(cols==0,8,16))
tikz("e2c2.tex", width = 3.5, height =3.5)
plot(x,y,
     pch=pchs,
     cex=1.3,
     col=cols2, 
     xlab = "Estimated alpha/eta", 
     ylab= "Estimated theta / tau-inverse",
     cex.lab=0.9,
     cex.axis = 0.6,
     tck=-0.02,
     las=1,
     mgp = c(2.1, 1, 0) 
)
dev.off()

cols <- unlist(e02c03$predictions[28])
cols2 <- cols
cols[cols==0] <- rainbow(20)[15] 
cols[cols==1] <- rainbow(20)[19]
cols[cols==2] <- rainbow(20)[6]
unlist(e02c02$algorithm[28])
pchs <- cols2
pchs[pchs==0] <- 7
pchs[pchs==1] <- 8
pchs[pchs==2] <- 16
tikz("e2c3.tex", width = 3.5, height =3.5)
plot(x,y,
     pch=pchs,
     cex=1.3,
     col=cols, 
     xlab = "Estimated alpha/eta", 
     ylab= "Estimated theta / tau-inverse",
     cex.lab=0.9,
     cex.axis = 0.6,
     tck=-0.02,
     las=1,
     mgp = c(2.1, 1, 0) 
)
dev.off()


