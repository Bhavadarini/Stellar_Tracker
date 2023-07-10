import numpy as np
from astropy.io import fits
import matplotlib.pyplot as plt
import numpy as np
from photutils.centroids import centroid_2dg

# function to return centroid and FWHM from numpy array
def star_centroids(data):
     # Insert code for finding centroid and FWHM
    centroids=[[],[]] #x and y coordinates of the centroids of stars in the image
    FWHM=0 # Full width Half maximum, the radius around centroid at which intensity roughly halves
    centroids=centroid_2dg(data) #calculates the centroid by fitting a 2D Gaussian to the 2D distribution of the data
   
    return (centroids,FWHM)

# displaying the location of stars
filename="M-31Andromed220221022931.FITS" # this is an exaple file
with fits.open(filename) as hdul: # returns a list of header-data-units 
    data=hdul[0].data # a header-data-unit object has a string(header) and a numpy array(image data)
    centroids,FWHM=star_centroids(data) 
    plt.scatter(centroids[0],centroids[1]) # scatter plot showing location of stars
    plt.show()
