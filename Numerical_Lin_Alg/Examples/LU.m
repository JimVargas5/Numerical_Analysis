function [L,U,p]=LU(A)
%% [L,U,p]=LU(A).

n=size(A,1); 
p=1:n;  % Initialize permutation vector

for k=1:n-1
    %% Determine pivot entry for column k, and permute rows
    [piv,q]=max(abs(A(k:n,k))); % q is first occurrence of maximal value piv
    q=q+k-1; % row number of pivot
    if q>k
        A([k q],:)=A([q k], :); % swap rows k and q
        p([k q])=p([q k]); % update permutation
    end
    %% Now eliminate sub-diagonal entries in column k
    ij=k+1:n;
    A(ij,k)=A(ij,k)/A(k,k);  % multipliers 
    A(ij,ij)=A(ij,ij)-A(ij,k)*A(k,ij); % row reduction
end

%U=triu(A); L=eye(n)+tril(A,-1);
U=A; L=A;
for k=1:n-1
    U(k+1:n,k)=0;
    L(k,k+1:n)=0;
    L(k,k)=1;
end
L(n,n)=1;

% If desired, P=eye(n), P=P(p,:);
