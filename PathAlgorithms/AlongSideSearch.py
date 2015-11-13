from Apex import Apex
from Common import *
import copy

class AlongSideSearch():
    def __init__(self,
                 weightsOfPoints):
        self.weightsOfPoints = weightsOfPoints
        
    def findIdxInList(self,
                      weightOfApex,
                      listOfActualApexes):
        return len(listOfActualApexes)
    
    def getWeightOfPoint(self,
                         xApexCoord,
                         yApexCoord):
        return self.weightsOfPoints[xApexCoord][yApexCoord]