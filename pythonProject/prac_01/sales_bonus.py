
"""
Program to calculate and display a user's bonus based on sales.
If sales are under $1,000, the user gets a 10% bonus.
If sales are $1,000 or over, the bonus is 15%.
"""

sales =0
while sales >= 0:
    sales = float(input("Enter sales: "))

    sales += 1
    if sales < 1000:
        bonus = float(sales * 0.01)
        print(f"Your bonus is: ", bonus)

    elif sales > 1000:
        bonus = float(sales * 0.15)
        print(f"Your bonus is: ", bonus)

else:
    print("Invalid input")


    