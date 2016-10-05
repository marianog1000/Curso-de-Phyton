def rental_car_cost(days):
    total = days * 40
    if (days >= 7):
        return  total - 50
    elif (days >= 3):
        return total - 20
    else:
        return total
        
def hotel_cost(nights):
    return 140 * nights
    
def plane_ride_cost(city):
    if (city == "Charlotte"):
        return 183
    elif (city == "Tampa"):
        return 220
    elif (city == "Pittsburgh"):
        return 222
    elif (city == "Los Angeles"):
        return 475
        
def trip_cost(city, days):
    total = hotel_cost(days) 
    print total
    
    ride = plane_ride_cost(city)
    print ride 
    
    rental = rental_car_cost(days)
    print rental
    
    return total + ride + rental
    
print trip_cost("Tampa", 4)
