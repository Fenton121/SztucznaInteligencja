from Path import Path
from Common import *

class BestSearch():
    def search(self,
               occupiedPoints,
               weightsOfPoints):
        startPoint = (0, 0)
        stopPoint =  (10, 10)
        listOfPath = [Path(startPoint)]

        while ( (listOfPath[0].getCoordinate()) != stopPoint):
            actualPoint = listOfPath[0].getCoordinate()
            occupiedPoints[actualPoint[0]][actualPoint[1]] = 1
            self.addPaths(listOfPath, occupiedPoints)
        
    def addPaths(self, listOfPath, occupiedPoints):
        print "hah" + str(numOfPossbilePoints)
        actualPoint = listOfPath[0].getCoordinate()