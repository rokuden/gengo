#!/usr/bin/python
# coding: UTF-8
moj1 = "paraparaparadise"
moj2 = "paragraph"
def n_gram(uni,n):
    return [uni[k:k+n] for k in range(len(uni)-n+1)]
print "X="    
print n_gram(moj1,2)
print "Y="
print n_gram(moj2,2)
X = n_gram(moj1,2)
Y = n_gram(moj2,2)
s = set(X)
print "和集合"
print s.union(Y)
print "差集合"
print s.difference(Y)
print "積集合"
print s.intersection(Y)
print "seがXに含まれる"
print ('se' in X)
print "seがYに含まれる"
print ('se' in Y)
 
