#--------------------------------------------------------------------------------
# Heatmap function
#--------------------------------------------------------------------------------

my.heatmap <- function( matrix, dendr = NA, dendc = NA, colors = "Reds", nco = 100, 
                        bparam = 9, margin = c(2,2), height = 600, width = 600,
                        scale = "none", rname = NULL, cname = NULL)
{
  rownames(matrix)  <- rev(rname)
  colnames(matrix)  <- rname
  new.matrix <- data.matrix(matrix)
  cols       <- colorRampPalette(brewer.pal(bparam,colors))(nco)
  heatmap    <- heatmap(new.matrix, Rowv=dendr, Colv=dendc, col = cols, scale="column", margins=margin,distfun=NULL)
  }


#--------------------------------------------------------------------------------
# 
#--------------------------------------------------------------------------------

line.plot <- function(){
  
  reds  <- colorRampPalette(brewer.pal(9,"Reds"))(ncoolor)
  blues <- colorRampPalette(brewer.pal(9,"Blues"))(ncoolor)
  diverging.colors <- c(reds,blues)
  
}

#--------------------------------------------------------------------------------
# 
#--------------------------------------------------------------------------------

json.unlist <- function(data){
  mat <- data[[1]]
  for( i in 2:length(data) ){
    mat <- rbind(mat,data[[i]])
  }
  rownames(mat) <- NULL
  colnames(mat) <- NULL
  return(mat)
}