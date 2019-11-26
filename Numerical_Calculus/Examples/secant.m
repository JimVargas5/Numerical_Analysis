function [x,n]=secant(x0,x1)

nmax=40; tol=eps; 

r=1.6319824429618811918;

s=sprintf('%d %11.4e',0,x0);
disp(s)
s=sprintf('%d %11.4e',1,x1);
disp(s)

f0=f(x0); f1=f(x1);
n=1;
while(n < nmax && abs(x1-r)>tol)
    x= x1-(x1-x0)*f1/(f1-f0);
    x0=x1; f0=f1;
    x1=x; f1=f(x1);
    n=n+1;
    s=sprintf('%d %11.4e',n,x);
    disp(s)
end
x=x1;

end % secant
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

function y=f(x)
    
    a=4+sqrt(5); b=(19+7*sqrt(5))/4; c=(7+3*sqrt(5))/4;
    y=2-a*x+b*x*x-c*x*x*x;
    
end % f