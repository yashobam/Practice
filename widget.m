function [out]=widget(x,y)
    if y>(sqrt(5*x)/100)||y<(sqrt(0.2*x)/100)
        out=0;
    elseif y>(sqrt(2*x)/100)
        out=1;
    elseif y>(sqrt(0.5*x)/100)
        out=2;
    elseif y>(sqrt(0.2*x)/100)
        out=1;
    end
end