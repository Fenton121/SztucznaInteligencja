from Apex import Apex
from Common import *
import copy
import timeit

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
        stopPointCoord = (455, 290)
        
        startApex = [startPointCoord, (-1, -1), 0]
        
        listOfActualApexes = [startApex]
        self.occupiedPoints[startPointCoord[0]][startPointCoord[1]] = 0
        self.apexes[startPointCoord[0]][startPointCoord[1]] = startApex
        
        index = 0
        
        addApexesTime = 0
        copyTime = 0
        findIdxInListTime = 0
        
        while ( listOfActualApexes[0][0] != stopPointCoord ):
            
            actualPointCoord = listOfActualApexes[0][0]
            self.occupiedPoints[actualPointCoord[0]][actualPointCoord[1]] = 0
            
            print "index =" + str(index) + "actualPointCoord = " + str(actualPointCoord)
            index = index + 1
            
            listOfNewPoints = self.getNewPoints(actualPointCoord)
    
            self.setOccupiedPoints(listOfNewPoints)
            
            startAddApexes = timeit.default_timer()
            copyTimeTemp, findIdxInListTimeTemp = self.addApexes(listOfActualApexes,
                                                                 listOfNewPoints,
                                                                 stopPointCoord)
            stopAddApexes = timeit.default_timer()
            addApexesTime =  addApexesTime + (stopAddApexes - startAddApexes)
            
            copyTime = copyTime + copyTimeTemp
            findIdxInListTime = findIdxInListTime + findIdxInListTimeTemp
            
            
            
        #targeCoord = listOfActualApexes[0].getCoordinate()
        print "addApexesTime = " + str(addApexesTime)
        print "findIdxInListTime = " + str(findIdxInListTime)
        print "copyTime = " + str(copyTime)
        return listOfActualApexes[0][0], self.apexes
            
    
    def findIdxInList(self,
                      weightOfApex,
                      listOfActualApexes):
        
        numOfApexes = len(listOfActualApexes)
        #print "numOfApexes" + str(numOfApexes)
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
        oldFirstApex        = listOfActualApexes.pop(0)
        
        copyTime = 0
        findIdxInListTime = 0
        for pointIdx in range(numOfNewApexes):
            newApex = copy.copy(oldFirstApex)
            #startCopy = timeit.default_timer()
            #newApex = copy.copy(oldFirstApex)  
            
            #stopCopy = timeit.default_timer()
            
            #copyTime = copyTime + (stopCopy - startCopy)
            
            startAddApexes = timeit.default_timer()
            xApexCoord = listOfNewPoints[pointIdx][0]
            yApexCoord = listOfNewPoints[pointIdx][1]
            
            newApex[1] = newApex[0]
            newApex[0] = listOfNewPoints[pointIdx]
            newApex[2] = newApex[2] + self.weightsOfPoints[xApexCoord][yApexCoord]
            #newApex.changeApex(listOfNewPoints[pointIdx],
                               #self.weightsOfPoints[xApexCoord][yApexCoord])
            
            self.apexes[xApexCoord][yApexCoord] = newApex

            
            startFindIdxInList = timeit.default_timer()
            idxOfApex = self.findIdxInList(newApex[2],
                                           listOfActualApexes)
            stopFindIdxInList = timeit.default_timer()
            
            findIdxInListTime = findIdxInListTime + (stopFindIdxInList - startFindIdxInList)
            
            listOfActualApexes.insert(idxOfApex, newApex)
        return copyTime, findIdxInListTime
                
    
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
    