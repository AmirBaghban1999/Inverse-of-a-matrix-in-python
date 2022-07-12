# -*- coding: utf-8 -*-
"""
Created on Sun Dec 13 21:51:26 2020

@author: Amir
"""
import numpy as np
np.set_printoptions(suppress=True)




    

def inversematrix(a):
    counter=[]
    n=len(a[0])
    inverse=np.empty((n,n),dtype=float)
    c=np.empty((n,2*n),dtype=float)
    b=np.empty((n,n+n),dtype=float)
    identity=np.empty((n,n),dtype=float)
    for i in range(n):
        for j in range(n):
            if i==j:                                 
                identity[i,j]=1
            else:
                identity[i,j]=0
    for k in range(n):
        pp=list(a[k])
        for t in range(n):
            pp.append(identity[k,t])
        b[k]=np.array(pp)

    for j in range(n):
        for i in range(n):
            if b[j,i]!=0:
                b[j]=(1/b[j][i])*b[j]
                counter.append((j,i))
                break
        for t in range(n):
            if t!=j and b[t,i]!=0:
                b[t]=b[t]-b[t][i]*b[j]
                
    for k in counter:
        c[k[0]]=b[k[1]]
    for i in range(n):
        inverse[i]=c[i,n:]
    
    
        
    return inverse

a=np.array([[0,3,1,0],[8,9,1,1],
            [3,2,10,0],[0,0,0,1]],
        dtype=float)

print(inversematrix(a))