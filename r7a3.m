function [summedValue] = r7a3(input_matrix)
[rows,cols]=size(input_matrix);
summedValue=0;
for i=1:rows
    for j=1:cols
        if isprime(abs(input_matrix(i,j)))
            summedValue=summedValue+input_matrix(i,j);
        end
    end
end
end
