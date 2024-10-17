# write your code here
def total_cost(amount):
    if amount < 100:
        amount +=10
     
    if amount>= 200:
       amount -= amount*0.05
       return amount
    
#ans
def total_cost(amount):
    # Check for delivery fee
    if amount < 100:
        amount += 10  # Add delivery fee

    # Check for discount
    if amount >= 200:
        amount -= amount * 0.05  # Apply 5% discount

    return amount
