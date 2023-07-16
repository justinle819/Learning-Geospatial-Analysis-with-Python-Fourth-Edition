"""Swap bands in a raster satellite image"""

# https://github.com/PacktPublishing/Learning-Geospatial-Analysis-with-Python-4th-Edition/raw/main/B19730_06_Asset_Files/FalseColor.zip

from osgeo import gdal_array

# name of our source image
src = "FalseColor.tif"

# load the source image into an array
arr = gdal_array.LoadFile(src)

# swap bands 1 and 2 for a natural color image.
# We will use numpy "advanced slicing" to reorder the bands.
# Using the source image
output = gdal_array.SaveArray(arr[[1, 0, 2], :], "swap.tif",
                      format="GTiff", prototype=src)
# Dereference output to avoid corrupted file on some platforms
output = None