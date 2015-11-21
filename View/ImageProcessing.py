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
                          apexes,
                          occupiedPoints):
        self.convertToRGB()
        self.drawPaths(targetCoord, apexes, occupiedPoints)
        self.showImage()

    def getSize(self,):
        self.dimension = self.image.size

    def loadImage(self):
        self.image= Image.open('Images/dobry.bmp') 

    def drawPaths(self,
                  targetCoord,
                  apexes,
                  occupiedPoints):

        draw = ImageDraw.Draw(self.image)

        #draw.line(( 643, 322, 655, 322), fill=(233, 0, 0))
    
        xTargetCoord = targetCoord[0]
        yTargetCoord = targetCoord[1]
        
        apex = apexes[xTargetCoord][yTargetCoord]
        
        
        for idxX in range(self.dimension[0]):
            for idxY in range(self.dimension[1]):
                if(occupiedPoints[idxX][idxY] == 0 and self.nonDrawPoints[idxX][idxY] == 0):
                    draw.point((idxX, idxY), fill=(201, 133, 185))
                     
        while ( (apex[1] != (-1, -1)) ):
            firstPoint = apex[0]
            secondPoint = apex[1]
            draw.line((firstPoint[0], firstPoint[1], secondPoint[0], secondPoint[1]), fill=(255, 255, 0))
            apex = apexes[secondPoint[0]][secondPoint[1]]
            



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
    
    def findWeightOfColor(self, weightOfPoint):
         
        if( (weightOfPoint[0] > weightOfPoint[1]) and (weightOfPoint[0] > weightOfPoint[2]) ):
            return 1280
        if( (weightOfPoint[2] > weightOfPoint[0]) and (weightOfPoint[2] > weightOfPoint[1])):
            return 2560
        if( (weightOfPoint[1] > weightOfPoint[0]) and (weightOfPoint[1] > weightOfPoint[2])):
            return 1
        return 0
        
    def createWeightsOfPoints(self):
        self.weightsOfPoints = []
        self.nonDrawPoints = []
        for idxX in range(self.dimension[0]):
            self.weightsOfPoints.append([])
            self.nonDrawPoints.append([])
            for idxY in range(self.dimension[1]):
                weightOfPoint = self.image.getpixel((idxX, idxY))
                
                weight = self.findWeightOfColor(weightOfPoint)
                if(weight) > 1:
                    self.occupiedPoints[idxX][idxY] = 0
                    self.nonDrawPoints[idxX].append(1)
                else:
                    self.nonDrawPoints[idxX].append(0)
                    
#                 print "weightOfPoint = " + str(weight)
                self.weightsOfPoints[idxX].append(weight)
                
    def getWeightsOfPoints(self):
        return self.weightsOfPoints
    
    def getDimension(self):
        return self.dimension