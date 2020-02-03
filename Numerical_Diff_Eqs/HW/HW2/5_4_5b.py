# Jim Vargas
# 5.4.5b

""" This code tests a third order Runge-Kutta method on the IVP
    y'=lambda(y-cos(t))-sin(t), y(0)=1.
The solution is y(t)=cos(t). It outputs convergence history to 
a .txt file and graphs to a .pdf file. 
"""

import math
from tabulate import tabulate
from matplotlib import pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages
pdf = PdfPages('Output_5b.pdf')

t0=0
y0=1
Lambda=[-8,-30]

def f(t,y,i):
    return Lambda[i]*(y - math.cos(t)) - math.sin(t)
def actualFunction(t):
    return math.cos(t)

def nextStep(t,y,h,i):
    K1=f(t,y,i)
    K2=f(t + (1/2)*h, y + h*(1/2)*K1,i)
    K3=f(t + h, y + h*(-1*K1 + 2*K2),i)
    return y + h*((1/6)*K1 + (2/3)*K2 + (1/6)*K3)

bigTable=[] # Indeces 0 to 2
bigTable.append(['h', 'E_max','Ratio'])



for i in range(2): # Both lambdas
    bigTable.append(['-----','lambda: '+str(Lambda[i]),'-----'])
    for n in range(2,11+1):
        running_yk=[y0]
        running_Actual=[actualFunction(t0)]
        running_Errors=[actualFunction(t0)-y0]
        running_AbsoluteErrors=[abs(actualFunction(t0)-y0)]
        running_t=[t0]

        h=2**(-1*n)

        y=y0
        t=t0
        currentMaxVector=[0 for k in range(2+1)] # Represents a row in bigTable
        currentMaxVector[0]="2^(-"+str(n)+")"
        while t<=math.pi:
            y_next=nextStep(t,y,h,i)
            temp=abs(actualFunction(t)-y)
            if temp > currentMaxVector[1]:
                currentMaxVector[1]=temp

            y=y_next
            t=t+h

            running_yk.append(y)
            running_Actual.append(actualFunction(t))
            running_AbsoluteErrors.append(temp)
            running_t.append(t)

        fig=plt.figure()
        plt.subplot(1,2,1)
        plt.plot(running_t,running_Actual, label='y(t_k)')
        plt.plot(running_t,running_yk, label='y_k')
        plt.title("Lambda="+str(Lambda[i])+", h=2^(-"+str(n)+")")
        plt.legend(loc='best')

        plt.subplot(1,2,2)
        plt.plot(running_t,running_AbsoluteErrors, label='Absolute Error')
        plt.title("Absolute Errors")
        plt.close()
        pdf.savefig(fig)

        bigTable.append(currentMaxVector)

# bigTable rows [0,1,1+(11-1)] are text
# Ratio: E_max(h)/E_max(h/2)
for row in range(3,len(bigTable)):
    if row !=12 and row !=13: # Skip rows 2 and 13 as well
        bigTable[row][2]=(bigTable[row][1] / bigTable[row-1][1]) ** (-1)


with open("Output_5b.txt", "w") as text_file:
    print(tabulate(bigTable), file=text_file)


pdf.close()

