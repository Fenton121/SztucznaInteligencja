from Apex import Apex
from Common import *
import copy

class BestSearch():
    def __init__(self,
                 startPointCoord,
                 stopPointCoord,
                 weightsOfPoints):
        self.startPointCoord = startPointCoord
        self.stopPointCoord = stopPointCoord
        self.weightsOfPoints = weightsOfPoints
        
    def findIdxInList(self,
                      weightOfApex,
                      listOfActualApexes):
        numOfApexes = len(listOfActualApexes)
        for apexIdx in range(numOfApexes):
            if(weightOfApex < listOfActualApexes[apexIdx][2]):
                return apexIdx
        return numOfApexes
    
    def getWeightOfPoint(self,
                         xApexCoord,
                         yApexCoord):
        return self.weightsOfPoints[xApexCoord][yApexCoord]
    
    def getStartPointCoord(self):
        return self.startPointCoord
    
    def getStopPointCoord(self):
        return self.stopPointCoord 