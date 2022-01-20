%This function calculates how long it takes an object to fall a certain
%distance given a certain initial velocity and a distance

function time = fallTime(startVelocity,distance)

g = 9.81; %m/s^2
len=length(startVelocity);
finalVelocity = sqrt(startVelocity^2 + 2*g*distance); %m/s

time = (finalVelocity - startVelocity)/g; %s