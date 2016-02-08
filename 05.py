#!/usr/bin/python
# coding: UTF-8
moj = "I am an NLPer"
def n_gram(uni,n):
    return [uni[k:k+n] for k in range(len(uni)-n+1)]
print n_gram(moj,2)
mojs = moj.split(" ")
for mojh in mojs:
	print n_gram(mojh,2)
