function [dist,eff] = carDistance(car)
eff=(car.workPerUnit*60)/car.mass;
dist=eff*car.fuelORcharge;
end