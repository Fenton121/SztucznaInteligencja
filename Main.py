import sys
sys.path.append("View")

from ImageProcessing import ImageProcessing
from PathFinder import PathFinder

class Search:
    def searchBestPath(self):
        imageProcessing = ImageProcessing()
        imageProcessing.processImage()
        imageProcessing.createWeightsOfPoints()

if __name__ == "__main__":
    search = Search()
    search.searchBestPath()

    


