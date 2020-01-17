# Jim Vargas
# 5.2.2
# part B)
import math

t0=0
y0=1
Lambda=-30

def f(t,y):
    return Lambda*(y - math.cos(t)) - math.sin(t)
def actualFunction(t):
    return math.cos(t)


# The explicit methods
def ForwardEuler(t,y,h):
    return y + h*f(t,y)
def Midpoint(t,y,h):
    y_plusHalf= y + (h/2)*f(t,y)
    t_plusHalf= t + (h/2)
    return y + h*f(t_plusHalf,y_plusHalf)
def TPC(t,y,h):
    y_bar=y + h*f(t,y)
    return y + (h/2)*(f(t,y) + f(t+h,y_bar))

# Implicit methods made explicit for this problem
def BackwardEuler(t,y,h):
    numerator= y - h*Lambda*math.cos(t+h) - h*math.sin(t+h)
    denominator= 1 - h*Lambda
    return numerator/denominator
def Trapezoid(t,y,h):
    numerator= y + (h/2)*f(t,y) - (h*Lambda/2)*math.cos(t+h) - (h/2)*math.sin(t+h)
    denominator= 1 - h*Lambda/2
    return numerator/denominator


bigTable=[] # 0 to 5
bigTable.append(['h','FE','M','TPC','BE','T'])

for n in range(2,8):
    h=2**(-1*n)
    t=t0

    y_FE=y0
    y_M=y0
    y_TPC=y0
    y_BE=y0
    y_T=y0

    currentMaxVector=[0 for i in range(5+1)]
    currentMaxVector[0]=h

    # Not clear how many steps to get to pi are needed
    while t<=math.pi:
        if abs(actualFunction(t) - ForwardEuler(t,y_FE,h)) > currentMaxVector[1]:
            currentMaxVector[1]=abs(actualFunction(t) - ForwardEuler(t,y_FE,h))

        if abs(actualFunction(t) - Midpoint(t,y_M,h)) > currentMaxVector[2]:
            currentMaxVector[2]=abs(actualFunction(t) - Midpoint(t,y_M,h))

        if abs(actualFunction(t) - TPC(t,y_TPC,h)) > currentMaxVector[3]:
            currentMaxVector[3]=abs(actualFunction(t) - TPC(t,y_TPC,h))

        if abs(actualFunction(t) - BackwardEuler(t,y_BE,h)) > currentMaxVector[4]:
            currentMaxVector[4]=abs(actualFunction(t) - BackwardEuler(t,y_BE,h))

        if abs(actualFunction(t) - Trapezoid(t,y_T,h)) > currentMaxVector[5]:
            currentMaxVector[5]=abs(actualFunction(t) - Trapezoid(t,y_T,h))

        y_FE=ForwardEuler(t,y_FE,h)
        y_M=Midpoint(t,y_M,h)
        y_TPC=TPC(t,y_TPC,h)
        y_BE=BackwardEuler(t,y_BE,h)
        y_T=Trapezoid(t,y_T,h)
        t=t+h
        #print(t,actualFunction(t))
    bigTable.append(currentMaxVector)

with open("Output_p2.txt", "w") as text_file:
    # i:rows
    # j:columns
    for i in range(len(bigTable)):
        print(bigTable[i][0],'\t',bigTable[i][1],'\t',bigTable[i][2],'\t',bigTable[i][3],'\t',bigTable[i][4],'\t',bigTable[i][5],'\n', file=text_file)