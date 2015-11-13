from ImageProcessing import ImageProcessing
from Search import Search
from BestSearch import BestSearch
from DeepSearch import DeepSearch
from AlongSideSearch import AlongSideSearch
import timeit

class PathFinder():
        
    def findPathsVariusAlgo(self):
        
        bestSearchAlgorithm      = BestSearch()
        deepSearchAlgorithm      = DeepSearch()
        alongSideSearchAlgorithm = AlongSideSearch()
        
        print " ** Best Search **"
        self.executeAlgo(bestSearchAlgorithm)
        
        print " ** Deep Search **"
        self.executeAlgo(deepSearchAlgorithm)
        
        print " ** Alongside Search **"
        self.executeAlgo(alongSideSearchAlgorithm)
        
    def executeAlgo(self,
                    specificAlgorithms):
        
        self.loadImage()
        
        start = timeit.default_timer()
    
        bestSearch = Search(specificAlgorithms,
                            self.imageProcessing.getOccupiedPoints(),
                            self.imageProcessing.getWeightsOfPoints(),
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