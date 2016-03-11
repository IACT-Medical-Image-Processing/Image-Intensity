__author__ = 'anna'

import skimage
import skimage.io
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

def setTableOfIntensities(image):

    image_normalisation = skimage.img_as_ubyte(image)

    intensities = np.zeros(image.shape)

    intensities[0][0]=image_normalisation[0][0]

    for i in range (1,image.shape[0]):
        intensities[i][0]=image_normalisation[i][0]+intensities[i-1][0]

    for j in range (1,image.shape[1]):
        intensities[0][j]=image_normalisation[0][j]+intensities[0][j-1]

    for i in range(1,image.shape[0]):
        for j in range(1,image.shape[1]):
            intensities[i][j]= image_normalisation[i][j]+intensities[i][j-1]+intensities[i-1][j]-intensities[i-1][j-1]

    return intensities

def findMaxIntSquare(m, intensities, image):

    intensitiesOfSquares = np.zeros(image.shape)

    intensitiesOfSquares[m-1][m-1]=intensities[m-1][m-1]

    for i in range (m,image.shape[0]):
        intensitiesOfSquares[i][m-1]=intensities[i][m-1]-intensities[i-m][m-1]

    for j in range(m,image.shape[1]):
        intensitiesOfSquares[m-1][j]=intensities[m-1][j]-intensities[m-1][j-m]

    for i in range(m,image.shape[0]):
        for j in range(m,image.shape[1]):
            intensitiesOfSquares[i][j]=intensities[i][j]-intensities[i-m][j]-intensities[i][j-m]+intensities[i-m][j-m]

    i,j = np.unravel_index(intensitiesOfSquares.argmax(), intensitiesOfSquares.shape)

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
