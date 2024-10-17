# write your code here
def next_player(player, player_count):
    
    #ans
   def next_player(player, player_count):
    return (player + 1) % player_count
#Increment and Modulus: 
# The expression (player + 1) % player_count adds 1 to the current player 
# and then uses the modulus operator to wrap around to the beginning if the current player
# reaches the last one (i.e., player count - 1).