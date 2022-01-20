function [out]=E2Q6(in1,in2)
[~,cols]=size(in1);
out=[];
for i=1:cols
    if (in1(i)>in2(i)); x=in1(i)^2; else; x=in2(i)^2; end
    if (in1(i)<in2(i)); y=in1(i)^0.5; else; y=in2(i)^0.5; end
    out=[out, sin(y)^x];
end
end