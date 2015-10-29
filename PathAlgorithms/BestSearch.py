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
        stopPointCoord = (455, 290)
        
        startApex = [startPointCoord, (-1, -1), 0]
        
        listOfActualApexes = [startApex]
        self.occupiedPoints[startPointCoord[0]][startPointCoord[1]] = 0
        self.apexes[startPointCoord[0]][startPointCoord[1]] = startApex
        
        
        while ( listOfActualApexes[0][0] != stopPointCoord ):
            
            actualPointCoord = listOfActualApexes[0][0]
            self.occupiedPoints[actualPointCoord[0]][actualPointCoord[1]] = 0
            
            listOfNewPoints = self.getNewPoints(actualPointCoord)
    
            self.setOccupiedPoints(listOfNewPoints)
            
            self.addApexes(listOfActualApexes,
                           listOfNewPoints,
                           stopPointCoord)
           
            
        return listOfActualApexes[0][0], self.apexes
            
    
    def findIdxInList(self,
                      weightOfApex,
                      listOfActualApexes):
        
        numOfApexes = len(listOfActualApexes)
        for apexIdx in range(numOfApexes):
            if(weightOfApex < listOfActualApexes[apexIdx][2]):
                return apexIdx
        return numOfApexes

    def addApexes(self,
                  listOfActualApexes,
                  listOfNewPoints,
                  stopPoint):
        
        numOfNewApexes = len(listOfNewPoints)
        actualPoint    = listOfActualApexes[0][0]
        oldFirstApex   = listOfActualApexes.pop(0)
        
        for pointIdx in range(numOfNewApexes):
            newApex = copy.copy(oldFirstApex)
            
            xApexCoord = listOfNewPoints[pointIdx][0]
            yApexCoord = listOfNewPoints[pointIdx][1]
            
            newApex[1] = newApex[0]
            newApex[0] = listOfNewPoints[pointIdx]
            newApex[2] = newApex[2] + self.weightsOfPoints[xApexCoord][yApexCoord]
            
            self.apexes[xApexCoord][yApexCoord] = newApex
            
            idxOfApex = self.findIdxInList(newApex[2],
                                           listOfActualApexes)
            
            listOfActualApexes.insert(idxOfApex, newApex)
                
    
    def isFreePoint(self,
                    adjacentPoint):     
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
        
        for idxPoint in range(numOfAdjacentPoints):
            adjacentPoint = ( actualPointCoord[0] + adjacentPoints[idxPoint][0], 
                              actualPointCoord[1] + adjacentPoints[idxPoint][1])
            if(self.isFreePoint(adjacentPoint)):
                listOfNewPoints.append(adjacentPoint)
                
        return listOfNewPoints
    