#!/usr/bin/env python2.7

import glob
import csv  
import os

# get absolute parent folder path for all csv
parentFolderPath = input("chemin absolu du dossier parent dans lequel se trouve tous les csv (non splité) \n")

# create lists
listTGI = []
listSGI = []

def newCSV(listGI, filePath):
    with open(filePath, 'w', newline='') as csvfile:
        spamwriter = csv.writer(csvfile, delimiter='\r', lineterminator='\n', quotechar=';', quoting=csv.QUOTE_MINIMAL)
        for it in listGI:
            spamwriter.writerow([it,""])

# Get all csv in this path 
allCSV = glob.glob(parentFolderPath + "/*.csv")
for aCSV in allCSV: # For each csv
    # Read the csv
    with open(aCSV, newline='') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
        
        for row in spamreader:
            line = (', '.join(row)).split(';')[0] # Split all lines to keep only TGI and SGI
            
            if(line and line[0] == 'T'): # make two list for SGI & TGI
                listTGI.append(line)
            if(line and line[0] == 'S'):
                listSGI.append(line)

        # get the name of the CSV
        csvfilesize = len((csvfile.name).split("\\"))
        aCSVName = (csvfile.name).split("\\")[csvfilesize - 1].split(".")[0]
        
        # Create two new CSV and write theses lists
        newCSV(listTGI, parentFolderPath + "\\" + aCSVName + " - TGI.csv")
        newCSV(listSGI, parentFolderPath + "\\" + aCSVName + " - SGI.csv")

        # Close the CSV
        csvfile.close()

        # Remove the CSV
        os.remove(csvfile.name)