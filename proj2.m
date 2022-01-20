function out1=proj2(filename,vacnum)
    x=csvread(filename);
    [~,col]=size(x);
    x=[x;zeros(1,col);zeros(1,col)];
    for i=1:col
        x(4,i)=i;
    end
    vacc=0;
    temp=[];
    for j = 0 : col-1
        for i = 1: col-j-1
            if x(2,i)>x(2,i+1)
                temp = x(:,i);
                x(:,i) = x(:,i+1);
                x(:,i+1) = temp;
            end
        end
    end
    for j = 0 : col-1
        for i = 1: col-j-1
            if x(1,i)>x(1,i+1)
                temp = x(:,i);
                x(:,i) = x(:,i+1);
                x(:,i+1) = temp;
            end
        end
    end
    
    for i=1:col
        
        if x(2,i)>=2
            x(5,i)=0;
        elseif x(3,i)<21 && x(3,i)>=0
            x(5,i)=0;
        elseif vacc==vacnum
            continue;
        else
            x(5,i)=1;
            vacc=vacc+1;
        end
    end
    for j = 0 : col-1
        for i = 1: col-j-1
            if x(4,i)>x(4,i+1)
                temp = x(:,i);
                x(:,i) = x(:,i+1);
                x(:,i+1) = temp;
            end
        end
    end
    indices=[];
    for i=1:col
        if x(5,i)==1
            indices=[indices i];
        end
    end
    disp(indices);
out1=x(1:5,:);
end