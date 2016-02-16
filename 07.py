#!/usr/bin/python
# coding: UTF-8
def test(x,y,z):

	if x == 0:
		x = 'x'
	elif x == 1:
		x = '12'
	if y == 0:
		y = 'y'
	elif y == 1:
		y = '気温'
	if z == 0:
		z = 'z'
	elif z == 1:
		z = '22.4'
    	print x + '時の' + y + 'は' + z

if __name__ == "__main__":
    test(0,0,0)
