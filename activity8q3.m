function activity8q3()
in=imread("ru.png");
[rows,cols,colors] = size(in);
newRows = 2*rows-1;
out = uint8(zeros(newRows,cols,colors));  
out(1:2:newRows,:,:) = in(:,:,:);
out(2:2:newRows,:,:) = in(1:rows-1,:,:)*0.5+in(2:rows,:,:)*0.5;
imshow(out)
end