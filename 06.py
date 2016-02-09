#!/usr/bin/python
# coding: UTF-8
moj1 = "paraparaparadise"
moj2 = "paragraph2"
def n_gram(uni,n):
    return [uni[k:k+n] for k in range(len(uni)-n+1)]
print n_gram(moj1,2)
print n_gram(moj2,2)
