# this part is for transfering the .mol file into
# string

#### ********* retrieve/generate smiles/mol
# file for list of the given molecules
from rdkit import Chem

# ***input: identifier name
# ***output: the SMILES string (CC(=O)C(C)O, for example)
def FindSmiles(identifier, pathway):
    m = Chem.MolFromMolFile(pathway + '/' + identifier)
    stringWithMolData = open(pathway + '/' + identifier, 'r').read()
    m = Chem.MolFromMolBlock(stringWithMolData)
    smileString = Chem.MolToSmiles(m)
    # print (smileString)
    return smileString


while True:
    chron = raw_input('Please enter the chronology, q for quit\n')
    if chron == 'q':
        break
    while True:
        classification = raw_input('Please enter the classification, q for quit\n')
        if classification == 'q':
            break

        currPath = './StructureMaps/' + chron + '/' + classification + '/' + classification
        # print (currPath)
        file = open(currPath, 'r')
        currMatabolites = []
        for line in file:
            currMatabolites.append(line.replace('\n', ''))
        file.close()
        # print (currMatabolites)
        MolString = {}
        for currID in currMatabolites:
            tempFilePath = './StructureMaps/' + chron + '/' + classification
            MolString[currID] = FindSmiles(currID, tempFilePath)
            print (currID, MolString[currID])
        file = open(tempFilePath + '/MoleculeString', 'w')
        for key in currMatabolites:
            file.write(key + ' : ' + MolString[key])
            file.write('\n')
        file.close()
        # print (MolString)





