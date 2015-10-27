from Path import Path
from Common import *
import copy

class BestSearch():
    
    def __init__(self,
                 occupiedPoints,
                 weightsOfPoints,
                 dimension):
        self.occupiedPoints  = occupiedPoints
        self.weightsOfPoints = weightsOfPoints
        self.dimension       = dimension
        
    def printListOfPath(self,
                        listOfPaths):
        numOfPaths = len(listOfPaths)
        
        for pathsIdx in range(numOfPaths):
            print "path nr = " + str(pathsIdx)
            listOfPaths[pathsIdx].printPath()
            
    def setOccupiedPoints(self,
                          listOfPoints):
        
        numOfPoints = len(listOfPoints)
        for pointIdx in range(numOfPoints):
            self.occupiedPoints[listOfPoints[pointIdx][0]][listOfPoints[pointIdx][1]] = 1
            
    def search(self):
        startPoint = (0, 0)
        #stopPoint =  (self.dimension[0] - 1, self.dimension[1] - 1)
        stopPoint = (110, 110)
        
        listOfPaths = [Path(startPoint)]
        self.occupiedPoints[startPoint[0]][startPoint[1]] = 1
        index = 0
        while ( ((listOfPaths[0].getCoordinate()) != stopPoint)):

            actualPoint = listOfPaths[0].getCoordinate()
            
            self.occupiedPoints[actualPoint[0]][actualPoint[1]] = 1
            
            listOfNewPoints = self.getNewPoints(listOfPaths)
            
            if (len(listOfNewPoints) == 0):
                listOfPaths.pop(0)
            else:
                self.setOccupiedPoints(listOfNewPoints)
                                  
                isTarget = self.addPaths(listOfPaths,
                                         listOfNewPoints,
                                         stopPoint)
                if(isTarget):
                    return listOfPaths
        
        return listOfPaths
            
    
    def findIdxInList(self,
                      weightOfPath,
                      listOfPaths):
        idx = 0
        numOfPath = len(listOfPaths)
        for pathIdx in range(numOfPath):
            if(weightOfPath < listOfPaths[pathIdx].getWeight()):
                return pathIdx
        return numOfPath

    def addPaths(self,
                 listOfPaths,
                 listOfNewPoints,
                 stopPoint):
        
        numOfNewPoints = len(listOfNewPoints)
        actualPoint = listOfPaths[0].getCoordinate()
        oldFirstPath = listOfPaths.pop(0)
        
        for pointIdx in range(numOfNewPoints):
            
            newPath = copy.deepcopy(oldFirstPath)  
            newPath.addNewPoint(listOfNewPoints[pointIdx],
                                self.weightsOfPoints[listOfNewPoints[pointIdx][0]]
                                                    [listOfNewPoints[pointIdx][1]])
            if (listOfNewPoints[pointIdx] == stopPoint):
                listOfPaths.insert(0, newPath)
                return True
            else:
                weightOfPath = newPath.getWeight()
            
                idxOfPath = self.findIdxInList(weightOfPath,
                                               listOfPaths)
                listOfPaths.insert(idxOfPath, newPath)
        return False
    
    def isFreePoint(self,
                    adjacentPoint):
        
        if (( adjacentPoint[0] >= 0 ) & \
            ( adjacentPoint[1] >= 0 ) & \
            ( adjacentPoint[0] < self.dimension[0]) & \
            ( adjacentPoint[1] < self.dimension[1])):
            if( self.occupiedPoints[adjacentPoint[0]][adjacentPoint[1]] == 0):
                return True
            else:
                return False
        else:
            return False
               
               
        
    def getNewPoints(self, 
                     listOfPaths):
        listOfNewPoints = []

        actualPoint = listOfPaths[0].getCoordinate()
        numOfAdjacentPoints = len(adjacentPoints)
        
        for idxPoint in range(numOfAdjacentPoints):
            adjacentPoint = ( actualPoint[0] + adjacentPoints[idxPoint][0], 
                              actualPoint[1] + adjacentPoints[idxPoint][1])
            if(self.isFreePoint(adjacentPoint)):
                listOfNewPoints.append(adjacentPoint)
                
        return listOfNewPoints
    
    def sortListOfPaths(self,
                        listOfPaths):
        sort = True
        numOfPaths = len(listOfPaths)
        while(sort == True):
            sort = False
            for pathIdx in range(1, numOfPaths):
                firstPath  = listOfPaths[pathIdx-1].getWeight()
                secondPath = listOfPaths[pathIdx].getWeight()
                if(firstPath > secondPath):
                    sort = True
                    tempPath = listOfPaths[pathIdx]
                    listOfPaths[pathIdx]   = listOfPaths[pathIdx-1]
                    listOfPaths[pathIdx-1] = tempPath
