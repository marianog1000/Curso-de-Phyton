def rental_car_cost(days):
    total = days * 40
    if (days >= 7):
        return  total - 50
    elif (days >= 3):
        return total - 20
    else:
        return total
        
print rental_car_cost(10)
