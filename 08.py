#!/usr/bin/python
# coding: UTF-8
def cipher():
	nuko = (u"A soccer team which has played a game was going home. Unfortunately, since the driver was exhausted, the car crushes on a black luxury car on their way. As opposed to Miura which protected the younger generation and took all the responsibility -- the conditions of the private settlement to which the owner of a car and gangster Tanioka were sentenced ...")
	for niko in nuko:
		noko = ord(niko)
		if 97 <= noko <= 122:
			neko = 219 - noko
			print chr(neko)
		else:
			print niko

if __name__ == "__main__":
    cipher()
