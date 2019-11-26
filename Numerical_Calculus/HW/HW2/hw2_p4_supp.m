%Jim Vargas
clc, format compact, format long e
fprintf("Jim Vargas\nSome convergence histories for Problem 4\n");
fprintf("NOTE: In all tables, the 'SuccessiveRatioSquared' columns are the current error divided by the square of the previous error.\n\n");

a0=-1; b0=1; r=0; M=10;
% This ends up re-using a lot of code, but I'm not sure how to recycle it.
% I need to redefine a new 'f' for each part, and then need to call it
% during each of the while loops. I need to learn how to pass a function
% definition instead of a function evaluated at a point.


% 4) a) ###################################################################
fprintf("Problem 4 a):\n");
tol=5*10^-4; 
z=@(u,v) (u*fa(v)-v*fa(u))/(fa(v)-fa(u));
x0=z(a0,b0); 

x=x0; a=a0; b=b0;
n=0;
errorVector=[];
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
TableMaker(M,n,errorVector);
fprintf("The succesive ratio of errors is increasing and approaching 1, which suggests convergence is sublinear.\n");



% 4 b) ####################################################################
fprintf("Problem 4 b):\n");
f=@(t) -2*t/(t+3);
tol=10^-12;
z=@(u,v) (u*f(v)-v*f(u))/(f(v)-f(u));
x0=z(a0,b0); 

x=x0; a=a0; b=b0;
n=0;
errorVector=[];
while abs(x-r)>tol
    error=abs(x-r);
    errorVector(n+1)=error;
    if f(a)*f(x)<0
        b=x;
    else
        a=x;
    end
    x=z(a,b);
    n=n+1;
end
TableMaker(M,n,errorVector);
fprintf("The succesive ratio of errors is constant throughout all iterations, so convergence is linear.\n");



% 4 c) ####################################################################
fprintf("Problem 4 c):\n");
f=@(t)-999*t/(t+1000);
tol=10^-12;
z=@(u,v) (u*f(v)-v*f(u))/(f(v)-f(u));
x0=z(a0,b0); 

x=x0; a=a0; b=b0;
n=0;
errorVector=[];
while abs(x-r)>tol
    error=abs(x-r);
    errorVector(n+1)=error;
    if f(a)*f(x)<0
        b=x;
    else
        a=x;
    end
    x=z(a,b);
    n=n+1;
end
TableMaker(4,n,errorVector);
fprintf("This one converged right away and the errors are hopping down constantly by a factor of about 10^-3, so convergence is linear.\n");



% 4 d) ####################################################################
fprintf("Problem 4 d):\n");
f=@(t) (t^2-2*t)/(t^2+2);
tol=10^-52;
z=@(u,v) (u*f(v)-v*f(u))/(f(v)-f(u));
x0=z(a0,b0); 

x=x0; a=a0; b=b0;
n=0;
errorVector=[];
while abs(x-r)>tol
    error=abs(x-r);
    errorVector(n+1)=error;
    if f(a)*f(x)<0
        b=x;
    else
        a=x;
    end
    x=z(a,b); %x
    n=n+1;
end
TableMaker(6,n,errorVector);
fprintf("Thhe ratio the current error the the previous squared error is about constant for each iteration, suggesting convergence here is quadratic.\n");



% 4 e) ####################################################################
fprintf("Problem 4 e):\n");
f=@(t) (t^3-2*t)/(t^3+2);
tol=10^-52;
z=@(u,v) (u*f(v)-v*f(u))/(f(v)-f(u));
x0=z(a0,b0); 

x=x0; a=a0; b=b0;
n=0;
errorVector=[];
while abs(x-r)>tol
    error=abs(x-r);
    errorVector(n+1)=error;
    if f(a)*f(x)<0
        b=x;
    else
        a=x;
    end
    x=z(a,b);
    n=n+1;
end
TableMaker(4,n,errorVector);
fprintf("Apparently convergence again happened really fast, so it's hard to say at what rate it happened. Based on my figures I can only say that the convergence is at least super-linear.\n");



% 4 f) ####################################################################
fprintf("Problem 4 f):\n");
p=3/2; q=1/2;
f=@(t) (q*abs(t)^p-t)/(q*abs(t)^p+1);
tol=10^-52;
z=@(u,v) (u*f(v)-v*f(u))/(f(v)-f(u));
x0=z(a0,b0); 

x=x0; a=a0; b=b0;
n=0;
errorVector=[];
while abs(x-r)>tol
    error=abs(x-r);
    errorVector(n+1)=error;
    if f(a)*f(x)<0
        b=x;
    else
        a=x;
    end
    x=z(a,b);
    n=n+1;
end
TableMaker(M,n,errorVector);
fprintf("Convergence here is not quadratic, as the ratio of successive squared errors gets large. On the otherhand, the linear ratio appears to be going down by non-constant amounts, so converegence seems at least super-linear.\n");



% f for part a specifally. It needs to be at the bottom and is piece-wise
function [y]=fa(x)
    if x<0
        y=x^2;
    else
        y=-(x^2)/(2*x+1);
    end
end

