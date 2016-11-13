#! /usr/bin/env python3.4
#
#$Author: ee364e07 $
#$Date: 2015-12-02 19:36:50 -0500 (Wed, 02 Dec 2015) $
#$HeadURL: svn+ssh://ece364sv@ecegrid/home/ecegrid/a/ece364sv/svn/F15/students/ee364e07/Lab11/HomographyApp.py $
#$Revision: 83612 $

import sys
from PySide.QtGui import *
from PySide.QtCore import *
from HomographyGUI import *
from Homography import *
from scipy.misc import toimage, imread, imsave
import os
import copy

class HomographyApp(QMainWindow, Ui_MainWindow):

    def __init__(self, parent=None):

        super(HomographyApp, self).__init__(parent)
        self.setupUi(self)
        initialBtns = [self.viewSource, self.viewTarget, self.acquirePts, self.point1, self.point2, self.point3, self.point4,
                       self.effectBox, self.transform, self.reset, self.save, self.elabel, self.acquireSpts, self.spoint1, self.spoint2]

        self.currPt = 1
        self.currSpt = 1
        self.tFlag = False
        self.rFlag = False
        self.tempPts = []
        self.tempSpts = []
        self.scene = None
        self.sscene = None
        for btn in initialBtns:
            btn.setEnabled(False)

        self.loadSource.clicked.connect(self.openSource)
        self.loadTarget.clicked.connect(self.openTarget)
        self.acquirePts.clicked.connect(self.getPts)
        self.acquireSpts.clicked.connect(self.getSpts)
        self.save.clicked.connect(self.saveFile)
        self.reset.clicked.connect(self.resetScreen)
        self.transform.clicked.connect(self.doTransform)

    def openSource(self):
        self.viewSource.setEnabled(True)
        """
        Obtain a file name from a file dialog, and pass it on to the loading method. This is to facilitate automated
        testing. Invoke this method when clicking on the 'load' button.

        *** DO NOT MODIFY THIS METHOD, OR THE TEST WILL NOT PASS! ***
        """
        filePath, _ = QFileDialog.getOpenFileName(self, caption='Open source image file ...', filter="PNG files (*.png)")

        if not filePath:
            return

        self.sourceImage = imread(filePath)

        pixmap = QPixmap(filePath)
        self.sview = QGraphicsPixmapItem()
        self.sscene = QGraphicsScene()

        self.sview.setPixmap(pixmap)
        self.sscene.addItem(self.sview)

        self.viewSource.setScene(self.sscene)
        self.viewSource.fitInView(self.sscene.sceneRect(), Qt.KeepAspectRatio)
        self.viewSource.show()

        self.hasPoints = False

        if self.viewTarget.isEnabled():
            self.loadedState()

        if self.tFlag:
            self.resetScreen()
            self.loadedState()

        # self.sourceReset()
        #
        # if not self.rFlag:
        #     self.enablePts()

    def openTarget(self):
        self.viewTarget.setEnabled(True)
        """
        Obtain a file name from a file dialog, and pass it on to the loading method. This is to facilitate automated
        testing. Invoke this method when clicking on the 'load' button.

        *** DO NOT MODIFY THIS METHOD, OR THE TEST WILL NOT PASS! ***
        """
        filePath, _ = QFileDialog.getOpenFileName(self, caption='Open target image file ...', filter="PNG files (*.png)")

        if not filePath:
            return

        self.targetImage = imread(filePath)
        self.pixmap = QPixmap(filePath)
        self.view = QGraphicsPixmapItem()
        self.scene = QGraphicsScene()

        self.view.setPixmap(self.pixmap)
        self.scene.addItem(self.view)

        self.viewTarget.setScene(self.scene)
        self.viewTarget.fitInView(self.scene.sceneRect(), Qt.KeepAspectRatio)
        self.viewTarget.show()

        self.rFlag = False

        if self.viewSource.isEnabled():
            self.loadedState()

    def loadedState(self):
        if self.sscene:
            if self.sscene.changed:
                if not self.hasPoints:
                    self.acquireSpts.setEnabled(True)
                    self.spoint1.setEnabled(True)
                    self.spoint2.setEnabled(True)
                    self.currSpt = 1
                    self.tempSpts = []
                    self.sourcePts = None
                    self.spoint1.setText('')
                    self.spoint2.setText('')

                if self.tFlag:
                    self.acquirePts.setEnabled(True)
                    self.point1.setEnabled(True)
                    self.point2.setEnabled(True)
                    self.point3.setEnabled(True)
                    self.point4.setEnabled(True)

                    self.currPt = 1
                    self.tempPts = []
                    self.targetPts = []
                    self.point1.setText('')
                    self.point2.setText('')
                    self.point3.setText('')
                    self.point4.setText('')

                    self.elabel.setEnabled(False)
                    self.effectBox.setEnabled(False)
                    self.transform.setEnabled(False)
                    self.reset.setEnabled(False)
                    self.save.setEnabled(False)

        if self.scene:
            if self.scene.changed:
                if not self.rFlag:
                    self.acquirePts.setEnabled(True)
                    self.point1.setEnabled(True)
                    self.point2.setEnabled(True)
                    self.point3.setEnabled(True)
                    self.point4.setEnabled(True)

                    self.currPt = 1
                    self.tempPts = []
                    self.targetPts = []
                    self.point1.setText('')
                    self.point2.setText('')
                    self.point3.setText('')
                    self.point4.setText('')

                    self.elabel.setEnabled(False)
                    self.effectBox.setEnabled(False)
                    self.transform.setEnabled(False)
                    self.reset.setEnabled(False)
                    self.save.setEnabled(False)

    def getSpts(self):
        self.loadSource.setEnabled(False)
        self.loadTarget.setEnabled(False)
        self.acquirePts.setChecked(False)
        # self.elabel.setEnabled(False)
        # self.effectBox.setEnabled(False)
        # self.transform.setEnabled(False)
        # self.reset.setEnabled(False)
        # self.save.setEnabled(False)

        self.sview.mousePressEvent = self.spointSelect
        self.keyPressEvent = self.delSpt


        if not self.acquireSpts.isChecked():
            self.loadSource.setEnabled(True)
            self.loadTarget.setEnabled(True)

            if self.currSpt < 3:
                self.loadedState()

            if self.currSpt >= 3:
                if len(self.tempSpts) == 2:
                    self.sourcePts = self.tempSpts
                    self.hasPoints = True

    def getPts(self):
        self.loadSource.setEnabled(False)
        self.loadTarget.setEnabled(False)
        self.acquireSpts.setChecked(False)
        self.elabel.setEnabled(False)
        self.effectBox.setEnabled(False)
        self.transform.setEnabled(False)
        self.reset.setEnabled(False)
        self.save.setEnabled(False)

        self.view.mousePressEvent = self.pointSelect
        self.keyPressEvent = self.delPt

        if not self.acquirePts.isChecked():
            self.loadSource.setEnabled(True)
            self.loadTarget.setEnabled(True)

            if self.currPt < 5:
                self.loadedState()

            if self.currPt >= 5:
                if len(self.tempPts) == 4:
                    self.targetPts = self.tempPts
                    self.readyState()

    def readyState(self):
        self.elabel.setEnabled(True)
        self.effectBox.setEnabled(True)
        self.transform.setEnabled(True)
        self.reset.setEnabled(True)
        self.save.setEnabled(True)
        self.rFlag= True

    def pointSelect(self, event):

        if self.acquirePts.isChecked():
            if event.button() == Qt.LeftButton:
                if self.currPt < 5:
                    point = event.pos()
                    x = float(round(point.x()))
                    y = float(round(point.y()))
                    tempt = (x,y)
                    if self.currPt == 1:
                        self.point1.setText('{}, {}'.format(x,y))
                        self.tempPts.append(tempt)
                    elif self.currPt == 2:
                        self.point2.setText('{}, {}'.format(x,y))
                        self.tempPts.append(tempt)
                    elif self.currPt == 3:
                        self.point3.setText('{}, {}'.format(x,y))
                        self.tempPts.append(tempt)
                    elif self.currPt == 4:
                        self.point4.setText('{}, {}'.format(x,y))
                        self.tempPts.append(tempt)

                    self.currPt += 1

    def spointSelect(self, event):

        if self.acquireSpts.isChecked():
            if event.button() == Qt.LeftButton:
                if self.currSpt < 3:
                    point = event.pos()
                    x = float(round(point.x()))
                    y = float(round(point.y()))
                    tempt = (x,y)
                    if self.currSpt == 1:
                        self.spoint1.setText('{}, {}'.format(x,y))
                        self.tempSpts.append(tempt)
                    elif self.currSpt == 2:
                        self.spoint2.setText('{}, {}'.format(x,y))
                        self.tempSpts.append(tempt)

                    self.currSpt += 1

    def delPt(self, event):
        if self.acquirePts.isChecked():
            if event.key() == Qt.Key_Backspace:
                if self.currPt > 1:
                    self.currPt -= 1

                    if self.currPt == 1:
                        self.point1.setText('')
                        del self.tempPts[0]
                    elif self.currPt == 2:
                        self.point2.setText('')
                        del self.tempPts[1]
                    elif self.currPt == 3:
                        self.point3.setText('')
                        del self.tempPts[2]
                    elif self.currPt == 4:
                        self.point4.setText('')
                        del self.tempPts[3]

    def delSpt(self, event):
        if self.acquireSpts.isChecked():
            if event.key() == Qt.Key_Backspace:
                if self.currSpt > 1:
                    self.currSpt -= 1

                    if self.currSpt == 1:
                        self.spoint1.setText('')
                        del self.tempSpts[0]
                    elif self.currSpt == 2:
                        self.spoint2.setText('')
                        del self.tempSpts[1]

    def saveFile(self):

        filePath, _ = QFileDialog.getSaveFileName(self, caption='Name of file for new target image...', filter="PNG files (*.png)")

        if not filePath:
            return

        self.savePath = filePath

        if self.tFlag:
            imsave(self.savePath, self.temp)
        else:
            imsave(self.savePath, self.targetImage)

    def resetScreen(self):
        if self.tFlag:
            self.view.setPixmap(self.pixmap)

            self.acquirePts.setEnabled(True)
            self.point1.setEnabled(True)
            self.point2.setEnabled(True)
            self.point3.setEnabled(True)
            self.point4.setEnabled(True)
            self.tFlag = False

    def sourceReset(self):
        if self.tFlag:
            self.view.setPixmap(self.pixmap)

            self.point1.setText('')
            self.point2.setText('')
            self.point3.setText('')
            self.point4.setText('')

            self.spoint1.setText('')
            self.spoint2.setText('')
            self.tFlag = False

        else:
            self.spoint1.setText('')
            self.spoint2.setText('')

    def doTransform(self):
        self.acquirePts.setEnabled(False)
        self.point1.setEnabled(False)
        self.point2.setEnabled(False)
        self.point3.setEnabled(False)
        self.point4.setEnabled(False)

        ind = self.effectBox.currentIndex()

        if ind == 0:
            effect = None
        elif ind == 1:
            effect = Effect.rotate90
        elif ind == 2:
            effect = Effect.rotate180
        elif ind == 3:
            effect = Effect.rotate270
        elif ind == 4:
            effect = Effect.flipHorizontally
        elif ind == 5:
            effect = Effect.flipVertically
        elif ind == 6:
            effect = Effect.transpose
        else:
            effect = None

        # if self.sourceImage.ndim == 2:
        #     newT = Transformation(self.sourceImage)
        #     newT.setupTransformation(self.targetPts, effect)
        #     newTarget = newT.transformImage(self.targetImage)
        #
        #     imsave('.temp.png', newTarget)
        #     pixmap = QPixmap('.temp.png')
        #
        #     if os.path.exists('.temp.png'):
        #         os.remove('.temp.png')
        #
        #     self.view.setPixmap(pixmap)
        #
        #     self.tFlag = True

        # if self.sourceImage.ndim == 3:
        #     newCT = ColorTransformation(self.sourceImage)
        #     newCT.setupTransformation(self.targetPts, effect)
        #     temp = copy.deepcopy(self.targetImage)
        #     newTarget = newCT.transformImage(temp)
        #
        #     imsave('.temp.png', newTarget)
        #     pixmap = QPixmap('.temp.png')
        #
        #     if os.path.exists('.temp.png'):
        #         os.remove('.temp.png')
        #
        #     self.view.setPixmap(pixmap)
        #
        #     self.tFlag = True
        newGT = GeneralTransformation(self.sourceImage, self.sourcePts)
        newGT.setupTransformation(self.targetPts, effect)
        self.temp = copy.deepcopy(self.targetImage)
        newTarget = newGT.transformImage(self.temp)

        imsave('.temp.png', newTarget)
        pixmap = QPixmap('.temp.png')

        if os.path.exists('.temp.png'):
            os.remove('.temp.png')

        self.view.setPixmap(pixmap)

        self.tFlag = True

