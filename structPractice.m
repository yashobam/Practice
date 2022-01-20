function [y]= structPractice(x)
y.num=x.num;
n=length(x.data);
if(n == x.num)
    y.data = x.data;
    y.name = append(x.name, ' - valid');
else
    y.name = append(x.name,' - modified');
    if (n < x.num)
        if isrow(x.data) == true
            y.data = [x.data,zeros(1,x.num-n)];
        else
            y.data = [x.data; zeros(x.num-n,1)];
        end
    elseif (n> x.num)
        y.data = x.data(1:1:x.num,:);
    end
end