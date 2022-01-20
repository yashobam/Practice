function out=Homework8(n)
out = uint8(zeros(6,6,3));
out(1:2:n,1:2:n,2)=255;
out(2:2:n,1:2:n,1)=255;
out(1:2:n,2:2:n,3)=255;
out(2:2:n,2:2:n,2)=255;
imshow(out)
end