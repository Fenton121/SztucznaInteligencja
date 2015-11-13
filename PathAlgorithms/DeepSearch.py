from Apex import Apex
from Common import *
import copy

class DeepSearch():
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
        return 0
    
    def getWeightOfPoint(self,
                         xApexCoord,
                         yApexCoord):
        return self.weightsOfPoints[xApexCoord][yApexCoord]
    
    def getStartPointCoord(self):
        return self.startPointCoord
    
    def getStopPointCoord(self):
        return self.stopPointCoord 