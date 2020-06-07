# -*- coding: utf-8 -*-
"""
Created on Sat Oct 12 03:38:28 2019

@author: cosmi

Working Batch Processer for DNG to JPG

rawpy is an easy-to-use Python wrapper for the LibRaw library. 
rawpy works natively with numpy arrays and supports a lot of options, 
including direct access to the unprocessed Bayer data
It also contains some extra functionality for finding and repairing hot/dead pixels.
import rawpy.enhance for this


"""

import os
import rawpy
import imageio

## Image Processing libraries for histogram equalisation
from skimage import exposure


for infile in os.listdir("./"):
    print( "file : " + infile)
    if infile[-3:] == "tif" or infile[-3:] == "DNG" :
       # print "is tif or DNG (RAW)"
       outfile = infile[:-3] + "jpg"
       raw = rawpy.imread(infile)
       print( "new filename : " + outfile)
       

       # Postprocessing, i.e demosaicing here, will always 
       #change the original pixel values. Typically what you want
       # is to get a linearly postprocessed image so that roughly 
       #the number of photons are in linear relation to the pixel values. 
       #You can do that with:

       rgb = raw.postprocess()

       #Apply gamma corrections: gamma values greater than 1 will shift the image histogram towards left and the output image will be darker than the input image. On the other hand, for gamma values less than 1, the histogram will shift towards right and the output image will be brighter than the input image.
    

       gamma_corrected_image = exposure.adjust_gamma(rgb, gamma=1, gain=0.5)

       
       image=gamma_corrected_image
       
       #apply histogram equalization
       #using skimage (easy way)
       hist_equalized_image = exposure.equalize_hist(image)
    

       imageio.imsave(outfile, hist_equalized_image)
