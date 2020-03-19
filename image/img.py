#!/usr/bin/env python
#coding=iso-8859-15
#Image resizing Programm
import PIL
from PIL import Image
import os
from os import listdir
from os.path import isfile, join

#write names of resized images in quotes
#or use drag and drop
#----------------------------------------

#function to convert one picture
def one():
	convert = input('enter name of picture: ')
	x = input('enter width: ')
	y = input('enter height: ')
	newsize = (x,y)
	name = input('enter name of resized image: ')
	os.chdir('images')
	os.chdir('resized')
	img = Image.open(convert)
	fil = img.resize(newsize)
	fil.save(name +'.png', 'PNG')
#---------------------------------------------------------------
dec = input ('Image_Resizer\n-------------\nset name of resized files in quotes\n\n1. resize one picture\n\n')

if dec is 1:
	one()
else:
	print('Invalid')

