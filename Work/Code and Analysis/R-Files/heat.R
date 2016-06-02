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

### Get auxilliary functions
source('Code and Analysis/R-Files/Auxlliary_Functions.R')

### Get Data 
cosine.cat     <- json.unlist(fromJSON(file='Code and Analysis/Results/Real data/21/cosine_cat.txt', method='C'))
cosine.ent     <- json.unlist(fromJSON(file='Code and Analysis/Results/Real data/21/cosine_ent.txt', method='C'))
edr.ent        <- json.unlist(fromJSON(file='Code and Analysis/Results/Real data/21/edr_sim.txt', method='C'))
eskim.cho      <- json.unlist(fromJSON(file='Code and Analysis/Results/Real data/21/eskin_sim.txt', method='C'))
euclid.cho.dis <- json.unlist(fromJSON(file='Code and Analysis/Results/Real data/21/eucliddist.txt', method='C'))
lin.cho.dis    <- json.unlist(fromJSON(file='Code and Analysis/Results/Real data/21/lin_disim.txt', method='C'))
lin.cho.sim    <- json.unlist(fromJSON(file='Code and Analysis/Results/Real data/21/lin_sim.txt', method='C'))
overlap.cho    <- json.unlist(fromJSON(file='Code and Analysis/Results/Real data/21/overlap.txt', method='C'))
rbf.ent        <- json.unlist(fromJSON(file='Code and Analysis/Results/Real data/21/rbf.txt', method='C'))
timewarp.ent   <- json.unlist(fromJSON(file='Code and Analysis/Results/Real data/21/timewarp.txt', method='C'))




### Reset wd to report 
setwd('Report/TeX/Pictures/')

################################################################################

################################################################################

thief      <- rep("Theft",22)
robbery    <- rep("Robbery",6)
sex        <- rep("Sex",17)
drug       <- rep("Drug",22)
owi        <- rep("OWI",4)
aussault   <- rep("Assault",10)
escape     <- rep("Escape",4)
vandalism  <- rep("Vandalism",1)
forgery    <- rep("Forgery",7)
probabiton <- rep("Probabiton",1)
other      <- rep("Other",2) 
healthy    <- rep("Healthy",96)
all.names  <- c(thief,robbery,sex,drug,owi,aussault,escape,
                vandalism,forgery,probabiton,other,healthy)

h01 <- my.heatmap( cosine.cat,nco=200,colors = "Reds", rname = all.names)
h02 <- my.heatmap( cosine.ent,nco=200,colors = "Reds", rname = all.names)
h03 <- my.heatmap( edr.ent,nco=200,colors = "Reds", rname = all.names)
h04 <- my.heatmap( eskim.cho,nco=200,colors = "Reds", rname = all.names)
h05 <- my.heatmap( euclid.cho.dis,nco=200,colors = "Reds", rname = all.names)
h06 <- my.heatmap( lin.cho.dis,nco=200,colors = "Reds", rname = all.names)
h07 <- my.heatmap( lin.cho.sim,nco=200,colors = "Reds", rname = all.names)
h08 <- my.heatmap( overlap.cho,nco=200,colors = "Reds", rname = all.names)
h09 <- my.heatmap( rbf.ent,nco=200,colors = "Reds", rname = all.names)
h09 <- my.heatmap( timewarp.ent,nco=200,colors = "Reds", rname = all.names)

################################################################################

################################################################################

