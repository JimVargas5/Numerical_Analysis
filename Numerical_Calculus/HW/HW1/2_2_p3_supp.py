# Jim Vargas
import math

r=math.pi/2.0
def f(x):
    return (math.cos(x))**2.0
def f_prime(x):
    return -2*math.sin(x)*math.cos(x)

def Newton(x,f,f_prime):
    return x-f(x)/f_prime(x)
def Newton1(x):
    return (math.cos(x) + 2*x*math.sin(x))/(2*math.sin(x))

x0=1
x=x0
n=0
while abs(x-r)!=0:
    t1=abs(x-r)
    x=Newton1(x)
    t2=abs(x-r)
    n+=1
    print(n, x,'\t',abs(x-r),'\t',t2/t1)

print(r)