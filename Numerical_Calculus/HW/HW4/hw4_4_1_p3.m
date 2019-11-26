% Jim Vargas
clc, format compact

fprintf("Jim Vargas HW4 4.1\nFor all problems, the columns of the tables will be n|e_n|r_n|p_n.\n\n");

fprintf("Problem 3#######################################\n");
a=0; b=1; m=8;
I=2/3;

E_left=zeros(m,4);
E_right=zeros(m,4);
E_trap=zeros(m,4);
E_mid=zeros(m,4);
E_simpson=zeros(m,4);

for n=1:m
    [L,R,T,M,S]=FiveQuad(a,b,2^(n-1));
    E_left(n,2)=I-L;    E_left(n,1)=2^(n-1);
    E_right(n,2)=I-R;   E_right(n,1)=2^(n-1);
    E_trap(n,2)=I-T;    E_trap(n,1)=2^(n-1);
    E_mid(n,2)=I-M;     E_mid(n,1)=2^(n-1);
    E_simpson(n,2)=I-S; E_simpson(n,1)=2^(n-1);
end

E_left(2:m,3)=abs(   E_left(1:m-1,2)./E_left(2:m,2)   );
E_left(2:m,4)= log(E_left(2:m,3))/log(2);
fprintf("Left\n"); disp(E_left);

E_right(2:m,3)=abs(   E_right(1:m-1,2)./E_right(2:m,2)   );
E_right(2:m,4)= log(E_right(2:m,3))/log(2);
fprintf("Right\n"); disp(E_right);


E_trap(2:m,3)=abs(   E_trap(1:m-1,2)./E_trap(2:m,2)   );
E_trap(2:m,4)= log(E_trap(2:m,3))/log(2);
fprintf("Trapezoid\n"); disp(E_trap);

fprintf("\n\n\n\n\n\n")

E_mid(2:m,3)=abs(   E_mid(1:m-1,2)./E_mid(2:m,2)   );
E_mid(2:m,4)= log(E_mid(2:m,3))/log(2);
fprintf("Midpoint\n"); disp(E_mid);

E_simpson(2:m,3)=abs(   E_simpson(1:m-1,2)./E_simpson(2:m,2)   );
E_simpson(2:m,4)= log(E_simpson(2:m,3))/log(2);
fprintf("Simpson\n"); disp(E_simpson);

fprintf("\n\nAs I said in problem (1) b), the derivative of f is not continuous on the interval [0,1], so none of the regularity assumptions for each quad. approx. really hold. Nevertheless, the data siggests that the convergence of some of these methods are near those dictateded by the theorem. For example, the order for the Trapezoid rule seems to be approaching 1.5, while the theorem dictates an order of 2. In fact, unless my coding is wrong, the order seems to be approaching 1.5 for the Midpoint and Simpson's Rule(s) as well.")




