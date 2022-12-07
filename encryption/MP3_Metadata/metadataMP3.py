#!/usr/bin/env python
import eyeD3

tag = eyeD3.Tag()
chemin = raw_input("Donnez le chemin du fichier mp3")
tag.link(chemin)
print (tag.getArtist())
print (tag.getAlbum())
print (tag.getTitle())
