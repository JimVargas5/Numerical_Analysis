# Jim Vargas
# 5.4.5b

import math
from tabulate import tabulate

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
    return y + h*((1/6)*K1 + (2/6)*K2 + (1/6)*K3)

bigTable=[] # 0 to 2
bigTable.append(['h', 'E_max','Ratio'])

for i in range(2):
    bigTable.append(['-----','lambda: '+str(Lambda[i]),'-----'])
    for n in range(2,11+1):
        h=2**(-1*n)

        y=y0
        t=t0
        currentMaxVector=[0 for k in range(2+1)]
        currentMaxVector[0]=h
        while t<math.pi:
            temp=abs(actualFunction(t)-nextStep(t,y,h,i))
            if temp > currentMaxVector[1]:
                currentMaxVector[1]=temp


            y=nextStep(t,y,h,i)
            t=t+h
        bigTable.append(currentMaxVector)

# bigTable rows 0,1,1+(11-2) are text
for row in range(3,len(bigTable)):
    if row !=12 and row !=13: # skip first ratio
        bigTable[row][2]=bigTable[row][1] / bigTable[row-1][1]


with open("Output_5b.txt", "w") as text_file:
    print(tabulate(bigTable), file=text_file)




