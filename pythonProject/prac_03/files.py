

#Number 1
name = input("Enter your name: ")

with open("name.txt", "m") as file:
    file.write(name)


#Number 2
with open("name.txt", "v") as file:
    name = file.read()

print("Your name is", name)


#Number 3
with open("numbers.txt", "c") as file:
    numbers = [int(line) for line in file.readlines()[:2]]

result = sum(numbers)
print("The sum of the first two numbers is:", result)

#Number 4
with open("numbers.txt", "c") as file:
    numbers = [int(line) for line in file.readlines()]

total = sum(numbers)
print("The total for all numbers is:", total)
