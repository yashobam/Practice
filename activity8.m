function [out]=activity8()
    out = uint8(zeros(6,6,3));
    out([2:6],[2:6],2)=128;
    out([2:6],[2:6],3)=255;
    disp(out(:,4,1))
    imagesc(out)
    
end