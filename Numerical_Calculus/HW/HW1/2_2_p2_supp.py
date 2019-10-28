# Jim Vargas

p=3.0*2**-18
q=2.0
eps=2.0**-52
#print(eps)

# determine r
b=(q*q/4 - p*p*p/27)**(1.0/2.0)
r=(q/2 + b)**(1.0/3.0) + (q/2 - b)**(1.0/3.0)
print(r)
# This r is really bad!!!

def f(x):
    return x*x*x - p*x - q
def f_prime(x):
    return 3*x*x - p 

#def Newton1(x):
#    return 524288.0*(x*x*x+1)/(786432*x*x-3)
def Newton(x,f,f_prime):
    return x-f(x)/f_prime(x)

def Secant(x,t,f):
    return x-(x-t)*f(x)/(f(x)-f(t))
def Secant1(x,t):
    return x - (262144*x*x*x - 3*x - 524288)/(262144*t*t + 262144*t*x + 262144*x*x - 3)

print(f(r)) # Here shows why this r is really bad!!!
x0=1.0
x1=2
x=x1
y=x0
n=0

# for i in range(10):
#     x=Newton(x,f,f_prime)
#     n+=1
#     print(n,'\t',x,'\t',f(x))

# print(x)
# print(eps,abs(x-r))
n=1
for i in range(10):
    t=y
    y=x
    #x=Secant(x,t,f)
    x=Secant1(x,t)
    n+=1
    print(n,'\t',x,'\t',f(x))

print(x)
print(eps,abs(x-r))

