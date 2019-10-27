function TableMaker(M,n,errorVector)
    tableErrors=[];
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
    %N=(1:M)'; 
    Errors=tableErrors'; SuccessiveRatios=sR'; SuccessiveRatioSquared=sRSQ';
    %T=table(N,Errors,SuccessiveRatios,SuccessiveRatioSquared)
    T=table(Errors,SuccessiveRatios,SuccessiveRatioSquared)

end