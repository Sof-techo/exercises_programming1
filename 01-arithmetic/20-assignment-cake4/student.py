# write your code here
def cake4(eggs, flour, butter, sugar, eggs_per_cake, flour_per_cake, butter_per_cake, sugar_per_cake):
    cake4_from_eggs=eggs//eggs_per_cake
    cake4_from_flour=flour//flour_per_cake
    cake4_from_butter=butter//butter_per_cake
    cake4_from_sugar=sugar//sugar_per_cake
    return min(cake4_from_eggs,cake4_from_flour,cake4_from_butter,cake4_from_sugar)


print(cake4(5, 250, 200, 250, 5, 250, 200, 250))   # Output: 1
print(cake4(10, 500, 400, 500, 5, 250, 200, 250))  # Output: 2
print(cake4(25, 1000, 800, 1000, 5, 250, 200, 250))  # Output: 4
print(cake4(0, 0, 0, 0, 5, 250, 200, 250))           # Output: 0
print(cake4(5, 250, 200, 200, 5, 250, 200, 250))     # Output: 0
