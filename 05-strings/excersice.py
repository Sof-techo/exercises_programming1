def control_digit(number):
    control_digit=number%97
    if number % 97== 0:
        return 97
    else:
        return control_digit
    
    print(control_digit(50)) 
    
def make_10_digits(number):
    return f"{number,.010}"
print(make_10_digits(123)) # "0000000123"
    
    
def add_control_digit(text):
    return f"{text:.12}"


def add_symbols(text):
    first_part= text[0:3]
    second_part=text[3:7]
    third_part=text[7:]
    result=f"+++{first_part}/{second_part}/{third_part}+++"
    return result


    