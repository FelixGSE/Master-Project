
setwd('/Users/felix/Documents/GSE/Term 3/Master_Project/Master-Project/Work/Code and Analysis/Results')

d <- Cocaine_Summary
d <- 9vA_full
dim(d)
head(d)
d.new <- d[,-c(3,13)]
d.new
cnames <- c(' Method','Similarity','C','CBC','BBC','E','EB','CC','NMI','ARI','VM') 
colnames(d.new) <- cnames
dim(d.new)
d.new
dim(d.new)

d.new

stargazer(d.new,summary = FALSE,column.sep.width='0pt',font.size='scriptsize',rownames=FALSE,colnames = TRUE)


stargazer(Summary_good_report[,-c(4,13)],summary = FALSE,column.sep.width='0pt',font.size='scriptsize',rownames=FALSE,colnames = TRUE)

