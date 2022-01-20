function [o1,o2]=proj3(alt,wat)
[m,n]=size(alt);
o1 = zeros(m,n,3,'uint8');
for i=1:m
    for j=1:n
        if wat(i,j)==1
            o1(i,j,1)=0;
            o1(i,j,2)=0;
            o1(i,j,3)=255;
        elseif alt(i,j)<0
            o1(i,j,1)=0;
            o1(i,j,2)=0;
            o1(i,j,3)=0;
        elseif alt(i,j)>=0 && alt(i,j)<1001
            o1(i,j,1)=0;
            o1(i,j,2)=255;
            o1(i,j,3)=0;
        elseif alt(i,j)>=1001 && alt(i,j)<2001
            o1(i,j,1)=255;
            o1(i,j,2)=255;
            o1(i,j,3)=0;
        elseif alt(i,j)>=2001 && alt(i,j)<3001
            o1(i,j,1)=255;
            o1(i,j,2)=128;
            o1(i,j,3)=0;
        elseif alt(i,j)>=3001 && alt(i,j)<4001
            o1(i,j,1)=255;
            o1(i,j,2)=0;
            o1(i,j,3)=0;
        elseif alt(i,j)>=4001
            o1(i,j,1)=255;
            o1(i,j,2)=255;
            o1(i,j,3)=255;
        end
    end
end
ma=max(max(alt));
for i=1:m
    for j=1:n
        if wat(i,j)==1
            alt(i,j)=ma-1;
        end
    end
end
mi=min(min(alt));
for i=1:m
    for j=1:n
        if alt(i,j)==ma
            o1(i,j,1)=255;
            o1(i,j,2)=0;
            o1(i,j,3)=255;
            maxx=[i,j];
        end
        if alt(i,j)==mi && wat(i,j)~=1
            o1(i,j,1)=128;
            o1(i,j,2)=0;
            o1(i,j,3)=255;
            minn=[i,j];
        end
    end
end
o2=((10*minn(1)-10*maxx(1))^2 + (10*minn(2)-10*maxx(2))^2)^0.5;
disp(o2);
imshow(o1)
end