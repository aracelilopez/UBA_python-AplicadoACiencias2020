#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 21 20:00:21 2020

@author: ara
"""

import random 
import matplotlib.pyplot as plt

def una_jugada(p):
    r=random.random()
    result=False
    if r<p:
        result=True
    return result

def repetir_jugada(p,n_rep):
    jugadasganadas=[]
    for k in range(len(p)):
        jugadasganadas.append(0)
    for i in range(n_rep):
        for j in range(len(p)):
            jugar=una_jugada(p[j])
            if jugar==True:
                jugadasganadas[j]=jugadasganadas[j]+1
    return jugadasganadas

def juan_se_arruina(j,m,p):
    while j>0 and m>0:
        jugar=una_jugada(p)
        if jugar==True:
            m=m-1
            j=j+1
        else:
            m=m+1
            j=j-1
    if m > 0:
        return True
    else:
        return False


def estimacion_juan_gana(j,m,p,n_rep):
    count=0
    for i in range(n_rep):    
        if juan_se_arruina(j,m,p)==False:
            count = count + 1
    return count/n_rep


def grafico(p,m):
    plt.title("Propocion que Juan Gana", fontsize= 16)
    plt.xlabel("Juan gana", fontsize = 12, color= "green")
    plt.ylabel("Cantidad de monedad de j",fontsize=12, color = "green")
    listaderesultados=[]
    for j in range(m):
        listaderesultados.append(estimacion_juan_gana(j,m,p,1000))
    plt.plot(range(m), listaderesultados, "." )
    plt.show()    
        
        
print(una_jugada(1/6))
#p=[0.2, 0.5, 0.8, 1]
#print(repetir_jugada(p,1000))
print(juan_se_arruina(13,5,1/6))
print(estimacion_juan_gana(3,5,1/3,1000))
grafico(0.5,50)