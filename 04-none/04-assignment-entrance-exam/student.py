def  product(a, b, c):
    if a==b==c is None:
        return 1
    if a==None:
        return b*c
    if b==None:
        return a*c
    if c==None:
        return a*b
    
def  product(a, b, c):
    if a is None:
        a=1
    if b is None:
        b=1
    if c is None:
        c=1
        return a*b*c
    
#ans
def product(a, b, c):
    # Replace None with 1 for multiplication purposes
    if a is None:
        a = 1
    if b is None:
        b = 1
    if c is None:
        c = 1
    
    # Compute the product
    return a * b * c

# Examples of usage
print(product(2, 3, 4))    # Output: 24
print(product(None, 3, 5))  # Output: 15
print(product(None, None, None))  # Output: 1
