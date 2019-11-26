function [x,fx,n]=regula(a,b)

nmax=2000; tol=5.0e-4; 

fa=f(a); fb=f(b);
if(fa*fb >= 0)
    disp('Bad search interval');
    x=NaN; fx=NaN; n=0;
    return;
end

r=0;

x=(a*fb-b*fa)/(fb-fa); fx=f(x); n=0;
e=abs(x-r)
while(n < nmax & abs(x-r)>tol)
    if(fa*fx<0)
        b=x;fb=fx;
    else
        a=x;fa=fx;
    end
    x=(a*fb-b*fa)/(fb-fa); fx=f(x); n=n+1;
    e=abs(x-r)
end

function y=f(x)

y=-x*x/(2*x+1);
if(x<0)
    y=x*x;
end