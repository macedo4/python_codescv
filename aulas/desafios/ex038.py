print("Comparison of two numbers")
number_a1 = int(input("Your first number, please: "))
number_b1 = int(input("Your second number, please: "))
if number_a1 > number_b1:
    print(f"{number_a1} is greater than {number_b1}")
elif number_b1 == number_a1:
    print(f"{number_a1} is equal to {number_b1}")
else:
    print(f"{number_b1} is less than {number_a1}")