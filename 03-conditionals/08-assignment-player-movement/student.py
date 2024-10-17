# write your code here
def player_movement(position, left_arrow, right_arrow, shift):
    if left_arrow and not right_arrow:
        movement = -1 if not shift else -2
    elif right_arrow and not left_arrow:
        movement = 1 if not shift else 2
    else:
        movement = 0  # No movement if both keys are pressed or none

    return position + movement
