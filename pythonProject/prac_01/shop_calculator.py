
items = int(input("Number of Items: "))
amount = 0
for i in range(items):

    price = int(input("Enter price: "))

    amount += price

if amount > 100:
    discount = amount * 0.1
    amount -= discount

print(f"Total price for {items} items is ${amount}")