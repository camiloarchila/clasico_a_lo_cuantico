"""
Created on Sat Sep 19 10:18:34 2020

@author: Camilo
"""
import matplotlib.pyplot as plot
import numpy as np

def canicas(mat,vect,clicks):
    res=[]
    k=0
    while k != clicks:
        vect = mat*vect
        k+=1
    for i in range(len(vect)):
        res = res + [int(vect[i])]
        for i in range(len(res)):
            if res[i]==1:
                res[i]= ["True"]
            else:
                res[i]=["False"]
    return res

def clasicoproba(mat,vec,clicks):
    k=0
    res = []
    while k != clicks:
        vec = mat*vec
        k+=1
    for i in range(len(vec)):
        res = res + [[float(vec[i])]]
    return res

def multiplerendija(mat,clicks):
    k=0
    mat1 = mat[:]
    while k!= clicks:
        for k in range(clicks):
            mat = mat*mat1
        k+=1
    row, column = len(mat), len(mat[0])
    for i in range(row):
        nRow = []
        for j in range(column):
            nRow.append([(modulo(mat[i][j]) ** 2), 0])
        mat[i] = nRow
    return mat
        
def modulo (num):
    ans = (num[0] ** 2 + num[1] ** 2) ** (1/2)
    return ans

def grafico(vector):
    data =len(vector)
    x = np.array([x for x in range(data)])
    y = np.array([round(vector[x][0] * 100, 2) for x in range(data)])

    plot.bar(x, y, color='g', align='center')
    plot.title('Probabilidad del vector')
    plot.show()
    
