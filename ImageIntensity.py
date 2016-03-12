__author__ = 'anna'

import skimage
import skimage.io
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

mod = 2**16

# function to calculate intensities for each rectangle from point(0,0) to point(i,j)
def setTableOfIntensities(image):

    # representation of picture like 2D array, where it is set the intensity for each pixel
    image_normalisation = skimage.img_as_ubyte(image)

    # array for intensities of rectangles
    intensities = np.zeros(image.shape)

    intensities[0][0]=image_normalisation[0][0]

    # set the first column for intensities array
    for i in range (1,image.shape[0]):
        intensities[i][0]=(image_normalisation[i][0]+intensities[i-1][0]) % mod

    # set the first raw for intensities array
    for j in range (1,image.shape[1]):
        intensities[0][j]=(image_normalisation[0][j]+intensities[0][j-1]) % mod

    for i in range(1,image.shape[0]):
        for j in range(1,image.shape[1]):
            intensities[i][j]= (image_normalisation[i][j]+intensities[i][j-1]+intensities[i-1][j]-intensities[i-1][j-1]) % mod

    return intensities

# function to find the m*m square of the image, where the total intensity has the biggest value
def findMaxIntSquare(m, intensities, image):

    # In each position (i,j) of intensitiesOfSquares array the total intensity of m*m_square_array is set.
    # index (i,j) is the index of top right corner of m*m_square_array
    intensitiesOfSquares = np.zeros(image.shape)

    intensitiesOfSquares[m-1][m-1]=intensities[m-1][m-1]

    for i in range (m,image.shape[0]):
        intensitiesOfSquares[i][m-1]=(intensities[i][m-1]-intensities[i-m][m-1])% mod

    for j in range(m,image.shape[1]):
        intensitiesOfSquares[m-1][j]= (intensities[m-1][j]-intensities[m-1][j-m])% mod

    for i in range(m,image.shape[0]):
        for j in range(m,image.shape[1]):
            intensitiesOfSquares[i][j]=(intensities[i][j]-intensities[i-m][j]-intensities[i][j-m]+intensities[i-m][j-m])%mod

    i,j = np.unravel_index(intensitiesOfSquares.argmax(), intensitiesOfSquares.shape)

    #return the biggest value of total intensities in m*m_square
    return intensitiesOfSquares[i][j]

def main():

    image = skimage.io.imread('/home/anna/IdeaProjects/ImageIntensity/parrots.jpg', as_grey=True)
    # plt.imshow(image)
    # plt.show()
    intensities = setTableOfIntensities(image)
    maxInten = findMaxIntSquare(16,intensities,image)
    print maxInten



if __name__ == '__main__':
    main()
