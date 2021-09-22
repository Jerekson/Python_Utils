#!/usr/bin/env python2.7

import glob

# get absolute parent folder path for all csv
parentFolderPath = input("chemin absolu du dossier parent dans lequel se trouve tous les csv \n");

# Get all csv in this path 
# All files ending with .txt
print(glob.glob(parentFolderPath + "/*.txt")) 

#fichier = open('fichier1.txt','r') #Mode de lecture

#Fermeture du fichier
# fichier.close()

print("test")
