function out=quiz(in)
[m,n]=size(in);
for i=1:m
    for j=1:n
        if i>j
            in(i,j)=i;
        elseif i<j
            in(i,j)=j;
        else
            in(i,j)=in(i,j)*2;
        end
    end
end
out=in;
end