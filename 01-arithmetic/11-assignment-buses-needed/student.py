# write your code here
def buses_needed(people_count, bus_capacity):
    import math 
    result= math.ceil(people_count/bus_capacity)
    return result