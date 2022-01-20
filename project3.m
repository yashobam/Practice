function project3(dims,fred,fgreen,fblue,pred,pgreen,pblue)
out =uint8(zeros(dims,dims,3));
o2 =uint8(zeros(dims,dims,3));
for i=1:dims
    out(:,i,1)=255*abs(sin((i*fred)/100+pred));
    out(:,i,3)=255*abs(sin((i*fblue)/100+pblue));
    out(:,i,2)=255*abs(sin((i*fgreen)/100+pgreen));
end
for i=1:dims
    o2(:,i,:)=floor((double(out(1,i,1))+double(out(1,i,2))+double(out(1,i,3)))/400)*255;
end
imshow(out);
end