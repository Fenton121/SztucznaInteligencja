from PIL import Image, ImageDraw
import operator
import numpy
import sys

class ImageProcessing():

    def processImage(self):
        self.loadImage()
        self.getSize()
        self.createOccupiedPoints()
        self.createWeightsOfPoints()
        
    def convertAndDisplay(self,
                          targetCoord,
                          apexes):
        self.convertToRGB()
        self.drawPaths(targetCoord, apexes)
        self.showImage()

    def getSize(self,):
        self.dimension = self.image.size
        print self.dimension

    def loadImage(self):
        self.image= Image.open('Images/labirynt2.bmp') 

    def drawPaths(self,
                  targetCoord,
                  apexes):

        draw = ImageDraw.Draw(self.image)
        #draw.line(( 455, 290, 470, 290), fill=(233, 0, 0))
    
        xTargetCoord = targetCoord[0]
        yTargetCoord = targetCoord[1]
        
        apex = apexes[xTargetCoord][yTargetCoord]
        
        
        index = 0
        while ( (apex[0] != (-1, -1)) & (index < 100) ):

            firstPoint = apex[0]
            secondPoint = apex[1]
            print "firstPoint = " + str(firstPoint) + "secondPoint = " + str(secondPoint)
            draw.line((firstPoint[0], firstPoint[1], secondPoint[0], secondPoint[1]), fill=(233, 0, 0))
            apex = apexes[secondPoint[0]][secondPoint[1]]
            index = index + 1

    def showImage(self):
        resizeX = operator.div(1366, self.dimension[0])
        resizeY = operator.div(768, self.dimension[1])

        if(resizeX > resizeY):
            resize = resizeY
        else:
            resize = resizeX

        if(resize == 0):
            resize = 1

        resizedImg = self.image.resize((self.dimension[0]*resize, self.dimension[1]*resize))

        resizedImg.show()

    def convertToRGB(self):
        self.image = self.image.convert('RGB')

    def createOccupiedPoints(self):
        self.occupiedPoints = []
        for idxX in range(self.dimension[0]):
            self.occupiedPoints.append([])
            for idxY in range(self.dimension[1]):
                self.occupiedPoints[idxX].append(1)
        
    def getOccupiedPoints(self):
        return self.occupiedPoints
    
    def createWeightsOfPoints(self):
        self.weightsOfPoints = []
        for idxX in range(self.dimension[0]):
            self.weightsOfPoints.append([])
            for idxY in range(self.dimension[1]):
                weightOfPoint = self.image.getpixel((idxX, idxY))
                self.weightsOfPoints[idxX].append(256 - weightOfPoint)
                if(weightOfPoint < 30):
                    self.occupiedPoints[idxX][idxY] = 0
                
    def getWeightsOfPoints(self):
        return self.weightsOfPoints
    
    def getDimension(self):
        return self.dimension