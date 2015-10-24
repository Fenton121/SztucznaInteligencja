
class Path():
    def __init__(self, startPoint):
        self.listOfPoint = [startPoint]
        
        
    def getCoordinate(self):
        actualPoint = self.listOfPoint[-1]
        self.listOfPoint[-1] = (actualPoint[0] + 1, actualPoint[1] + 1)
        return (actualPoint)