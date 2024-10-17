# write your code here
def next_player2(player, player_count):
    return (player% player_count)+1
#ans
#Modulus Operator: The expression player % player_count wraps around when the player number exceeds the total number of players.
#Adjusting for One-Based Indexing: By adding 1 to the result, you shift the range from 0-based (0 to n-1) to 1-based (1 to n).