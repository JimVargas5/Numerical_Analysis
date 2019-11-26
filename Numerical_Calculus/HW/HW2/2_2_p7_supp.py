# Jim Vargas
import math as m

a0=2.0
a1=-(4.0+m.sqrt(5))
a2=(19.0+7*m.sqrt(5))/4.0
a3=-(7+3*m.sqrt(5))/4.0

def f(x):
    return a0 + a1*x + a2*x*x + a3*x*x*x

def Secant(x,t,f):
    return x-(x-t)*f(x)/(f(x)-f(t))

x0=0
x1=1

y=x0
x=x1
n=1
while f(x)!=f(y):
    t=y
    y=x
    x=Secant(x,t,f)
    n+=1
    print(n,'\t',x,'\t',f(x))


