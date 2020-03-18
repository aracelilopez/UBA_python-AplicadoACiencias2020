#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 28 09:13:49 2020

@author: araceli
"""

import random 
import numpy as np
import matplotlib.pyplot as plt

def generar_bosques(n):
    bosque=[]
    for i in range(0,n,1):
        bosque.append(0)
    return bosque
        
def suceso_aleatorio(p):
    r=random.random()
    result=False
    if r<p:
        result=True
    return result
    
    
def brotes(bosques,p):
    for i in range(len(bosques)):
        suceso=suceso_aleatorio(p)
        if suceso==True:
            bosques[i]=1
    return bosques

def cuantos(bosques,tipo_celda):
    count=bosques.count(tipo_celda)
    return count
        
def rayos(bosques,f):
    
    for i in range(len(bosques)):
        s=suceso_aleatorio(f)
        if bosques[i]==1 and s:
            bosques[i]=-1
    return bosques

def propagacion(bosques):
    
    for i in range(len(bosques)-1):
        if bosques[i]==-1 and bosques[i+1]==1:
            bosques[i+1]=-1
    for j in range(len(bosques)-1,0,-1):
        if bosques[j]==-1 and bosques[j-1]==1:
            bosques[j-1]=-1
    return bosques
    
def limpieza(bosques):
    for k in range(len(bosques)):
        if bosques[k]==-1:
            bosques[k]=0
    return bosques
    
def dinamica(n, n_rep, p, f):
    bosques=generar_bosques(n)
    contar=0
    for t in range(1,n_rep,1):
        bosques=brotes(bosques,p)
        bosques=rayos(bosques,f)
        bosques=propagacion(bosques)
        bosques=limpieza(bosques)
        contar=contar+cuantos(bosques,1)
    prom=(contar/n_rep)
    return prom
        
def grafico(n,n_rep):
    p=np.linspace(0,1,100)
    lista=[]
    for i in range(len(p)):
        lista.append(dinamica(n,n_rep,p[i],0.02))
    plt.plot(p, lista, "." )
    plt.show()    
            
    
  
        
#primerbosque=generar_bosques(10)
#probable=suceso_aleatorio(0.6)
#nuevosbrotes=brotes(primerbosque,0.6)
#cuantos1=cuantos(nuevosbrotes,0)
#rayos1=rayos(primerbosque,0.3)
b_1 = [1, 1, 1, -1, 0, 0, 0, -1, 1, 1]
p=propagacion(b_1)
#print(primerbosque)
#print(probable)
#print(nuevosbrotes)
#print(cuantos1)
#print(rayos1)       
print(dinamica(100, 10, 0.2, 0.05))
grafico(100, 10)