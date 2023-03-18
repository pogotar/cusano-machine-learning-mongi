# -*- coding: utf-8 -*-
"""
Created on Fri Mar 17 11:14:11 2023

@author: pmong
"""

import numpy as np

v = np.array([1, 2, 3.14, 0., 5., 19., 10.])


print(v.size) # mi dice quanto è grande
print(v[0])
print(v[-1])
print(v[2:4])
print(v[:4])

v[3] = 1.1223344

w = np.array([1,2,3,4,5,-6,-7])

# element per element
print("\n")
print([v+w])
print([v-w])
print([v*w])
print([v/w])

# 
print("\n", v.sum()) # summation of all the elements
print(v.mean())
print(v.min())
print(v.max())
print(v.var()) # variance
print(v.std()) # standard deviation

#
print("\n", np.cos(v)) # cos of every element
print(np.exp(v))
print(np.log(v))
print(np.sqrt(v))

#  product of vectors (scalar product)
print("\n", np.dot(v, w)) 
print(v @ w)
print((v*w).sum())

# matrices
m = np.array([[1,2,3,4], [5,6,7,8],[9,10,11,12]])
print(m,"\n", m.size, "\n", m.shape, "\n", m.ndim) # shape returns the touple
print("\n",v.shape, v.ndim) # ndim mi dice la dimensione
print("\n", m[0,0])
print(m[1,3])
print(m[0:2,0:2])
print(m[1,:])
print(m[:,1])

#
print("\n")
k = np.array([[1,1,1,1], [2,2,2,2],[3,3,3,3]])
print(m+k) # elemento per elemento
print(m.sum())
print(m.sum(0)) # ho sommato le riighe tra di loro
print(m.sum(1)) # ho sommato le colonne tra di loro
ciao =  m.sum(0, keepdims = True)
print("\n", m.sum(0, keepdims = True)) # fa la stessa cosa ma ritorna la matrice

print(np.cos(m))

################################## broadcasting
print("\n", m+1) # sommo 1 a tutte le posizioni
print(m*10) # sommo 1 a tutte le posizioni
n = np.array([[10,20,30,40]])
# m.shape = 3,4      n.shape = 1,4
print("\n", m+n)

p = np.array([[7], [11],[13]])
print(p.shape)
print(m+p)
print(n+p) # sembra che finchè della tuple hanno un numero in comune posso fare operazioni

##### broadcasting matrices and vectors
v= np.array([10, 20, 30, 40])
print(m.shape)
print(v.shape)
print(m+v)
w = np.array([10,20,30]) # 1*3  and not broadcastable to a 3*4
print(m.shape)
print(w.shape)
# print(m+w) da errore

###############################
print(m.T) # fa il trasposto
k = np.array([[10, 20],[30, 40], [59, 60],[70,80]])
print(m.shape)
print(k.shape)
print(v.shape)
print(m@k)
print(m@v)
print(w@m)
# a traspose of a vector returns the same vector, vector are just vectors

#############
print(np.zeros(4)) # return a zero vector
print(np.zeros((3,4))) # returns the matrix

print(np.ones((3,4))) # returns the matrix
print(np.empty((3,4))) # returns the matrix   allocates spaces
print(np.random.rand(3,4)) # qui fa proprio numeri randomici, uniform distribution
print(np.random.randn(3,4))  # qui fa proprio numeri randomici, normal distribution

a = np.arange(12) 
print("\n", a)
a = a.reshape(3, 4) # modifica la forma
print(a)