function [L,d,p]=LDLH(A)


n=size(A,1); 
p=1:n;  % Initialize permutation vector

for k=1:n-1
    %% Determine pivot entry for column k, and permute rows
    [piv,q]=max(diag(A(k:n,k:n))); % q is first occurrence of maximal value piv
    q=q+k-1; % row number of pivot
    if q>k
        A([k q],:)=A([q k], :); % swap rows k and q
        A(:,[k q])=A(:,[q k]); % swap columns k and q
        p([k q])=p([q k]); % update permutation
    end
    %% Now eliminate sub-diagonal entries in column k
    ij=k+1:n;
    A(ij,k)=A(ij,k)/A(k,k);  % multipliers 
    A(ij,ij)=A(ij,ij)-A(ij,k)*A(k,ij); % row reduction
end

d=diag(A); 
% L=tril(A,-1)+eye(n);  % this does not work in FreeMat

L=A; 
for k=1:n
    L(k,k)=1;
    if k<n
        L(k,k+1:n)=0;
    end
end