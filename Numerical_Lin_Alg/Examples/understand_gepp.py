# Jim Vargas
# Trying to understand GEPP Outer Product Form algorithm

import numpy as np

A=np.array([
    [1,2,3],
    [6,5,4],
    [7,8,9]
])

p=np.array([1,2,3])

for k in range(0,3):
    q=np.argmax(A[k,:])
    if A[k][q] !=0:
        if q>k:
            A[(k,q),:]=A[(q,k),:]
            p[[k,q]]=p[[q,k]]
        ii=np.linspace(k+1,3)
        A[[ii,k]]=A[[ii,k]]/A[k,k]
        A[ii,ii]=A[ii,ii] - np.matmul(A[ii,k], A[k,ii])
    print(A)

