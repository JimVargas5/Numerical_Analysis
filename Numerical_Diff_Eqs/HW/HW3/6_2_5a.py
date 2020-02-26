# Jim Vargas
# 6.2.5a

"""
    What does this code do
"""

import math
from tabulate import tabulate
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


currentMaxVector=[]
for n in h_exponents:
    h=2**(-1*n)
    N=int(1/h) + 1
    gridpoints=np.linspace(x0, xmax, N)

    # b in Ax=b
    RHS=np.array(
        [(h*h) * f(gridpoints[i]) for i in range(N)]
    )
    RHS[0]=RHS[0] + alpha
    RHS[N-1]=RHS[N-1] + beta

    # A in Ax=b
    d=2*np.ones(N)
    e=-1*np.ones(N-1)
    A=np.diag(d) + np.diag(e, k=1) + np.diag(e, k=-1)
    # A must be in diagonal banded form for solve_banded.
    # Prepend zero to upper diag, append zero to lower diag
    A_banded=np.array(  np.vstack(
        (np.insert(e,0,0), d, np.insert(e,N-1,0))
    ))

    # x in Ax=b
    coeffs=sp.solve_banded((1,1),A_banded,RHS)

    true_coeffs=np.array([u(gridpoints[i]) for i in range(N)])
    #print(coeffs,'\n',true_coeffs)

    error=max(abs(true_coeffs - coeffs))
    currentMaxVector.append(error)




bigTable=[["h", "Max error\n |u(x_j)-U_j|", "ratio"]]
for idx in range(len(h_exponents)):
    if idx==0:
        temp_row=["2^(-1*"+str(h_exponents[idx])+")",currentMaxVector[idx],0]
    else:
        temp_row=["2^(-1*"+str(h_exponents[idx])+")",
            currentMaxVector[idx],currentMaxVector[idx-1]/currentMaxVector[idx]
        ]
    bigTable.append(temp_row)
with open("Output_6_2_5a.txt", "w") as text_file:
    print(tabulate(bigTable), file=text_file)



    





