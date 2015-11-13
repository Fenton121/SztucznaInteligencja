import sys
sys.path.append("View")
sys.path.append("PathAlgorithms")
sys.path.append("Images")
sys.path.append("Common")

from PathFinder import PathFinder

if __name__ == "__main__":
    pathFinder = PathFinder();
    pathFinder.findPathsVariusAlgo()

    


