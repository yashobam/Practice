function [car]=carGenerator(mass,passengers,isElectric,fuelORcharge,workPerUnit)
if mass>=0 && passengers>=0 && fuelORcharge>=0 && workPerUnit>=0
    if isElectric && fuelORcharge<=100
        car=struct("mass",mass,"passengers",passengers,"isElectric",isElectric,"fuelORcharge",fuelORcharge,"workPerUnit",workPerUnit);
    elseif ~isElectric
        car=struct("mass",mass,"passengers",passengers,"isElectric",isElectric,"fuelORcharge",fuelORcharge,"workPerUnit",workPerUnit);
    else
        car='Invalid car parameters.';
    end
else
    car='Invalid car parameters.';
end
end