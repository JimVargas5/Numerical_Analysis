# Jim Vargas
# 5.2.1

# y'=f(t,y)
import math

def f(t,y):
    return t**2 / y
def actualFunction(t):
    return math.sqrt((2/3)*t**3 + 1)

t0=0
y0=1
h=1/4
steps=3

# The explicit methods
def ForwardEuler(t,y):
    return y + h*f(t,y)
def Midpoint(t,y):
    y_plusHalf=y + (h/2)*f(t,y)
    t_plusHalf=t + (h/2)
    return y + h*f(t_plusHalf,y_plusHalf)
def TPC(t,y,k):
    y_bar=y + h*f(t,y)
    return y + (h/2)*(f(t,k) + f(t0+(k+1)*h,y_bar))

with open("Output.txt", "w") as text_file:
    y=y0
    t=t0
    print("\nForward Euler\n", file=text_file)
    for k in range(1,steps+1):
        y=ForwardEuler(t,y)
        t=t0 + k*h

        print(k,'\t',t,'\t',y, file=text_file)

    y=y0
    t=t0
    print("\nMidpoint\n", file=text_file)
    for k in range(1,steps+1):
        y=Midpoint(t,y)
        t=t0 + k*h

        print(k,'\t',t,'\t',y, file=text_file)
    y=y0
    t=t0

    print("\nTrapezoid Predictor-Corrector\n", file=text_file)
    for k in range(1,steps+1):
        y=TPC(t,y,k)
        t=t0 + k*h

        print(k,'\t',t,'\t',y, file=text_file)

    print("\nActual Values\n", file=text_file)
    for k in range(1,steps+1):
        t=t0 + k*h
        print(t,'\t',actualFunction(t), file=text_file)
    
    #print("Purchase Amount: {}".format(), file=text_file)
