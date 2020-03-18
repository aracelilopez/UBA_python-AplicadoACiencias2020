#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
Created on Fri Feb 21 09:10:23 2020

@author: Araceli 
'''

import random 

def generarmazos(n):
    j=0
    m=[]
    while j<n:
        i=1
        while i<14:
            k=0 
            while k<4:
                m.append(i)
                k= k+1
            i=i+1
        j=j+1
    random.shuffle(m)
    return m

def jugar(m):
    suma=0
    while suma<21 and len(m)>0:
        suma=suma+m.pop(0)
    return suma 

def jugarvarios(m,n):
    resultados=[]
    i=0
    while i<n:
        resultados.append(jugar(m))
        i+=1
    return resultados

def verquiengano(resultados):
    lista=[]
    j=0
    while j<len(resultados):
        if resultados[j]==21:
            lista.append(1)
        else:
            lista.append(0)
        j+=1
    return lista
    
def experimentar(rep,n):
    p=0
    lista=[]
    while p<n:
        lista.append(0)
        p+=1
    if rep>0:
        i=0
        m=generarmazos(n)
        while i<rep:
            r=jugarvarios(m,n)
            r1=verquiengano(r)
            j=0
            while j<len(r1):
                lista[j]=lista[j]+r1[j]
                j+=1
            i+=1
        return lista
    else:
        print('Error')
        
mazonuevo=generarmazos(1)
print(mazonuevo)
print(len(mazonuevo))
j=jugar(mazonuevo)
print(j)
print(len(mazonuevo))
m=jugarvarios(mazonuevo,5)
print(m)
print(verquiengano(m))

p=experimentar(3,10)

print(p)