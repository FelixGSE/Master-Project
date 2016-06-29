
# ----
# Converting type of multiple variables in one go
# ----

# better solution is be careful how you import the data and specify it there

convertType <- function(obj, types) {
    for(i in 1:length(types)) { 
        if (types[i] == "num") { 
            if(is.factor(obj[,i])) {
                obj[,i] <- as.numeric(levels(obj[,i]))[obj[,i]]
            } else {
                obj[,i] <- as.numeric(obj[,i])
            }
        } else if (types[i] == "char") {
            obj[,i] <- as.character(obj[,i])
        } else if (types[i] == "fac") {
            obj[,i] <- as.factor(obj[,i])
        }
        
    }
    return(obj)
}

# ----
# rep for matrices
# ----

repmat = function(X, m, n) {
    mx = dim(X)[1]
    nx = dim(X)[2]
    matrix(t(matrix(X,mx,nx*n)),mx*m,nx*n,byrow=T)
} 

repRow<-function(x, n){
   matrix(rep(x, each=n),nrow=n)
}

repCol<-function(x, n){
   matrix(rep(x, each=n), ncol=n, byrow=TRUE)
}

# ----
# Sum of rows/columns, accepting both matrix AND vector
# ----

rowSum <- function(data, ...) {
    # data has to be either vector OR matrix/data frame
    if(is.vector(data)) {
        rowSum <- sum(data, ...)
    } else {
        rowSum <- apply(data,1,sum, ...)
    }
    return(rowSum)
}

colSum <- function(data, ...) {
    # data has to be either vector OR matrix/data frame
    if(is.vector(data)) {
        colSum <- sum(data, ...)
    } else {
        colSum <- apply(data,2,sum, ...)
    }
    return(colSum)
}




# ----
# Max of rows/columns, accepting both matrix AND vector
# ----

rowMax <- function(data, ...) {
    # data has to be either vector OR matrix/data frame
    if(is.vector(data)) {
        rowMax <- max(data, ...)
    } else {
        rowMax <- apply(data,1,max, ...)
    }
    return(rowMax)
}

colMax <- function(data, ...) {
    # data has to be either vector OR matrix/data frame
    if(is.vector(data)) {
        colMax <- max(data, ...)
    } else {
        colMax <- apply(data,2,max, ...)
    }
    return(colMax)
}


# ----
# Count of rows/columns, accepting both matrix AND vector
# ----

nrows <- function(data) {
    # data has to be either vector OR matrix/data frame
    if(is.vector(data)) {
        nrows <- 1
    } else {
        nrows <- dim(data)[1]
    }
    return(nrows)
}

ncols <- function(data) {
    # data has to be either vector OR matrix/data frame
    if(is.vector(data)) {
        ncols <- length(data)
    } else {
        ncols <- dim(data)[2]
    }
    return(ncols)
}

# ----
# Simple matrix wrapper for random numbers
# ----

rmat <- function(distribution, ncol, nrow, byrow=TRUE, ...) {
    matrix(distribution(ncol*nrow,...), ncol=ncol, nrow=nrow, byrow=byrow)
}


# ----
# Improved list of objects, sorted, with memory
# ----

# taken from:
# http://stackoverflow.com/questions/1358003/tricks-to-manage-the-available-memory-in-an-r-session
.ls.objects <- function (pos = 1, pattern, order.by,
                        decreasing=FALSE, head=FALSE, n=5) {
    napply <- function(names, fn) sapply(names, function(x)
                                         fn(get(x, pos = pos)))
    names <- ls(pos = pos, pattern = pattern)
    obj.class <- napply(names, function(x) as.character(class(x))[1])
    obj.mode <- napply(names, mode)
    obj.type <- ifelse(is.na(obj.class), obj.mode, obj.class)
    obj.prettysize <- napply(names, function(x) {
                           capture.output(print(object.size(x), units = "auto")) })
    obj.size <- napply(names, object.size)
    obj.dim <- t(napply(names, function(x)
                        as.numeric(dim(x))[1:2]))
    vec <- is.na(obj.dim)[, 1] & (obj.type != "function")
    obj.dim[vec, 1] <- napply(names, length)[vec]
    out <- data.frame(obj.type, obj.size, obj.prettysize, obj.dim)
    names(out) <- c("Type", "Size", "PrettySize", "Rows", "Columns")
    if (!missing(order.by))
        out <- out[order(out[[order.by]], decreasing=decreasing), ]
    if (head)
        out <- head(out, n)
    out
}

# shorthand
lsos <- function(..., n=10) {
    .ls.objects(..., order.by="Size", decreasing=TRUE, head=TRUE, n=n)
}




# ----
# Insert a row in a data frame
# ----

insertRow <- function(existingDF, newrow, r) {
  existingDF[seq(r+1,nrow(existingDF)+1),] <- existingDF[seq(r,nrow(existingDF)),]
  existingDF[r,] <- newrow
  existingDF
}


# ----
# From knitr to docx using Pandoc
# ----


knitsDoc <- function(name) {
  library(markdown)
  library(knitr)
  bib<-paste0("~/Dropbox/Research/library.bib")   # bibtex file, from Mendeley
  csl<-paste0("~/Dropbox/Research/apa.csl")  # reference list format
  knit(paste0(name, ".Rmd"), encoding = "utf-8")
  system(paste0("pandoc -S -c custom.css -o ", name, ".html ", name, ".md --bibliography ",bib," --csl ",csl," --self-contained"))
  system(paste0("pandoc -S -o ", name, ".docx ", name, ".html"))
}


#
# Tic/Toc functions for measuring running time (a la Matlab)
#

tic <- function(gcFirst = TRUE, type=c("elapsed", "user.self", "sys.self"))
{
   type <- match.arg(type)
   assign(".type", type, envir=baseenv())
   if(gcFirst) gc(FALSE)
   tic <- proc.time()[type]
   assign(".tic", tic, envir=baseenv())
   invisible(tic)
}

toc <- function()
{
   type <- get(".type", envir=baseenv())
   toc <- proc.time()[type]
   tic <- get(".tic", envir=baseenv())
   print(toc - tic)
   invisible(toc)
}


#
# Normalizing a vector of data
#

# x = v - min/ max - min
# max = 1 and min = 0.

normalize <- function(x) { (x - min(x, na.rm=TRUE))/(max(x,na.rm=TRUE) - min(x, na.rm=TRUE))}

#
# rbind for many matrices/data frames
#
rbind.many <- function(ls) {
  # input comes in a form of list AND it assumes that each matrix/data frame has
  # the same number of columns
  env <- rbind(ls[[1]], ls[[2]])
  for (i in 3:length(ls)) {env <- rbind(env, ls[[i]])}
  env
}

#
# appending a new list element in an existing list
#
push <- function(lst, obj) {
  lst[[length(lst)+1]] <- obj
  return(lst)
}


#
# Function: tslag (lagging a vector)
#
tslag <- function(x, d=1)
  {
    x <- as.vector(x)
    n <- length(x)
    c(rep(NA,d),x)[1:n]
  }

