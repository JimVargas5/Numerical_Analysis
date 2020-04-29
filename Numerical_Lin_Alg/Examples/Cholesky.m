function R=Cholesky(A)
%% R=Cholesky(A).
%% For a positive definite matrix A, the routine computes the
%% upper-triangular factor R of the Cholesky decomposition
%% A=R'*R, using an outer-product form of the algorithm to
%% overwrite the upper-triangular part of A

n=size(A,1); 

%% Inner-product version
for i=1:n
   jj=i:n;
   A(i,jj)=A(i,jj)-A(1:i-1,i)'*A(1:i-1,jj);
   A(i,jj)=A(i,jj)/sqrt(A(i,i));
end

%% Outer-product version
%for k=1:n-1
%    A(k,k:n)=A(k,k:n)/sqrt(A(k,k));  % row k of R 
%    ij=k+1:n;    
%    A(ij,ij)=A(ij,ij)-A(k,ij)'*A(k,ij); 
%end
%A(n,n)=sqrt(A(n,n));

%R=triu(A); % Doesn't work in FreeMat
R=A;
for k=1:n-1
    R(k+1:n,k)=0;
end
