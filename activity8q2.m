function [out]=activity8q2(in)
    
    out = uint8(zeros(size(in)));
    out(:,:,1)=in(:,:,1);
    out(:,:,2)=in(:,:,2);
    out(:,:,3)=in(:,:,2);
    imagesc(out)
    
end