function [z] = recitation5_activity1(x,y)
if x==0 ||  y==0
    z = 0 ;
elseif x == y
    z = 1;
elseif x<0 && y<0
    z = x-y ;
else
    z = x+y;
end
