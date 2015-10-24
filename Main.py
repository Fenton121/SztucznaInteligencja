import sys
sys.path.append("View")

from ImageProcessing import ImageProcessing

class Search:
    def searchBestPath(self):
        imageProcessing = ImageProcessing()
        imageProcessing.processImage()

if __name__ == "__main__":
    search = Search()
    search.searchBestPath()

    


