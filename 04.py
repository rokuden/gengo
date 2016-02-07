#!/usr/bin/python
# coding: UTF-8
moj = "Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can."
mojs = moj.split(" ") 
for mojh in mojs:
	if mojh == "Hi" or mojh == "Boron" or mojh == "Could" or mojh == "Not" or mojh == "Oxidize" or mojh == "Fluorine" or mojh == "Peace" or mojh == "Security" or mojh == "King":
		print mojh[0:1]
	else:
		print mojh[0:2]
