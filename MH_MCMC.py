# -*- coding: utf-8 -*-
"""
Created on Thu Apr  4 04:13:30 2024

@author: HP
"""

import math
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def cosh(x):
    return (math.exp(x)+math.exp(-x))/2

def temp(q,x):
    return 100*((cosh(q*(100-x)*(1/1000)))/cosh(q*0.1))
def gauss(s,g):
    u=-1*(s/(2*g*g))
    k=1/((math.sqrt(2*math.pi))*g)
    return k*(math.exp(u))

data=pd.read_csv("D:\\new_downloads\\AT_3.csv")
n=len(data)
q=[]
q.append(12)
rv=[[0.001213,0.8989,0.5788],[0.499629,0.282693,0.730594],[0.108501,0.386183,0.769105],[0.557434,0.799824,0.45679],[0.09264,0.589628,0.332164],[0.76267,0.696237,0.170288],[0.032722,0.299315,0.308614],[0.352862,0.5741,0.265836],[0.941875,0.24,0.655595],[0.199044,0.93655,0.888098],[0.339548,0.543258,0.624006],[0.155062,0.582447,0.858532],[0.751033,0.239493,0.535597],[0.634536,0.199621,0.65],[0.227241,0.191479,0.406443],[0.721023,0.222878,0.072814],[0.789616,0.052303,0.106694],[0.760869,0.120791,0.27738],[0.80548,0.8265,0.29453],[0.585186,0.986111,0.344882]]
i=0
j=0
likepast=1
likepresent=1

y=0
likelihood=[]
while len(q)<6:
    
    if rv[j][1]>0.5:
        y=q[i]+(1.2)*rv[j][0]
    else:
        y=q[i]-(1.2)*rv[j][0]
    
    if y>=0 :
        s=0
        for k in range(0,n):
            T_=temp(y,data.iloc[k]['Distance'])            
            T=data.iloc[k]['Temp']
            s=s+(T-T_)**2
        likel=gauss(s,0.707)
        

        likepresent=likel
        if(len(q)>1):
            A=min(1,likepresent/likepast)
            
            if (A>rv[j][2]):
                q.append(y)
                i=i+1
                likelihood.append(likel)
                
                likepast=likel
        elif(len(q)==1):
            q.append(y)
            i=i+1
            likelihood.append(likel)
            likepast=likel
        j=j+1
        
print(q)
norm=0
ppdf=[]
for z in likelihood:
    norm=norm+z
for z in likelihood:
    ppdf.append(z/norm)

print(ppdf)
mean=0
for z in range(0,5):
    mean=mean+q[z+1]*ppdf[z]
    
print(mean)



    
    
    






   

    