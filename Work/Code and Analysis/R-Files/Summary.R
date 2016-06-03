################################################################################
# Preamble
################################################################################

### Clear workspace
rm(list = ls())

### Set general file path
setwd('~/Documents/GSE/Term 3/Master_Project/Master-Project/Work/')

### Load Packages 
if (!require("stargazer")) install.packages("stargazer"); library(stargazer)

### Get auxilliary functions
source('Code and Analysis/R-Files/Auxlliary_Functions.R')

### Get Data 
source('Code and Analysis/R-Files/Load_Data.R')

### Load Data
df01 <- read.csv2("~/Documents/GSE/Term 3/External Data/prisondata/characteristics.csv")

################################################################################

################################################################################

df02 <- df01[,-1]
rownames(df02) <- df01[,1]
df03 <- t(df02)
colnames(df03)[21] <- "iq"
colnames(df03)[20] <- "tabe"

#  Means by crime
df.count <- as.numeric(table(df03[,5]))
df.age   <- aggregate( age  ~ crime , data=df03, mean )
df.educ  <- aggregate( education  ~ crime , data=df03, mean ) 
df.tabe  <- aggregate( tabe ~ crime , data=df03, mean ) 
df.IQ    <- aggregate( iq ~ crime , data=df03, mean ) 

# Standard deviation by crime
sd.count <- as.numeric(table(df03[,5]))
sd.age   <- aggregate( age  ~ crime , data=df03, sd )
sd.educ  <- aggregate( education  ~ crime , data=df03, sd ) 
sd.tabe  <- aggregate( tabe ~ crime , data=df03, sd ) 
sd.IQ    <- aggregate( iq ~ crime , data=df03, sd ) 
sd.merge <- Reduce(merge, list(sd.age,sd.educ,sd.tabe,sd.IQ))


# Merge 
rnames <- c("Theft/Burglary","Robbery","Sex","Drug","OWI","Assault",
            "Escape/ Failure To Appear","Vandalism","Forgery",
            "Probabiton","Other")
cnames <- c("Count","Age","TABE Score","Education","Beta IQ")
merge.frame <- Reduce(merge, list(df.age,df.educ,df.tabe,df.IQ))
final.frame <- as.data.frame(append(merge.frame , list(Count = df.count), after = 1))[,-1]
rownames(final.frame) <- rnames
colnames(final.frame) <- cnames
is.num <- sapply(final.frame, is.numeric)
final.frame[is.num] <- lapply(final.frame[is.num], round, 2)

stargazer(final.frame, summary=TRUE, rownames=TRUE)




################################################################################

################################################################################