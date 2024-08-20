cars = 100               # number of cars available in garage
space_in_a_car = 4.0     # number of seats avaiable in car
drivers = 30             # number of drivers
passengers = 90          # Total number of passengers about to travel today
cars_not_driven = cars - drivers  # Remaining cars which is not driven
cars_driven = drivers             # Number of cars driven today
carpool_capacity = drivers * space_in_a_car  #Number of passenger can be accomdated
average_passengers_per_car = passengers / cars_driven #average number of person can be traveled in car

print "There are", cars, "cars available."
print "There are only", drivers, "drivers available."
print "There will be", cars_not_driven, "empty cars today."
print "We can transport", carpool_capacity, "people today."
print "We have", passengers, "to carpool today."
print "We need to put about", average_passengers_per_car,"in each car."
