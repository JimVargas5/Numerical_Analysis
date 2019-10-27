# Jim Vargas

p=3.0*2**-18
q=2.0
eps=2.0**-52
#print(eps)
def f(x):
    return x*x*x - p*x - q
def f_prime(x):
    return 3*x*x - p 

def Newton(x):
    return 524288.0*(x*x*x+1)/(786432*x*x-3)

x0=1.0
x=x0
print("Guess with x0: ",f(x))
n=0
for i in range(10):
    x=Newton(x)
    n+=1
    print(n,'\t',x,'\t',f(x))

print("Final guess: ",x,'\t',f(x))


