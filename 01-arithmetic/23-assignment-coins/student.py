# write your code here

def coins(amount):
    # Calculate the number of 5-coins
     five_coins = amount // 5
     amount -= five_coins * 5  # Subtract the value of the 5-coins
    
    # Calculate the number of 2-coins
     two_coins = amount // 2
     amount -= two_coins * 2  # Subtract the value of the 2-coins
    
    # Remaining amount is the number of 1-coins
     one_coins = amount
    
    # Return the total number of coins
     return five_coins + two_coins + one_coins
def coins(amount):
    five_c= amount//5
    amount -=five_c*5
    two_c =amount//2
    amount-=two_c*2
    one_c=amount
    return five_c+ two_c + one_c