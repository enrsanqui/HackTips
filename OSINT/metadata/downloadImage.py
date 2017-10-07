#! /usr/bin/env python
#-*- coding: utf-8 -*-
from PIL import Image
from urllib import urlopen
from StringIO import StringIO
import os
 
URL = 'http://images.performgroup.com/di/library/goal_es/74/b8/cristiano-ronaldo-real-madrid-granada-la-liga-ballon-dor_15fszo66dk5op1rygrakkp8g8z.jpg?t=2027796681'
data = urlopen(URL).read() # descarga y almacena la imagen en una cadena
file = StringIO(data) # trata la cadena como un fichero
img = Image.open(file) # lee el fichero y devuelve la imagen
print img.size # informa del tamaño
print img.format # formato
print img.info # meta información
img_rot = img.rotate(90) # rotar la imagen 90 grados
directorio = os.getcwd()
print directorio
img_rot.save(directorio + "/mi_imagen." + img.format) # y salvar la imagen en local
print "imagen salvada"