#!/usr/bin/python
# coding: UTF-8
str1 = u"パトカー"
str2 = u"タクシー"
str3 = min(len(str1), len(str2))
for i in range(str3):
	print str1[i],str2[i],
