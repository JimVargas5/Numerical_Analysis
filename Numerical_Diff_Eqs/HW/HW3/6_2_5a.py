# Jim Vargas
# 6.2.5a

"""
    What does this code do
"""

import math
import numpy as np
import scipy.linalg as sp
from matplotlib import pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages
pdf=PdfPages('Output_6_2_5a.pdf')


def u(x):
    return math.pow(1 - x, 5/2) + 2*x
def f(x):
    return -(15/4)*math.pow(1 - x, 1/2)


x0=0
xmax=1
h_exponents=[i for i in range(1,9+1)]

alpha=1
beta=2

# currentMax_vector=[]
# for n in h_exponents:
#     h=2**(-1*n)
#     N=int(1/h) + 1
#     gridpoints=np.linspace(x0, xmax, N)

#     RHS=np.array([f(gridpoints[i]) for i in range(N)])
#     true_RHS=np.array([u(gridpoints[i]) for i in range(N)])

#     d=2*np.ones(N)
#     e=-1*np.ones(N-1)
#     A=np.diag(d) + np.diag(e, k=1) + np.diag(e, k=-1)
#     ab=np.zeros()

#     coeffs=sp.solve_banded((1,1),A,RHS)

#     error=max(abs(true_RHS - coeffs))
#     currentMax_vector.append(error)

# print(currentMax_vector)


m=4
# Create arrays and set values
ab = np.zeros((3,m))
b = 2*np.ones(m)
ab[0] = 9
ab[1] = 8
ab[2] = 7

# Fix end points
ab[0,1] = 2
ab[1,0] = 1
ab[1,-1] = 4
ab[2,-2] = 3
b[0] = 1
b[-1] = 3

print(ab)
print()


    





