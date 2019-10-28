# Jim Vargas

def f(x):
    return x*x*x - 2*x + 2
def f_prime(x):
    return 3*x*x - 2

def Newton(x,f,f_prime):
    return x-f(x)/f_prime(x)

x01=.1
x02=.2

x=x01
n=0
#print(f(x01))
for i in range(25):
    x=Newton(x,f,f_prime)
    n+=1
    #print(n,'\t',x,'\t',f(x))

x=x02
n=0
#print(f(x02))
for i in range(25):
    x=Newton(x,f,f_prime)
    n+=1
    #print(n,'\t',x,'\t',f(x))

# So I can mention apparent rate of convergence.
r=x
x=x02
n=0
#print(f(x02))
for i in range(25):
    t1=abs(x-r)
    x=Newton(x,f,f_prime)
    t2=abs(x-r)
    n+=1
    if t1!=t2:
        print(n, x,'\t',abs(x-r),'\t',t2/t1**2)