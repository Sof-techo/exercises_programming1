# write your code here

def pizza(n_people, slices_per_pizza):
    pizza= ((n_people+slices_per_pizza-1)//slices_per_pizza)
    return pizza

pizza(8,9)
pizza(16,8)
pizza(9,8)
pizza(10,4)