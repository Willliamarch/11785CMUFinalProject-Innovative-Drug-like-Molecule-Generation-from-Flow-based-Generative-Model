
# graph analysis of the distance tree

import networkx as nx
import numpy as np

def SimilarToDistance(SimilarityScore):
    if SimilarityScore == 0:
        return 10000
    else:
        return ((1 / SimilarityScore) - 1) * 100

# print (SimilarToDistance(1))
def SimiMatrixToDisMatrix(simiMatrix):
    distance = []
    for key in simiMatrix:
        distance.append(SimilarToDistance(float(key)))
    return distance


def Amplification(matrix, amplify):
    NewMatrix = [i * amplify for i in matrix]
    return NewMatrix


def readFile(pathways):
    file = open(pathways, 'r')
    i = 0
    currMatrix = []
    for line in file:
        currMatrix.append(line.split())

    row = len(currMatrix[0])
    col = len(currMatrix[:][0])

    SimiMatrix = currMatrix[0 : row - 1]
    MoleculeList = currMatrix[len(currMatrix) - 1]

    return SimiMatrix, MoleculeList

def getPathways(chron, drugName):
    return './StructureMaps/' + chron + '/' + drugName + '/' + 'Dice'

chron = 'OtherDrug'
# drugName = 'Antiulcer' 'Hypnotics' 'immunosupressive' 'Osteoporosis' 'SulfonamideSulfa'
drugName = 'Antiulcer'
pathways = getPathways(chron, drugName)


SimilarMatrix, MoleculeList = readFile(pathways)
currDiction = {}


G = nx.Graph()

def estabGraph(G, MoleculeList, SimilarMatrix):
    for key in MoleculeList:
        G.add_node(key)

    for i in range(len(MoleculeList)):
        source = MoleculeList[i]
        for j in range(len(MoleculeList)):
            sink = MoleculeList[j]
            distance = SimilarMatrix[i][j]
            # print (source, sink, distance)
            G.add_edge(source, sink, weight = distance)
    return G

G = estabGraph(G, MoleculeList, SimilarMatrix)

def DrewGraph(G):
    import matplotlib.pyplot as plt
    nx.draw(G, with_labels = True, font_weight = 'bold')
    plt.show()
DrewGraph(G)
