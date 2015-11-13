from ImageProcessing import ImageProcessing
from Search import Search
from BestSearch import BestSearch
import timeit

class PathFinder():
        
    def bestSearch(self):
        self.loadImage()
        
        start = timeit.default_timer()
        
        bestSearchAlgorithm = BestSearch()
        
        bestSearch = Search(bestSearchAlgorithm,
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