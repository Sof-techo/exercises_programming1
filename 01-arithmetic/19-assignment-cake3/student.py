# write your code here
def cake3(eggs, flour, butter, sugar):
    eggs_per_cake3= 5
    flour_per_cake3= 250
    butter_per_cake3= 200
    sugar_per_cake3= 250
    
    a=cakes_from_eggs=eggs//eggs_per_cake3
    d=cakes_from_flour= flour// cakes_from_flour
    c=cakes_from_butter=butter//cakes_from_butter
    b=cakes_from_sugar=sugar//cakes_from_sugar
    return min(a,b,c,d)

def cake3(eggs, flour, butter, sugar):
    # Define the amount of each ingredient needed per cake
    eggs_per_cake = 5
    flour_per_cake = 250
    butter_per_cake = 200
    sugar_per_cake = 250

    # Calculate the number of cakes that can be made from each ingredient
    cakes_from_eggs = eggs // eggs_per_cake
    cakes_from_flour = flour // flour_per_cake
    cakes_from_butter = butter // butter_per_cake
    cakes_from_sugar = sugar // sugar_per_cake

    # Return the minimum number of cakes that can be made
    return min(cakes_from_eggs, cakes_from_flour, cakes_from_butter, cakes_from_sugar)
