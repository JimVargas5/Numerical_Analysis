clc, format short e, format compact % formatting

a=0; b=1; % Endpoints of interval
I=1.7182818284590452354; % e - 1 (exact value of integral)
m=8; 
E=zeros(m,15); % zero matrix with m rows, 15 columns

% Errors for five methods in columns 1,4,7,10,13
n=1;
for k=1:m
    [L,R,T,M,S]=FiveQuad(a,b,n);
    E(k,1:3:13)=I-[L,R,T,M,S];
    n=2*n;
end

% Error ratios for five methods in columns 2,5,8,11,14
E(2:m,2:3:14)=abs(E(1:m-1,1:3:13)./E(2:m,1:3:13));

% Estimates of order of convergence in columns 3,6,9,12,15
E(2:m,3:3:15)=log(E(2:m,2:3:14))/log(2)

