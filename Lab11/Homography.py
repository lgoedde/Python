#! /usr/bin/env python3.4
#
#$Author: ee364e07 $
#$Date: 2015-12-02 13:44:22 -0500 (Wed, 02 Dec 2015) $
#$HeadURL: svn+ssh://ece364sv@ecegrid/home/ecegrid/a/ece364sv/svn/F15/students/ee364e07/Lab11/Homography.py $
#$Revision: 83607 $

import numpy as np
from enum import Enum
from scipy.interpolate import RectBivariateSpline as rbs
from scipy.misc import toimage, imread
from scipy.interpolate import interp2d as i2d
import scipy

class Effect(Enum):
    rotate90 = 1
    rotate180 = 2
    rotate270 = 3
    flipHorizontally = 4
    flipVertically = 5
    transpose = 6

class Homography:

    def __init__(self, **kwargs):
        if len(kwargs) < 1 and len(kwargs) > 4:
            raise ValueError("Please give only the homography matrix, sourcePoints, and targetPoints as an argument.")
        checkS = False
        checkT = False
        checkH = False
        self.effect = None
        for key in kwargs:
            #Do all of the error testing to make sure we have the correct input and a 3x3 matrix
            if key == 'homographyMatrix':
                temp = kwargs['homographyMatrix']
                if len(temp) != 3:
                    raise ValueError("\'homographyMatrix\' must contain exactly three lists")
                for item in temp:
                    if len(item) != 3:
                        raise ValueError('Each list in \'homographyMatrix\' must contain exactly 3 values')
                    for num in item:
                        if type(num) != float:
                            raise ValueError("Please only enter float values for \'homographyMatrix\'")

                #If none of these errors are raised, then we have a good homography matrix to use
                self.hMatrix = temp
                checkH = True

            if key == 'sourcePoints':
                temp = kwargs['sourcePoints']
                if len(temp) != 4:
                    raise ValueError('"sourcePoints" must be a list with exactly 4 elements')
                for item in temp:
                    if len(item) != 2:
                        raise ValueError('"sourcePoints must be a list of 4 point tuples')
                self.sourcePoints = temp
                checkS = True

            if key == 'targetPoints':
                temp = kwargs['targetPoints']
                if len(temp) != 4:
                    raise ValueError('"targetPoints" must be a list with exactly 4 elements')
                for item in temp:
                    if len(item) != 2:
                        raise ValueError('"targetPoints" must be a list of 4 point tuples')
                self.targetPoints = temp
                checkT = True

            if key == 'effect':
                temp = kwargs['effect']
                if temp is not None:
                    if type(temp) != Effect:
                        raise TypeError("Please only give an effect enum for 'effect' argument")
                self.effect = temp


        if checkH:
            checkS = False
            checkT = False

        elif checkT and checkS:
            self.hMatrix = self.computeHomography(self.sourcePoints,self.targetPoints, self.effect)

        else:
            raise ValueError('If homographyMatrix is not given, then both sourcePoints and targetPoints must be given together')

    def computeHomography(self,sourcePoints, targetPoints, effect):

        sourcePoints = self.computeRotation(sourcePoints,effect)

        fullA = []
        fullB = []
        for ind,point in enumerate(sourcePoints):
            fullA.append([point[0],point[1],1,0,0,0,-targetPoints[ind][0]*point[0], -targetPoints[ind][0]*point[1]])
            fullA.append([0,0,0,point[0],point[1],1,-targetPoints[ind][1]*point[0], -targetPoints[ind][1]*point[1]])

            fullB.append([targetPoints[ind][0]])
            fullB.append([targetPoints[ind][1]])


        h = np.linalg.solve(fullA,fullB)
        newh = []

        newh.append([h[0][0],h[1][0],h[2][0]])
        newh.append([h[3][0],h[4][0],h[5][0]])
        newh.append([h[6][0],h[7][0],1.0])

        return newh


    def forwardProject(self, point):
        if len(point) != 2:
            raise ValueError("Please give one tuple containing an x and y value")

        point = self.managePoint(point)
        #The actual calculations for the homography projection
        h = np.dot(self.hMatrix,point)
        h /= h[2]

        #print(h)
        return round(h[0],2), round(h[1],2)

    def inverseProject(self, pointPrime):
        if len(pointPrime) != 2:
            raise ValueError("Please give one tuple containing an x and y value")

        pointPrime = self.managePoint(pointPrime)

        #Inverse the homography matrix
        invH = np.linalg.inv(self.hMatrix)

        #Do the inverse Homography math
        h = np.dot(invH,pointPrime)
        h /= h[2]


        return round(h[0],2), round(h[1],2)

    def managePoint(self,point):
        #Make the point a list then add 1 to get it to a 3x1
        point = list(point)
        point.append(1.0)

        #In order to transpose the matrix, it must be of type ndarry
        array = np.asarray(point)
        point = array.transpose()

        return point

    def computeRotation(self,sourcePoints, effect):

        if effect == Effect.rotate90:
            sourcePoints = [sourcePoints[2],sourcePoints[0],sourcePoints[3],sourcePoints[1]]
        if effect == Effect.rotate180:
            sourcePoints = [sourcePoints[3],sourcePoints[2],sourcePoints[1],sourcePoints[0]]
        if effect == Effect.rotate270:
            sourcePoints = [sourcePoints[1],sourcePoints[3],sourcePoints[0],sourcePoints[2]]
        if effect == Effect.flipHorizontally:
            sourcePoints = [sourcePoints[2],sourcePoints[3],sourcePoints[0],sourcePoints[1]]
        if effect == Effect.flipVertically:
            sourcePoints = [sourcePoints[1],sourcePoints[0],sourcePoints[3],sourcePoints[2]]
        if effect == Effect.transpose:
            sourcePoints = [sourcePoints[0],sourcePoints[2],sourcePoints[1],sourcePoints[3]]
        if effect == None:
            sourcePoints = sourcePoints

        return sourcePoints

