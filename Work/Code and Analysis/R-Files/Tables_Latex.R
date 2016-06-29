# ----------------------------------------------------------------------
# Packages
# ----------------------------------------------------------------------

library('stargazer')
setwd('~/Documents/GSE/Term 3/Master_Project/Master-Project/Work/Code and Analysis/Results/')
# ----------------------------------------------------------------------
# low alpha high mean
# ----------------------------------------------------------------------

df <- read.delim("~/Documents/GSE/Term 3/Master_Project/Master-Project/Work/Code and Analysis/Results/lthm.csv")
N <- nrow(df)
M <- ncol(df)
tab01 <- df[1:(N-1),1:M]
drops <- c('Data','Comment')
tab02 <- tab01[,!(names(tab01) %in% drops)]
stargazer(tab02,summary = FALSE,column.sep.width='0pt',font.size='tiny',rownames=FALSE)

# ----------------------------------------------------------------------
# med alpha high mean
# ----------------------------------------------------------------------

df <- read.delim("~/Documents/GSE/Term 3/Master_Project/Master-Project/Work/Code and Analysis/Results/mahm.csv")
N <- nrow(df)
M <- ncol(df)
tab01 <- df[1:(N-1),1:M]
drops <- c('Data','Comment')
tab02 <- tab01[,!(names(df) %in% drops)]
stargazer(tab02,summary = FALSE,column.sep.width='0pt',font.size='tiny',rownames=FALSE)

# ----------------------------------------------------------------------
# low  alpha low mean
# ----------------------------------------------------------------------

df <- read.delim("lalm.csv")
N <- nrow(df)
M <- ncol(df)
tab01 <- df[1:(N-1),1:M]
drops <- c('Data','Comment')
tab02 <- tab01[,!(names(tab01) %in% drops)]
stargazer(tab02,summary = FALSE,column.sep.width='0pt',font.size='scriptsize',rownames=FALSE)

# ----------------------------------------------------------------------
# mid alpha low mean
# ----------------------------------------------------------------------


df <- read.delim("malm.csv")
N <- nrow(df)
M <- ncol(df)
tab01 <- df[1:(N-1),1:M]
drops <- c('Data','Comment')
tab02 <- tab01[,!(names(tab01) %in% drops)]
stargazer(tab02,summary = FALSE,column.sep.width='0pt',font.size='scriptsize',rownames=FALSE)

# ----------------------------------------------------------------------
# low tau high mean
# ----------------------------------------------------------------------

df <- read.delim("lthm.csv")
N <- nrow(df)
M <- ncol(df)
tab01 <- df[1:(N-1),1:M]
drops <- c('Data','Comment')
tab02 <- tab01[,!(names(tab01) %in% drops)]
stargazer(tab02,summary = FALSE,column.sep.width='0pt',font.size='scriptsize',rownames=FALSE)

class(tab01)

df <- read.delim("mthm.csv")
N <- nrow(df)
M <- ncol(df)
tab01 <- df[1:(N-1),1:M]
drops <- c('Data','Comment')
tab02 <- tab01[,!(names(tab01) %in% drops)]
stargazer(tab02,summary = FALSE,column.sep.width='0pt',font.size='scriptsize',rownames=FALSE)


df <- read.delim("hthm.csv")
N <- nrow(df)
M <- ncol(df)
tab01 <- df[1:(N-1),1:M]
drops <- c('Data','Comment')
tab02 <- tab01[,!(names(tab01) %in% drops)]
stargazer(tab02,summary = FALSE,column.sep.width='0pt',font.size='scriptsize',rownames=FALSE)




