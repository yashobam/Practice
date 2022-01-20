function out = rowAdd(in)

[rows,cols,colors] = size(in);

newRows = 2*rows-1;

out = uint8(zeros(newRows,cols,colors));

for i = 1:1:rows
    out(i*2-1,:,:) = in(i,:,:);
    
end
for j = 2:2:newRows
    for i=1:cols
        out(j,i,1) = uint8((int32(out(j+1,i,1))+int32(out(j-1,i,1)))/2);
        out(j,i,2) = uint8((int32(out(j+1,i,2))+int32(out(j-1,i,2)))/2);
        out(j,i,3) = uint8((int32(out(j+1,i,3))+int32(out(j-1,i,3)))/2);
    end
end
end