class Transformation:

    def __init__(self, sourceImage, homography=None):
        if type(sourceImage) != np.ndarray:
            raise TypeError('Please give a sourceImage that is of the type "ndarray"')
        self.sourceImage = sourceImage

        if homography is not None:
            if type(homography) != Homography:
                raise TypeError('Please give an object that is of the type Homography')
        self.homography = homography


    def setupTransformation(self, targetPoints, effect=None):
        if len(targetPoints) != 4:
            raise ValueError('\'targetPoints\' must be a list of exactly 4 tuples')

        self.minpt, self.maxpt = self.computeBoundingBox(targetPoints)

        if self.sourceImage.ndim == 2:
            self.row, self.column = self.sourceImage.shape
        if self.sourceImage.ndim == 3:
            self.row, self.column, self.dim = self.sourceImage.shape

        sourcePoints = [(0,0),(self.column-1,0),(0,self.row-1),(self.column-1,self.row-1)]

        if self.homography == None:

            self.homography = Homography(sourcePoints=sourcePoints, targetPoints=targetPoints, effect=effect)

    def computeBoundingBox(self,targetPoints):
        minpt = list(max(targetPoints))
        maxpt = list(min(targetPoints))

        for x, y in targetPoints:
            if x < minpt[0]:
                minpt[0] = int(x)

            if x > maxpt[0]:
                maxpt[0] =  int(x)

            if y < minpt[1]:
                minpt[1] = int(y)

            if y > maxpt[1]:
                maxpt[1] = int(y)

        return minpt,maxpt


    def transformImage(self, containerImage):
        if type(containerImage) != np.ndarray:
            raise TypeError('Please give a containerImage that is of type "ndarray"')
        if containerImage.ndim != 2:
            raise ValueError('Please give a containerImage that is 2 dimensions')

        #toimage(containerImage).show()
        #setting up the spline

        fx = rbs(range(0,self.row), range(0,self.column), self.sourceImage, kx=1, ky=1)
        #print(list(range(self.minpt[0], self.maxpt[0]+1)))
        #print(range(self.minpt[1],self.maxpt[1]+1))
        self.minpt = [int(x) for x in self.minpt]
        self.maxpt = [int(x) for x in self.maxpt]

        """print(len(containerImage), len(containerImage[0]))
        print(range(self.minpt[0], self.maxpt[0]+1))
        print(range(self.minpt[1], self.maxpt[1]+1))"""

        for invX in range(0, containerImage.shape[0]):
            for invY in range(0,containerImage.shape[1]):
                x, y = self.homography.inverseProject((invY,invX))
                if x >=0 and x <= self.column-1 and y >= 0 and y <= self.row-1:
                    pixelData = fx(y,x)
                    containerImage[invX, invY] = pixelData

        #toimage(containerImage).show()
        return containerImage

