function r6a2q1()
sun2014=csvread('sun2014.csv');
sun2015=csvread('sun2015.csv');
sun2016=csvread('sun2016.csv');
sun2017=csvread('sun2017.csv');
newarray=0.25*(sun2014+sun2015+sun2016+sun2017);
arr=1:12;
plot(arr,newarray)
hold on
plot(arr,sun2014)
plot(arr,sun2015)
plot(arr,sun2016)
plot(arr,sun2017)
legend("average sunlight","sun2014","sun2015","sun2016","sun2017")
xlabel("Months")
ylabel("Sunlight")
title("Bamalwa")
disp(newarray(7))

end