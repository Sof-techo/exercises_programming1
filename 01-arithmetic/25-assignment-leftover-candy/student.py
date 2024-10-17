# write your code here
def leftover_candy(candy_count, child_count):
     return candy_count % candy_count
 
 #ans
def leftover_candy(candy_count, child_count):
    return candy_count % child_count if child_count > 0 else candy_count
