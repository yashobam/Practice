function E2Q5()
A=uint8(zeros(2,2,3));
x=[255 0;0 255];
y=[0 255;255 0];
z=[255 0;255 0];
A(:,:,1)=z;
A(:,:,2)=y;
A(:,:,3)=x;
imagesc(A)
B(:,:,1)=x;
B(:,:,2)=x;
B(:,:,3)=y;
imagesc(B)
end