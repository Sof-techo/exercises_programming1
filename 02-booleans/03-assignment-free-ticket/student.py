# write your code here
def free_ticket(age):
    return age >= 65 or age <12
    
def free_ticket(age):
    return age < 12 or age >= 65

print(free_ticket(11))  # Output: True
print(free_ticket(12))  # Output: False
print(free_ticket(18))  # Output: False
print(free_ticket(64))  # Output: False
print(free_ticket(65))  # Output: True
print(free_ticket(80))  # Output: True
