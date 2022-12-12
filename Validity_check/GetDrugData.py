# Haotian Zhang
# haotian.zhang@tufts.edu
# plt

import urllib.request
import os

# ************** Part *************
# get maps


def getMap(mapName, chronology, Classification):
    dataBase = 'pathway'
    url = 'http://rest.kegg.jp/get/' + dataBase + ':' + mapName
    # print (url)
    req = urllib.request.Request(url)
    response = urllib.request.urlopen(req)
    thePage = response.read().decode("utf-8")
    # print (thePage)
    startIndex = thePage.find('COMPOUND')
    endIndex = thePage.find('REFERENCE')
    temp = thePage[startIndex + 8 : endIndex].split()
    # print (thePage)
    DrugList = []
    for key in temp:
        if key.startswith('D') or key.startswith('C'):
            if len(key) == 6:
                DrugList.append(key)
    # print (DrugList)

    # chronology = 'NervousSystem'
    # Classification = 'Antipsychotics'
    targetPathway = './StructureMaps/' + chronology + '/' + Classification

    if not os.path.exists(targetPathway):
        os.makedirs(targetPathway)

    local_cache = './StructureMaps/' + chronology + '/' + Classification + '/' + Classification
    file = open(local_cache, 'w')
    for key in DrugList:
        file.write(key)
        file.write('\n')

# getMap('map07029', 'NervousSystem', 'AntipsyPheno')


getEnd = False
while getEnd == False:
    mapID = input('Please enter mapID, q for quit\n')
    if mapID == 'q':
        break
    chron = input('Please enter chronology of that ID\n')
    classification = input('Please enter the class of that drug\n')
    getMap(mapID, chron, classification)

def getMolFile(identifier, cache_file_path):

    url = "http://www.kegg.jp/dbget-bin/www_bget?-f+m+compound+" + identifier
    req = urllib.request.Request(url)
    response = urllib.request.urlopen(req)
    thePage = response.read().decode("utf-8")

    if not os.path.exists(cache_file_path):
        os.makedirs(cache_file_path)
    cache_file_path = cache_file_path + '/' + identifier
    # -*- coding: UTF-8 -*-
    with open(cache_file_path, 'w') as fw:
        fw.write(thePage)

'''
classification = 'Aminoglycosides'
currPath = './StructureMaps/Antiinfectives/' + classification
file = open(currPath + '/' + classification, 'r')
tempDrugList = []
for line in file:
    tempDrugList.append(line.replace('\n', ''))
print(tempDrugList)


'''
while True:
    chron = input('Please enter the chronology, q for quit\n')
    if chron == 'q':
        break
    while True:
        classification = input('Please enter the classification, q for quit\n')
        if classification == 'q':
            break
        currPath = './StructureMaps/' + chron + '/' + classification
        # while True:
        file = open(currPath + '/' + classification, 'r')
        tempDrugList = []
        for line in file:
            tempDrugList.append(line.replace('\n', ''))
        # print(tempDrugList)
        for key in tempDrugList:
            getMolFile(key, currPath)




'''
database_name = 'dr'
identifier = 'D01478'
url = 'http://rest.kegg.jp/get/' + database_name + ':' + identifier
# print (url)

req = urllib.request.Request(url)
response = urllib.request.urlopen(req)
thePage = response.read().decode("utf-8")
# print (thePage)
data = thePage
start_index = data.find('NAME')
end_index1 = data.find('PRODUCT')
end_index2 = data.find('FORMULA')
if end_index1 < end_index2 and end_index1 != -1:
    end_index = end_index1
else:
    end_index = end_index2

print (end_index2, end_index, end_index1)
tempList = data[start_index + 5 : end_index].split()
# print (tempList)
name = ''
for key in tempList:
    name += key

# print (name)

cache_file_path = './StructureMaps/Antiinfectives/' + identifier
with open(cache_file_path, 'w') as fw:
    fw.write(thePage)
'''