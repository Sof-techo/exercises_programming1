# write your code here
def rock_paper_scissors(player1_choice, player2_choice):
    if player1_choice==player2_choice:
        return 0 #tie"
   
    elif (player2_choice==0 and player2_choice==2) or\
         (player1_choice==1 and player2_choice==0) or\
         (player1_choice==2 and player2_choice==1):
        return 1# player1 wins
    else:
        return 2  # player2 wins   
             
             
#ans
def rock_paper_scissors(player1_choice, player2_choice):
    if player1_choice == player2_choice:
        return 0  # Tie
    elif (player1_choice == 0 and player2_choice == 2) or \
         (player1_choice == 1 and player2_choice == 0) or \
         (player1_choice == 2 and player2_choice == 1):
        return 1  # Player 1 wins
    else:
        return 2  # Player 2 wins
    
print(rock_paper_scissors(0, 0))  # Output: 0 (Tie)
print(rock_paper_scissors(1, 2))  # Output: 2 (Player 2 wins)
print(rock_paper_scissors(0, 2))  # Output: 1 (Player 1 wins)
print(rock_paper_scissors(2, 1))  # Output: 1 (Player 1 wins)
print(rock_paper_scissors(1, 0))  # Output: 2 (Player 2 wins)

             
             