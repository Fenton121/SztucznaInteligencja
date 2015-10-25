
class Path():
    def __init__(self, startPoint):
        self.listOfPoints = [startPoint]
        self.weight = 0
        #self.index = 0
        
    def printPath(self):
        numOfPoints = len(self.listOfPoints)
        
        for pointIdx in range(numOfPoints):
            print str(pointIdx) + ". " + str(self.listOfPoints[pointIdx])
    def getCoordinate(self):
        return self.listOfPoints[-1]
        
    def addNewPoint(self,
                    newPoint,
                    weightOfPoint):
        self.listOfPoints.append(newPoint)
        self.weight = self.weight + weightOfPoint
    
    def getWeight(self):
        return self.weight
    
    def getListOfPoints(self):
        return self.listOfPoints
            