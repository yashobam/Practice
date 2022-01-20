function [out]=E2Q7(m,n)
out=[];
for i=1:n
    out=[out, [i+1:i+1:(i+1)*m]'];
end

end