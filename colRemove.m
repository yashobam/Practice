function out = colRemove(in)

[rows,cols,colors] = size(in);

newCols = floor(cols/2);

out = uint8(zeros(rows,newCols,colors));

for i = 1:1:newCols
    out(:,i,:) = in(:,i*2-1,:);
end
end