from ImageProcessing import ImageProcessing
from Search import Search
from BestSearch import BestSearch
from DeepSearch import DeepSearch
from AlongSideSearch import AlongSideSearch
from GreedySearch import GreedySearch
from aWithStarSearch import aWithStarSearch
import timeit
import copy

class PathFinder():
        
    def findPathsVariusAlgo(self):
        
        self.loadImage()
        
        startPointCoord = (0, 0)
        stopPointCoord = (455, 290)
        
        bestSearchAlgorithm      = BestSearch(startPointCoord,
                                              stopPointCoord,
                                              self.imageProcessing.getWeightsOfPoints())
        
        deepSearchAlgorithm      = DeepSearch(startPointCoord,
                                              stopPointCoord,
                                              self.imageProcessing.getWeightsOfPoints())
        
        alongSideSearchAlgorithm = AlongSideSearch(startPointCoord,
                                                   stopPointCoord,
                                                   self.imageProcessing.getWeightsOfPoints())
        
        greedySearchAlgorithm    = GreedySearch(startPointCoord,
                                                stopPointCoord,
                                                self.imageProcessing.getWeightsOfPoints())
        
        aWithStarSearchAlgorithm = aWithStarSearch(startPointCoord,
                                                   stopPointCoord,
                                                   self.imageProcessing.getWeightsOfPoints())
        
        print " ** Best Search **"
        self.executeAlgo(bestSearchAlgorithm)
         
        print " ** Deep Search **"
        self.executeAlgo(deepSearchAlgorithm)
           
        print " ** Alongside Search **"
        self.executeAlgo(alongSideSearchAlgorithm)
        
        print " ** Greedy Search **"
        self.executeAlgo(greedySearchAlgorithm)
        
        print " ** A** Search **"
        self.executeAlgo(aWithStarSearchAlgorithm)
        
    def executeAlgo(self,
                    specificAlgorithms):
        
        self.loadImage()
        
        start = timeit.default_timer()
    
        bestSearch = Search(specificAlgorithms,
                            self.imageProcessing.getOccupiedPoints(),
                            self.imageProcessing.getDimension())
        
        targetCoord, apexes = bestSearch.search()
        stop = timeit.default_timer()
        self.dispaly(targetCoord, apexes)

        print "time = " + str(stop - start)
        
        
    def loadImage(self):
        self.imageProcessing = ImageProcessing()
        self.imageProcessing.processImage()
        


    def dispaly(self,
                targetCoord,
                apexes):
        self.imageProcessing.convertAndDisplay(targetCoord,
                                               apexes)