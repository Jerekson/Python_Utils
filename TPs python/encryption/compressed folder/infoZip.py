#!/usr/bin/env python
import zipfile

#Recuperation du zip
z = zipfile.ZipFile("/root/Documents/Forensics/J3/test.zip", "r")
#z = zipfile.ZipFile("test.zip", "r")

#retours des infos
for nom in z.namelist():
	print(f'le fichier {nom}')
	nb_octets = z.read(nom)
	print('content', len(nb_octets), 'octets')
