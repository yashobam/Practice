function out=Geometry(x,y,z)
    if strcmp(z,'Rectangle')
        out=x*y;
    elseif strcmp(z,'Cylinder')
        out=x*pi*y*y;
    elseif strcmp(z,'Pyramid')
        out=x*x*y/3;
    elseif strcmp(z,'Cone')
        out=pi*x*y*y/3;
    else
        out='wrong option';
    end
end