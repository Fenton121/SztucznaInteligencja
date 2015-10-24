from PIL import Image, ImageDraw
import operator
import numpy

class ImageProcessing():

    def processImage(self):
        self.loadImage()
        self.getSize()
        self.createOccupiedPoints()
        self.createWeightsOfPoints()

        self.convertToRGB()
        self.drawPaths()
        self.showImage()

    def getSize(self,):
        self.dimension = self.image.size
        print self.dimension

    def loadImage(self):
        self.image= Image.open('bmp.bmp') 

    def drawPaths(self):
        draw = ImageDraw.Draw(self.image)
        draw.line((0, 0) + self.dimension, fill=(233, 0, 0))
        draw.line((0, self.dimension[1], self.dimension[0], 0), fill=(233, 0, 0))

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
        self.occupiedPoints = numpy.zeros((self.dimension[0], self.dimension[1]))
        
    def getOccupiedPoints(self):
        return self.occupiedPoints
    
    def createWeightsOfPoints(self):
        self.weightsOfPoints = numpy.zeros((self.dimension[0], self.dimension[1]))
        for idxX in range(self.dimension[0]):
            for idxY in range(self.dimension[1]):
                self.weightsOfPoints[idxX, idxY] = self.image.getpixel(idxX, idxY)
                
    def getWeightsOfPoints(self):
        return self.occupiedPoints