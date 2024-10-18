#!/usr/bin/env python3

def tip_calculator():
    total_price = float(input("Enter total price: "))
    tip_percentage = input("Enter tip percentage (default=20): ")

    # Use default value if no input is provided
    if tip_percentage == "":
        tip_percentage = 20
    else:
        tip_percentage = float(tip_percentage)

    # Calculate total amount to pay and round it to the nearest integer
    tip_amount = total_price * (tip_percentage / 100)
    total_to_pay = round(total_price + tip_amount)

    print(f"You have to pay {total_to_pay}")

def main():
    tip_calculator()

if __name__ == "__main__":
    main()

    