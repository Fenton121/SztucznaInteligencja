from Apex import Apex
from Common import *
import copy

class DeepSearch():
    def __init__(self,
                 weightsOfPoints):
        self.weightsOfPoints = weightsOfPoints
    def findIdxInList(self,
                      weightOfApex,
                      listOfActualApexes):
        return 0
    
    def getWeightOfPoint(self,
                         xApexCoord,
                         yApexCoord):
        return self.weightsOfPoints[xApexCoord][yApexCoord]