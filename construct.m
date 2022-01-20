function [mat]=construct(x,y)
    if x<=20000 && y<=40000
        mat="Grade 1 Steel";
    elseif x<=45000 && y<=60000
        mat="Grade 2 Steel";
    elseif x<=65000 && y<=85000
        mat="Grade 3 Steel";
    elseif x<=90000 && y<=100000
        mat="Grade 4 Steel";
    elseif x<=95000 && y<=130000
        mat="Titanium";
    else
        mat="Consider a redesign";
end