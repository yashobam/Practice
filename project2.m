function [sdata,smean,sstd,snorm]=project2(data,cats,selected)
sdata=data(cats==selected);
smean=mean(sdata);
sstd=std(sdata);
snorm=(sdata-smean)/sstd;
end