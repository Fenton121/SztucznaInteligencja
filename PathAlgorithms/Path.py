
class Path():
    def __init__(self, startPoint):
        self.listOfPoint = [startPoint]
        
        self.index = 0
    def getCoordinate(self):
        
        self.index = self.index + 1
        if (self.index <= 10):
            return self.listOfPoint[-1]
        else:
        #actualPoint = self.listOfPoint[-1]
        #self.listOfPoint[-1] = (actualPoint[0] + 1, actualPoint[1] + 1)
            return (10, 10)
        
            