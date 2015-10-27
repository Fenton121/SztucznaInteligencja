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
                          listOfPaths):
        self.convertToRGB()
        self.drawPaths(listOfPaths)
        self.showImage()

    def getSize(self,):
        self.dimension = self.image.size
        print self.dimension

    def loadImage(self):
        self.image= Image.open('Images/labirynt2.bmp') 

    def drawPaths(self,
                  listOfPaths):
        listOfPoints = listOfPaths[0].getListOfPoints()
        
        
        numOfPoints = len(listOfPoints)
        
        draw = ImageDraw.Draw(self.image)
        #draw.line(( self.dimension[0] -1, self.dimension[1]-1, self.dimension[0] - 1, self.dimension[1] - 1), fill=(0, 233, 0))
        #draw.line(( 110, 110, 130, 120), fill=(0, 233, 0))
        
        for pointIdx in range(1, numOfPoints):
            firstPoint = listOfPoints[pointIdx - 1]
            secondPoint = listOfPoints[pointIdx]
            draw.line((firstPoint[0], firstPoint[1], secondPoint[0], secondPoint[1]), fill=(233, 0, 0))

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
                self.occupiedPoints[idxX].append(0)
        
    def getOccupiedPoints(self):
        return self.occupiedPoints
    
    def createWeightsOfPoints(self):
        self.weightsOfPoints = []
        for idxX in range(self.dimension[0]):
            self.weightsOfPoints.append([])
            for idxY in range(self.dimension[1]):
                self.weightsOfPoints[idxX].append(256 - self.image.getpixel((idxX, idxY)))
                if(256 - self.image.getpixel((idxX, idxY)) > 200):
                    self.occupiedPoints[idxX][idxY] = 1
                
    def getWeightsOfPoints(self):
        return self.weightsOfPoints
    
    def getDimension(self):
        return self.dimension