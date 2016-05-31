setwd('/Users/felix/Documents/GSE/Term 3/External Data/mixed data/')

prison <- read.csv('choices_num.csv',sep="",header=FALSE)
health <- read.csv('choice_100.csv',sep=";",header=FALSE)

N01 <- nrow(prison)
N02 <- nrow(health)

set.seed(123)
sample <- sample.int(96)

new.frame <- rbind(prison,health[sample,])

write.table(new.frame,"choices_combined.csv",col.names = FALSE,row.names = FALSE)
