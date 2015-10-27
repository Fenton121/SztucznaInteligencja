from Apex import Apex
from Common import *
import copy

class BestSearch():
    
    def __init__(self,
                 occupiedPoints,
                 weightsOfPoints,
                 dimension):
        self.occupiedPoints       = occupiedPoints
        self.weightsOfPoints      = weightsOfPoints
        self.dimension            = dimension
        self.numOfAdjacentPoints  = len(adjacentPoints)
        
        self.apexes = []
        for idxX in range(self.dimension[0]):
            self.apexes.append([])
            for idxY in range(self.dimension[1]):
                self.apexes[idxX].append(0)
            
    def setOccupiedPoints(self,
                          listOfPoints):
        
        numOfPoints = len(listOfPoints)
        for pointIdx in range(numOfPoints):
            self.occupiedPoints[listOfPoints[pointIdx][0]][listOfPoints[pointIdx][1]] = 0
            
    def search(self):
        startPointCoord = (0, 0)
        #stopPointCoord =  (self.dimension[0] - 1, self.dimension[1] - 1)
        stopPointCoord = (510, 510)
        
        actualPointCoord = startPointCoord
        startApex = Apex(actualPointCoord, (-1, -1))
        listOfActualApexes = [copy.deepcopy(startApex)]
        self.occupiedPoints[actualPointCoord[0]][actualPointCoord[1]] = 0
        self.apexes[actualPointCoord[0]][actualPointCoord[1]] = startApex
        
        while ( True ):
            
            actualPointCoord = listOfActualApexes[0].getCoordinate()
            self.occupiedPoints[actualPointCoord[0]][actualPointCoord[1]] = 0
            
            listOfNewPoints = self.getNewPoints(actualPointCoord)
            
            #if (len(listOfNewPoints) == 0):
                #listOfActualApexes.pop(0)
            #else:
            self.setOccupiedPoints(listOfNewPoints)
                                  
            isTarget = self.addApexes(listOfActualApexes,
                                      listOfNewPoints,
                                      stopPointCoord)
            if(isTarget):
                targeCoord = listOfActualApexes[0].getCoordinate()
                return targeCoord, self.apexes
            
    
    def findIdxInList(self,
                      weightOfPath,
                      listOfActualApexes):
        
        numOfApexes = len(listOfActualApexes)
        for apexIdx in range(numOfApexes):
            if(weightOfPath < listOfActualApexes[apexIdx].getWeight()):
                return apexIdx
        return numOfApexes

    def addApexes(self,
                  listOfActualApexes,
                  listOfNewPoints,
                  stopPoint):
        
        numOfNewApexes = len(listOfNewPoints)
        actualPoint    = listOfActualApexes[0].getCoordinate()
        oldFirstApex   = listOfActualApexes.pop(0)
        
        for pointIdx in range(numOfNewApexes):
            
            newApex = copy.deepcopy(oldFirstApex)  
            xApexCoord = listOfNewPoints[pointIdx][0]
            yApexCoord = listOfNewPoints[pointIdx][1]
            newApex.changeApex(listOfNewPoints[pointIdx],
                               self.weightsOfPoints[xApexCoord][yApexCoord])
            
            self.apexes[xApexCoord][yApexCoord] = newApex
            if (listOfNewPoints[pointIdx] == stopPoint):
                listOfActualApexes.insert(0, newApex)
                return True
            else:
                weightOfPath = newApex.getWeight()
            
                idxOfApex = self.findIdxInList(weightOfPath,
                                               listOfActualApexes)
                listOfActualApexes.insert(idxOfApex, newApex)
        return False
    
    def isFreePoint(self,
                    adjacentPoint):
        
        #isInside = ((adjacentPoint[0] + 1) * \
                    #(adjacentPoint[1] + 1) * \
                    #(self.dimension[0] - adjacentPoint[0]) * \
                    #(self.dimension[1] - adjacentPoint[1])) > 0
        #if(isInside):
            #return self.occupiedPoints[adjacentPoint[0]][adjacentPoint[1]]
        #else:
            #return False

            
        if (( adjacentPoint[0] >= 0 ) & \
            ( adjacentPoint[1] >= 0 ) & \
            ( adjacentPoint[0] < self.dimension[0]) & \
            ( adjacentPoint[1] < self.dimension[1])):
            
            return self.occupiedPoints[adjacentPoint[0]][adjacentPoint[1]]
        else:
            return False

    def getNewPoints(self, 
                     actualPointCoord):
        listOfNewPoints = []
        
        for idxPoint in range(self.numOfAdjacentPoints):
            adjacentPoint = ( actualPointCoord[0] + adjacentPoints[idxPoint][0], 
                              actualPointCoord[1] + adjacentPoints[idxPoint][1])
            if(self.isFreePoint(adjacentPoint)):
                listOfNewPoints.append(adjacentPoint)
                
        return listOfNewPoints
    