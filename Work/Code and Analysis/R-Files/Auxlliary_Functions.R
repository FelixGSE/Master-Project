#--------------------------------------------------------------------------------
# Heatmap function
#--------------------------------------------------------------------------------

my.heatmap <- function( matrix, dendr = NA, dendc = NA, colors = "Reds", nco = 100, 
                        bparam = 9, margin = c(2,2), height = 600, width = 600,
                        scale = "none", rname = NULL, cname = NULL, save = FALSE, 
                        plotname = "plot.png" )
{
  row.names(matrix) <- cname
  colnames(matrix)  <- cname
  new.matrix <- data.matrix(matrix)
  cols       <- colorRampPalette(brewer.pal(bparam,colors))(nco)
  heatmap    <- heatmap(new.matrix, Rowv=dendr, Colv=dendc, col = cols, scale="column", margins=margin,distfun=NULL)
  if( save == TRUE){
    png(plotname, height = height, width = width )
    heatmap(new.matrix, Rowv=dendr, Colv=dendc, col = cols,margins=margin, scale="column",distfun=NULL)
  dev.off()
  }
}

#--------------------------------------------------------------------------------
# 
#--------------------------------------------------------------------------------
