function [summedValue] = r7a2(input_matrix)
[rows,cols]=size(input_matrix);
summedValue=0;
for i=1:rows
    for j=1:cols
        summedValue=summedValue+input_matrix(i,j);
        if (i-1)*cols+j==4
            disp(i)
            disp(j)
            disp(summedValue)
        end
    end
end
end
