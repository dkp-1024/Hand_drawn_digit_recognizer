library(raster)
color.image <- brick("in.jpg")
color.values <- getValues(color.image)
bw.values <- color.values[,1]*0.21 + color.values[,1]*0.72 + color.values[,1]*0.07