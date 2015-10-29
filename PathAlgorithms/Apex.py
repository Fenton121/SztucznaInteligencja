
class Apex():
    def __init__(self, point, previousPoint):
        self.point         = point;
        self.previousPoint = previousPoint
        self.weight        = 0
        
    def changeApex(self,
                   newPoint,
                   weightOfPoint):
        self.previousPoint = self.point
        self.point = newPoint
        self.weight = self.weight + weightOfPoint

    def getPreviousPoint(self):
        return self.previousPoint
    
    def getWeight(self):
        return self.weight
    
    def getCoordinate(self):
        return self.point
    
    def setWeight(self,
                  weight):
        self.weightOfPoint = weight;