# -*- coding: utf-8 -*-
"""
Created on Mon Sep 27 14:07:14 2021

@author: lenovo
"""

#1.Flowchart
def Print_values(a,b,c):
    if a>b:
        if b>c:
            print(a,b,c)
        elif a>c:
            print(a,c,b)
        else:
            print(c,a,b)
    elif b>c:
        if a>c:
            print(b,a,c)
        else:
            print(b,c,a)
    else:
        print (c,b,a)
Print_values(4,5,6)
             
       
###2.Matrix multiplication

#2.1生成矩阵
#参考https://www.jianshu.com/p/85ec63259c4e-np.random用法
#numpy是python进行高效数据处理的模块
import numpy as np#导入numpy模块并将其简写成np
#np.random.randint(low,high=(),size=,dtype=)
#其中，low和high 是指随机生产整数的范围
#size是指array的维度，dtype是指数据类型,默认为int型
M1=np.random.randint(low=0,high=50,size=(5,10))
M2=np.random.randint(low=0,high=50,size=(10,5))
M3=np.dot(M1,M2)

#2.2定义一个矩阵相乘的函数
def Matrix_multip():
    M4=np.zeros((5,5))
    for i in range(5):
        n=0
        while n < 5:
            for j in range(10):
                M4[i,n]=M4[i,n]+M1[i,j]*M2[j,n]
            n=n+1
    print(M4)
Matrix_multip()


###3定义 Pascal_triangle 
def Pascal_triangle(K):
    k=int(K)
    a=[]
    if k==0:
        a.append([1])
    elif k==1:
        a.append([1,1])
    k-=2
    a=[[1],[1,1]]
    while k>0:
        b=[1]
        for i in range(len(a)-1):
            b.append(a[-1][i]+a[-1][i+1])
        b.append(1)
        k-=1
        a.append(b)
    return a

m=Pascal_triangle(100)
n=m=Pascal_triangle(200)


###4 Add or double

import random
def  Least_moves():
    x=random.randint(0,100)
    if x>1:
        if x%2==0:
            a=x/2
        else:
            a=(x+1)/2
    else:
        a=0
    return(a)
Least_moves()

#5 Dynamic programming



          
