def multiple_choice(right_answer, given_answer):
    if given_answer ==None:
        return 0
    elif given_answer==True:
        return 1
    else:
        return -0.2
    #ans
    def multiple_choice(right_answer, given_answer):
      if given_answer is None:
        return 0  # No answer
      elif given_answer == right_answer:
        return 1  # Correct answer
      else:
        return -0.2  # Incorrect answer
