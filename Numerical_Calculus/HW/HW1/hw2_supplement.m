%Jim Vargas
clc, format compact, format long e
fprintf("Jim Vargas\n");

% 4) a)
fprintf("Problem 4 a):\n");
tol=5*10^-4; r=0;
a0=-1; b0=1;
z=@(u,v) (u*fa(v)-v*fa(u))/(fa(v)-fa(u));
x0=z(a0,b0); 

x=x0; a=a0; b=b0;
n=0;
errorVector=[];
% The Regula Falsi thing
while abs(x-r)>tol
    error=abs(x-r);
    errorVector(n+1)=error;
    
    if fa(a)*fa(x)<0
        b=x;
    else
        a=x;
    end
    x=z(a,b);
    n=n+1;
end
M=10; tableErrors=[];
sR=[]; sR(1)="-";
sRSQ=[]; sRSQ(1)="-";
fprintf("A brief convergence history for the first "+M+" iterations of "+n+"\n");
for i=1:M
    tableErrors(i)=errorVector(i);
end
for i=2:M
    sR(i)=tableErrors(i)/tableErrors(i-1);
    sRSQ(i)=tableErrors(i)/tableErrors(i-1)^2;
end
N=(1:M)'; Errors=tableErrors'; SuccessiveRatios=sR'; SuccessiveRatiosSquared=sRSQ';
T=table(N,Errors,SuccessiveRatios,SuccessiveRatiosSquared)
fprintf("The succesive ratio of errors is increasing and approaching 1, which suggests convergence is sublinear.\n");







% f for part a, specifally
function [y]=fa(x)
    if x<0
        y=x^2;
    else
        y=-(x^2)/(2*x+1);
    end
end

