# write your code here
def is_valid_month(month):
    if 1<=month <=12:
        return True
def  is_leap_year(year):
    if  (year%4==0 and year %100!=0) or (year% 400==0):
        
      def has_30_days(month):
       return month in [4,6,9,11]

def has_31_days(month):
    return month in [1,3,5,7,8,10,12]
          
def has_28_days(month, year):
    return month ==2 and not is_leap_year
def has_29_days(month, year):
    return month ==2 and is_leap_year



    
    
    def is_valid_date(day, month, year):
     if not is_valid_month(month):
        return False
    return (
        (has_31_days(month) and 1 <= day <= 31) or
        (has_30_days(month) and 1 <= day <= 30) or
        (has_28_days(month, year) and day == 28) or
        (has_29_days(month, year) and day == 29)
    )
