function [l,m,n]=hw5(a,b,c)
m=c./b;
l=m./a;
[l,ArrangeIndex] = sort(l,'descend');
m=m(ArrangeIndex);
n=a(ArrangeIndex);
end
