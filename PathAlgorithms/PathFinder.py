from ImageProcessing import ImageProcessing
from BestSearch import BestSearch

class PathFinder():
    def bestSearch(self):
        bestSearch = BestSearch()
        
        self.loadImage()
        
        bestSearch.search(self.imageProcessing.getOccupiedPoints,
                          self.imageProcessing.getWeightsOfPoints)
        self.dispaly()
        
    def loadImage(self):
        self.imageProcessing = ImageProcessing()
        self.imageProcessing.processImage()
        


    def dispaly(self):
        self.imageProcessing.convertAndDisplay()