class GeneralTransformation(ColorTransformation, Transformation):

    def __init__(self, sourceImage, sourcePoints=None):
        super(GeneralTransformation, self).__init__(sourceImage)
        if sourcePoints != None:
            if len(sourcePoints) == 0:
                sourcePoints = None
        if sourcePoints != None:
            if len(sourcePoints) != 2:
                raise ValueError("Please only give two sourcePoints")

        self.sourcePts = sourcePoints
        self.sourceImage = sourceImage

    def setupTransformation(self, targetPoints, effect=None):
        if len(targetPoints) != 4:
            raise ValueError('\'targetPoints\' must be a list of exactly 4 tuples')

        self.minpt, self.maxpt = self.computeBoundingBox(targetPoints)

        if self.sourceImage.ndim == 2:
            self.row, self.column = self.sourceImage.shape
        if self.sourceImage.ndim == 3:
            self.row, self.column, self.dim = self.sourceImage.shape

        if self.sourcePts == None:
            sourcePoints = [(0,0),(self.column-1,0),(0,self.row-1),(self.column-1,self.row-1)]

        else:
            pt1 = self.sourcePts[0]
            pt2 = self.sourcePts[1]
            sourcePoints = [pt1, (pt2[0], pt1[1]), (pt1[0], pt2[1]), pt2]

        if self.homography == None:

            self.homography = Homography(sourcePoints=sourcePoints, targetPoints=targetPoints, effect=effect)

    def transformImage(self, containerImage):
        if type(containerImage) != np.ndarray:
            raise TypeError('Please give a containerImage that is of type "ndarray"')

        if self.sourcePts != None:
            pt1 = [int(x) for x in self.sourcePts[0]]
            pt2 = [int(x) for x in self.sourcePts[1]]

        if self.sourceImage.ndim == 2 and containerImage.ndim == 3:
            fx = rbs(range(0,self.row), range(0,self.column), self.sourceImage, kx=1, ky=1)

            for invX in range(0, containerImage.shape[0]):
                for invY in range(0,containerImage.shape[1]):
                    x, y = self.homography.inverseProject((invY,invX))
                    if self.sourcePts != None:
                        if x >=pt1[0] and x <= pt2[0]-1 and y >= pt1[1] and y <= pt2[1]-1:
                            pixelData = fx(y,x)
                            containerImage[invX, invY, 0] = pixelData
                            containerImage[invX, invY, 1] = pixelData
                            containerImage[invX, invY, 2] = pixelData
                    else:
                        if x >=0 and x <= self.column-1 and y >= 0 and y <= self.row-1:
                            pixelData = fx(y,x)
                            containerImage[invX, invY, 0] = pixelData
                            containerImage[invX, invY, 1] = pixelData
                            containerImage[invX, invY, 2] = pixelData

        elif self.sourceImage.ndim == 3 and containerImage.ndim == 2:
            row, col = containerImage.shape
            newImage = np.ndarray(shape=(row,col,3), dtype=np.uint8)

            newImage[:,:,0] = containerImage
            newImage[:,:,1] = containerImage
            newImage[:,:,2] = containerImage

            containerImage = newImage

            blue = rbs(range(0,self.row), range(0,self.column), self.sourceImage[:,:,0], kx=1, ky=1)
            red = rbs(range(0,self.row), range(0,self.column), self.sourceImage[:,:,1], kx=1, ky=1)
            green = rbs(range(0,self.row), range(0,self.column), self.sourceImage[:,:,2], kx=1, ky=1)

            for invX in range(0, containerImage.shape[0]):
                for invY in range(0,containerImage.shape[1]):
                    x, y = self.homography.inverseProject((invY,invX))
                    if self.sourcePts != None:
                        if x >=pt1[0] and x <= pt2[0]-1 and y >= pt1[1] and y <= pt2[1]-1:
                            pdBlue = blue(y,x)
                            pdRed = red(y,x)
                            pdGreen = green(y,x)
                            containerImage[invX, invY, 0] = pdBlue
                            containerImage[invX, invY, 1] = pdRed
                            containerImage[invX, invY, 2] = pdGreen
                    else:
                        if x >=0 and x <= self.column-1 and y >= 0 and y <= self.row-1:
                            pdBlue = blue(y,x)
                            pdRed = red(y,x)
                            pdGreen = green(y,x)
                            containerImage[invX, invY, 0] = pdBlue
                            containerImage[invX, invY, 1] = pdRed
                            containerImage[invX, invY, 2] = pdGreen

        elif self.sourceImage.ndim == 2 and containerImage.ndim == 2:
            fx = rbs(range(0,self.row), range(0,self.column), self.sourceImage, kx=1, ky=1)

            for invX in range(0, containerImage.shape[0]):
                for invY in range(0,containerImage.shape[1]):
                    x, y = self.homography.inverseProject((invY,invX))
                    if self.sourcePts != None:
                        if x >=pt1[0] and x <= pt2[0]-1 and y >= pt1[1] and y <= pt2[1]-1:
                            pixelData = fx(y,x)
                            containerImage[invX, invY] = pixelData
                    else:
                        if x >=0 and x <= self.column-1 and y >= 0 and y <= self.row-1:
                            pixelData = fx(y,x)
                            containerImage[invX, invY] = pixelData

        else:
            blue = rbs(range(0,self.row), range(0,self.column), self.sourceImage[:,:,0], kx=1, ky=1)
            red = rbs(range(0,self.row), range(0,self.column), self.sourceImage[:,:,1], kx=1, ky=1)
            green = rbs(range(0,self.row), range(0,self.column), self.sourceImage[:,:,2], kx=1, ky=1)

            for invX in range(0, containerImage.shape[0]):
                for invY in range(0,containerImage.shape[1]):
                    x, y = self.homography.inverseProject((invY,invX))
                    if self.sourcePts != None:
                        if x >=pt1[0] and x <= pt2[0]-1 and y >= pt1[1] and y <= pt2[1]-1:
                            pdBlue = blue(y,x)
                            pdRed = red(y,x)
                            pdGreen = green(y,x)
                            containerImage[invX, invY, 0] = pdBlue
                            containerImage[invX, invY, 1] = pdRed
                            containerImage[invX, invY, 2] = pdGreen
                    else:
                        if x >=0 and x <= self.column-1 and y >= 0 and y <= self.row-1:
                            pdBlue = blue(y,x)
                            pdRed = red(y,x)
                            pdGreen = green(y,x)
                            containerImage[invX, invY, 0] = pdBlue
                            containerImage[invX, invY, 1] = pdRed
                            containerImage[invX, invY, 2] = pdGreen

        return containerImage

if __name__ == "__main__":
    currentApp = QApplication(sys.argv)
    currentForm = HomographyApp()

    currentForm.show()
    currentApp.exec_()

    sourceImg = np.ones([10, 10, 3], dtype=np.uint8)
    spts = [(2,2), (10,10)]
    frontPoints = [(159.0, 136.0), (345.0, 85.0), (160.0, 276.0), (309.0, 216.0)]
    myGT = GeneralTransformation(sourceImg)
    myGT.setupTransformation(frontPoints)
