#! /usr/bin/env python3.4
#
#$Author: ee364e07 $
#$Date: 2015-11-21 16:27:47 -0500 (Sat, 21 Nov 2015) $
#$HeadURL: svn+ssh://ece364sv@ecegrid/home/ecegrid/a/ece364sv/svn/F15/students/ee364e07/Lab11/MoreHomography.py $
#$Revision: 83499 $

import numpy as np
from Homography import *

class AdvancedTransformation(ColorTransformation):

    def __init__(self, sourceImage, v, h1, h2):
        super(ColorTransformation,self).__init__(sourceImage)

        if not isinstance(sourceImage,np.ndarray):
            raise TypeError("sourceImage must be an instance of ndarray")

        if (sourceImage.shape[1] % 2) is not 0:
            raise ValueError("sourceImage must have an even number of columns")

        if sourceImage.ndim is not 3:
            raise ValueError("sourceImage must be a color image(3d array)")

        if v < 0:
            raise ValueError("v must be greater than or equal to 0")

        if h1 < 0:
            raise ValueError("h1 must be greater than or equal to 0")

        if h2 < 0:
            raise ValueError("h2 must be greater than or equal to 0")


        self.trow, self.tcol, tdim = sourceImage.shape
        self.row = self.trow - 1
        self.column = (self.tcol/2) - 1

        #Split the source image into two
        self.si1 = sourceImage[:,0:self.tcol/2,:]
        self.si2 = sourceImage[:,self.tcol/2:,:]

        #Parameters for the A or V effect
        self.v = v
        self.h1 = h1
        self.h2 = h2

    def applyEffectV(self):

        #Set up the target points
        tp1 = [(0,0),(self.column-self.h2,self.v),(self.h1,self.row),(self.column,self.row+self.v)]
        tp2 = [(self.h2,self.v),(self.column,0),(0,self.row+self.v),(self.column-self.h1,self.row)]

        return self.computeEffect(tp1,tp2)

    def applyEffectA(self):

        #Set up the target points
        tp1 = [(self.h1,self.v),(self.column,0),(0,self.row+self.v),(self.column-self.h2,self.row)]
        tp2 = [(0,0),(self.column-self.h1,self.v),(self.h2,self.row),(self.column,self.row+self.v)]

        return self.computeEffect(tp1,tp2)

    def computeEffect(self, tp1, tp2):

        #Create new color transformation objects
        newAT1 = ColorTransformation(self.si1)
        newAT2 = ColorTransformation(self.si2)

        #Create the Homographies
        newAT1.setupTransformation(tp1)
        newAT2.setupTransformation(tp2)

        #Make the container images
        containerImage1 = np.ones([self.trow+self.v,self.tcol/2,3], dtype=np.uint8)*255
        containerImage2 = np.ones([self.trow+self.v,self.tcol/2,3], dtype=np.uint8)*255

        #Transform the images
        containerImage1 = newAT1.transformImage(containerImage1)
        containerImage2 = newAT2.transformImage(containerImage2)

        #Compute one final image
        containerFinal = np.hstack((containerImage1, containerImage2))

        return containerFinal

if __name__ == "__main__":
    targetImg = np.ones([10, 10, 3], dtype=np.uint8)
    bad = [[1,0],[0,2]]
    AT = AdvancedTransformation(targetImg,10,5,3)
