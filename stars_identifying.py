import numpy as np
from astropy.io import fits
import matplotlib.pyplot as plt
import numpy as np

# function to return centroid and FWHM from numpy array
def star_centroids(data):
    centroids=[[],[]]
    FWHM=0
    return (centroids,FWHM)

# displaying the location of stars
filename="M-31Andromed220221022931.FITS"
with fits.open(filename) as hdul:
    data=hdul[0].data
    centroids,FWHM=star_centroids(data)
    plt.scatter(centroids[0],centroids[1],s=np.pi*FWHM*FWHM,c='tab:blue')
    plt.show()
