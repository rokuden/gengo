#!/usr/bin/python
# coding: UTF-8
import random
nuko = (u"I couldn't believe that I could actually understand what I was reading : the phenomenal power of the human mind .")
neko = nuko.split(" ")
for niko in neko:
	if len(niko) <= 4:
		print niko
	else:
		noko = niko[1:-1]
		ran = list(noko)
		random.shuffle(ran)
		print niko[0]
		print ran
		print niko[-1]
