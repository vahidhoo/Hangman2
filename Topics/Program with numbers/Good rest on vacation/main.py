# put your python code here
duration_day = int(input())
food_cost_per_day = int(input())
flight_cost_one_way = int(input())
hotel_cost_per_night = int(input())

# calculation part
total_food_cost = duration_day * food_cost_per_day
total_hotel_cost = (duration_day - 1) * hotel_cost_per_night
total_flight_cost = flight_cost_one_way * 2

# Total cost
total_cost = total_food_cost + total_flight_cost + total_hotel_cost
print(total_cost)