class ColorTransformation(Transformation):

    def __init__(self, sourceImage, homography=None):
        super(ColorTransformation,self).__init__(sourceImage,homography)

       # if sourceImage.ndim != 3:
        #    raise ValueError("Please enter a sourceImage that is 3 dimensions(color)")


    def transformImage(self, containerImage):
        if type(containerImage) != np.ndarray:
            raise TypeError('Please give a containerImage that is of type "ndarray"')
        if len(containerImage.shape) != 3:
            raise ValueError('Please give a containerImage that is 2 dimensions')


        #toimage(containerImage).show()
        #setting up the spline

        blue = rbs(range(0,self.row), range(0,self.column), self.sourceImage[:,:,0], kx=1, ky=1)
        red = rbs(range(0,self.row), range(0,self.column), self.sourceImage[:,:,1], kx=1, ky=1)
        green = rbs(range(0,self.row), range(0,self.column), self.sourceImage[:,:,2], kx=1, ky=1)

        #print(list(range(self.minpt[0], self.maxpt[0]+1)))
        #print(range(self.minpt[1],self.maxpt[1]+1))
        self.minpt = [int(x) for x in self.minpt]
        self.maxpt = [int(x) for x in self.maxpt]

        """print(len(containerImage), len(containerImage[0]))
        print(range(self.minpt[0], self.maxpt[0]+1))
        print(range(self.minpt[1], self.maxpt[1]+1))"""

        for invX in range(0, containerImage.shape[0]):
            for invY in range(0,containerImage.shape[1]):
                x, y = self.homography.inverseProject((invY,invX))
                if x >=0 and x <= self.column-1 and y >= 0 and y <= self.row-1:
                    pdBlue = blue(y,x)
                    pdRed = red(y,x)
                    pdGreen = green(y,x)
                    containerImage[invX, invY, 0] = pdBlue
                    containerImage[invX, invY, 1] = pdRed
                    containerImage[invX, invY, 2] = pdGreen

        #toimage(containerImage).show()
        return containerImage

if __name__ == "__main__":
    matrix = [[1.0,1.7,4.3],[2.7,2.0,8.4],[3.1,0.9,4.6]]
    myH = Homography(homographyMatrix=matrix,effect=Effect.rotate90)
    point = myH.forwardProject((1.0,2.0))
    newpoint = myH.inverseProject(point)
    targetImg = np.ones([10, 10, 3], dtype=np.uint8)
    img = np.ndarray(shape=(4,4))
    myT = Transformation(img,myH)

    newH = Homography(sourcePoints=[(1,2),(3,4),(5,6),(7,8)],targetPoints=[(9,10),(11,12),(13,14),(15,16)],effect=Effect.rotate90)
    myT.setupTransformation(targetPoints=[(1,1),(1,2),(3,4),(5,2)])

    t = Transformation(imread('TestImages/GrayNature.png'))
    frontPoints = [(159.0, 136.0), (345.0, 85.0), (160.0, 276.0), (309.0, 216.0)]
    t.setupTransformation(frontPoints)
    t.transformImage(imread('TestImages/WhiteSmall.png'))



