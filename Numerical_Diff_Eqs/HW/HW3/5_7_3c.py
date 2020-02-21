# Jim Vargas
# 5.7.3c

""" 
    This code runs the Backward Euler method on the DE system
    y' = Ay
where A and y(t0) are given. A is a 2x2 matrix and y is in R^2.
This code outputs a pdf of plots comparing the approximated solution
and the true solution, which is
    y(t) = exp((t-t0)A) y(t0)
"""
# Python notes:
# Numpy exp of a matrix returns exp of each entry
# Scipy expm returns exp of matrix
# Scipy modules must be imported separately


import math
import numpy as np
import scipy.linalg as sp
from matplotlib import pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages
pdf=PdfPages('Output_3c.pdf')

alpha=-4
beta=6
t0=0
tmax=4*math.pi
y0=np.array([1,0])
A=np.array([
    [alpha, -1*beta],
    [beta, alpha]
])
I=np.identity(2)


def BackwardEuler(y,h):
    return np.dot(np.linalg.inv(I-h*A), y)

def TrueSol(t):
    return np.dot(
        sp.expm((t-t0)*A), y0
    ) # Mind your matrix exponential...


# Mind your indexing...
for h in [1/6, 1/8, 1/16, 1/32]:
    t=t0
    y=y0

    running_Horizontal=[y0[0]]
    running_Vertical=[y0[1]]
    running_TrueH=[TrueSol(t0)[0]]
    running_TrueV=[TrueSol(t0)[1]]

    while t<=tmax:
        y=BackwardEuler(y,h)
        t=t+h

        running_Horizontal.append(y[0])
        running_Vertical.append(y[1])
        running_TrueH.append(TrueSol(t)[0])
        running_TrueV.append(TrueSol(t)[1])

    fig=plt.figure()
    plt.plot(running_TrueH, running_TrueV, label='y(t_k)')
    plt.plot(running_Horizontal, running_Vertical, label='y_k')
    plt.title("Phase portrait, h="+str(h)+", t in [0,4pi].")
    plt.xlabel('Horizontal direction')
    plt.ylabel('Vertical direction')
    plt.legend(loc='best')

    plt.close()
    pdf.savefig(fig)


pdf.close()

# print("Numpy version\n", np.exp(A))
# print("Scipy version\n", sp.expm(A))

