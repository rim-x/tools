#!/usr/bin/env python
#coding=iso-8859-15
#Password Generator
#-------------------
import random as r
al = str()
sy = str()
be = str()

#Creates 3 Random lower case Characters and 3 Random Upper case #Characters  
def alp1():
	b = ['A','B','C','D','E','F',
		'G','H','I','J','K','L',
		'M','N','O','P','Q','R',
		'S','T','U','V','W','X',
		'Y','Z']
	for i in range(0,3):
		global be
		z = r.randint(0, 25)
		be += b[z]
	return be

def alp():
	a = ['a','b','c','d','e','f','g',
		'h','i','j','k','l','m','n',
		'o','p','q','r','s','t','u',
		'v','w','x','y','z']
	for i in range(0,3):
		global al
		x = r.randint(0,25)
		al += a[x]
	return al

def sym():
	s = ['$','§','%','&','/','*','#','+']

	for i in range(0, 3):
		global sy
		y = r.randint(0,7)
		sy += s[y]
	return sy

#Two Random Three Digget Numbers
nr = r.randint(100,999)
nr1 = r.randint(100,999)

#The Password is merging and printed to the commandline
puffer = alp() + str(nr) + alp1() +  str(nr1) + sym()
print (puffer)

#The Password is saved into pwgen.txt
file = open('pwgen.txt','a')
file.write(puffer)
file.write('\n')
file.close()



