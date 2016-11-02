setwd('/Users/felix/Documents/GSE/Term 3/External Data/hrvoje/')

age       <- read.table('hrvoje_multiarm_age.csv',header = TRUE)[,1]
education <- read.table('hrvoje_multiarm_education.csv',header = TRUE)[,1]
gender    <- read.table('hrvoje_multiarm_gender.csv',header = TRUE)[,1]

# Summary
round(mean(age),2)
round(sd(age),2)
table(education)
table(gender)

length(age)
length(education)
length(gender)
