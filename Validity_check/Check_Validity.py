
# This file is for calculating the similarity score
# by using different similarity matirces

from __future__ import print_function

# Tanimoto, Dice, Cosine, Sokal, Russel, Kulczynski, McConnaughey, and Tversky.
"""
a = 'NCC1OC(OC2C(CO)OC(OC3C(O)C(N)CC(N)C3OC3OC(CN)C(O)C(O)C3N)C2O)C(N)C(O)C1O'
b = 'NCC1OC(OC2C(CO)OC(OC3C(O)C(N)CC(N)C3OC3OC(CO)C(O)C(O)C3N)C2O)C(N)C(O)C1O'
c = 'NCC1OC(OC2C(N)CC(N)C(O)C2OC2OC(CO)C(O)C2O)C(N)C(O)C1O'
"""

currPathway = './StructureMaps/Antiinfectives/Aminoglycosides/MoleculeString'

def getString(pathway):
    file = open(pathway, 'r')
    targetString = {}
    for line in file:
        tempInfo = line.split(':')
        targetString[tempInfo[0].strip()] = tempInfo[1].replace('\n', '').strip()
    return targetString

abc = getString(currPathway)
# print (abc.keys())


from rdkit import Chem
from rdkit import DataStructs
from rdkit.Chem.Fingerprints import FingerprintMols

# score = DataStructs.FingerprintSimilarity(a, b, metric=DataStructs.DiceSimilarity)
# print (score)


# function input: a dictionary and the name of similarity matrix
# output : the metabolites and the similarity scores
def calculateSimilar(MolHashTable, similarityMatrices = 'Tanimoto'):
    metabolites = MolHashTable.keys()
    ms = []
    for key in metabolites:
        ms.append(Chem.MolFromSmiles(MolHashTable[key]))
    fps = [FingerprintMols.FingerprintMol(x) for x in ms]
    size = len(metabolites)
    Score = [([0] * (size)) for i in range(size)]
    for i in range(len(metabolites)):
        for j in range(len(fps)):
            if similarityMatrices == 'Tanimoto':
                Score[i][j] = DataStructs.FingerprintSimilarity(fps[i],fps[j])
            elif similarityMatrices == 'Dice':
                Score[i][j] = DataStructs.FingerprintSimilarity(fps[i], fps[j],\
                metric = DataStructs.DiceSimilarity)
            elif similarityMatrices == 'Cosine':
                Score[i][j] = DataStructs.FingerprintSimilarity(fps[i], fps[j],\
                metric = DataStructs.CosineSimilarity)
            else:
                print ('The similarity matrices are not available!\n')
    return metabolites, Score


def writeFile(pathway, matrices, metabolites):
    file = open(pathway, 'w')
    size = len(matrices)
    for i in range(size):
        for j in range(size):
            file.write(str(matrices[i][j]) + ' ')
        file.write(';\n')
    for key in metabolites:
        file.write(key + ' ')
    file.close()

pathway = './StructureMaps/Antiinfectives/Aminoglycosides/' + 'Dice'


# print (a, b, c)
metabolites, Score = calculateSimilar(abc, 'Dice')
writeFile(pathway, Score, metabolites)
# print (metabolites, '\n')
# print (np.array(Score))

print (len(Score))


def CalMatrices(chron, classification):
    path = './StructureMaps/' + chron + '/' + classification
    currDic = getString(path + '/MoleculeString')
    metabolites, Score = calculateSimilar(currDic, 'Dice')
    writeFile(path + '/Dice', Score, metabolites)
    metabolites, Score = calculateSimilar(currDic, 'Tanimoto')
    writeFile(path + '/Tanimoto', Score, metabolites)
    metabolites, Score = calculateSimilar(currDic, 'Cosine')
    writeFile(path + '/Cosine', Score, metabolites)

while True:
    chron = raw_input('Please entering the chronology!q for quit\n')
    if chron == 'q':
        break
    while True:
        classification = raw_input('Please entering the class of the drug! q for quit\n')
        if classification == 'q':
            break
        CalMatrices(chron, classification)




'''
l = 5
PSSM = [([0] * (l + 1)) for i in range(4)]
print(np.array(PSSM))
'''