function out = rowRemove(in)

[rows,cols,colors] = size(in);

newRows = floor(rows/2);

out = uint8(zeros(newRows,cols,colors));

for i = 1:1:newRows
    out(i,:,:) = in(i*2-1,:,:);
end
end