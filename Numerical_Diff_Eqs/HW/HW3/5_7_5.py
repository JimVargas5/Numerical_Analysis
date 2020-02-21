# Jim Vargas
# 5.7.5

"""
    This code runs the RK4 method on the system
    x'=2x-1.2xy
    y'=0.9xy-y
where x(t0), y(t0) are given. It also plots approximations of
x(t) and y(t), as well as a phase portrait of z=(x,y).
"""

import math
import numpy as np
from matplotlib import pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages
pdf=PdfPages('Output_5.pdf')

t0=0
tmax=10
h=1/32

x0=1
y0=1/2
z0=np.array([x0,y0])
# z=(x,y)

def x_dot(x,y):
    return 2*x - 1.2*x*y
def y_dot(x,y):
    return 0.9*x*y - y
def f(z):
    return np.array(
        [x_dot(z[0],z[1]),y_dot(z[0],z[1])]
    )

def RK4(h,z):
    K1=f(z)
    K2=f(z + h*(1/2)*K1)
    K3=f(z + h*(1/2)*K2)
    K4=f(z + h*K3)
    return z + h*(1/6)*(K1 + 2*K2 + 2*K3 + K4)


t=t0
z=z0
running_x=[x0]
running_y=[y0]
running_t=[t0]

while t<=tmax:
    z=RK4(h,z)
    t=t+h

    running_x.append(z[0])
    running_y.append(z[1])
    running_t.append(t)

fig=plt.figure()
plt.subplot(1,2,1)
plt.plot(running_t, running_x, label='x_k')
plt.plot(running_t, running_y, label='y_k')
plt.xlabel('t_k')
plt.title(
    "Populations over time\n h="+
    str(h)+"\nt in ["+str(t0)+","+str(tmax)+"]"
)
plt.legend(loc='best')

plt.subplot(1,2,2)
plt.plot(running_x, running_y)
plt.xlabel('x_k')
plt.ylabel('y_k')
plt.title("Phase portrait of z_k=(x_k,y_k)")
plt.close()
pdf.savefig(fig)


pdf.close()