
vechile_milage = int(input("ENTER YOUR VECHILES MILAGE :"))
todays_fuel_price = int(input("ENTER TODAYS FUEL PRICE :"))
km_to_travel = int(input("KM YOU WANT TO TRAVEL :"))
time_to_travel = int(input("YOUR AVERAGE SPEED(kmph) :"))

liters = km_to_travel / vechile_milage
print("YOU NEED TO FILL FUEL IN LITERS : ",liters)

price_of_fuel=todays_fuel_price*liters
print("YOU NEED TO PAY :",price_of_fuel)

hour_to_reach= km_to_travel/time_to_travel
print("YOU WILL REACH DESTINATION IN HOURS :",hour_to_reach)



