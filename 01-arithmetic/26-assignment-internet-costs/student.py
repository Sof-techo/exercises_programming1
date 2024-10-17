# write your code here
def internet_costs(duration_in_seconds, cost_per_block):
    
    
    #ans
    def internet_costs(duration_in_seconds, cost_per_block):
    # If duration is 0, the cost is 0
     if duration_in_seconds == 0:
        return 0

    # Calculate the number of blocks (each block is 360 seconds)
    blocks = (duration_in_seconds + 359) // 360  # Adding 359 ensures we round up for any remaining seconds
    
    # Calculate the total cost
    return blocks * cost_per_block
