#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 26 09:33:45 2020

@author: araceli
"""

import random
import numpy as np

#random.random()
#random.randint(1, 10)
#lista = np.arange(7)
#print(lista)
#np.mean(lista)

def crearalbum(figustotal):
    i=0
    album=[]
    while i<figustotal:
        album.append(0)
        i=i+1
    return album

def hayalguno(l,e):
    i=0
    result=False
    while i<len(l): 
        if e==l[i]:
            result=True
        i=i+1
    return result

#contando elementos
    
def comprarunafigu(figustotal):
    figu=random.randint(1,figustotal)
    return figu    

def cuantasfigus(figustotal):
    alb=crearalbum(figustotal)
    ha=hayalguno(alb,0)
    figuscompradas=0
    while ha!=0:
        figuscompradas=figuscompradas+1
        comprarfigusnuevas=comprarunafigu(figustotal)
        ha=hayalguno(alb,0)
        alb[comprarfigusnuevas-1]=1 #indx de py
    return figuscompradas
    
def repetircinco(rep,figustotal):
    sumatotal=0
    for i in range(rep):
        cuantasfigus2=cuantasfigus(figustotal)
        sumatotal=sumatotal+cuantasfigus2
    return sumatotal/rep

def experimentar(figustotal,nrepes):
    lista=[]
    for i in range(nrepes):
        cuantasfigus2=cuantasfigus(figustotal)
        lista.append(cuantasfigus2)
    return np.mean(lista)

def crearpaquete(figus,cantidadenelpaquete):
    paquete=[]
    for i in range(cantidadenelpaquete):
        paquete.append(random.randint(1, figus))
    return paquete
#for i in range(figus_paquetes)
    #mifigus=comprarunafigu()
    #paquete.append(mifigus)
#return paquete
def albumlleno(album):
    count=0
    for i in range(len(album)):
        count=count+album[i]
    if count==len(album):
        return True
    else:
        return False
    
def cuantospaquetes(figus,cantidadenelpaquete):
    album=crearalbum(figus)
    count=0
    while albumlleno(album)==False:
        paq=crearpaquete(figus,cantidadenelpaquete)
        count=count+1
        for i in range(len(paq)):
            album[paq[i]-1]=1
    return count

def experimentarconpaquetes(figustotal,figuspaquete,nrepes):
    lista=[]
    for i in range(nrepes):
        lista.append(cuantospaquetes(figustotal,figuspaquete))
    return lista
        
completar=crearalbum(6)
print(completar)
l1=[1,0,2,5,8,7,7,5]
elementos=hayalguno(l1,9)
print(elementos)
comp=comprarunafigu(670)
print(comp)
compl=cuantasfigus(25)
print(compl)
repe=repetircinco(5,8)
print(repe)
#exp=experimentar(670,100)
#print(exp) tarda en procesar 
crearunpaquete=crearpaquete(670,5)
print(crearunpaquete)
print(cuantospaquetes(670,5))
