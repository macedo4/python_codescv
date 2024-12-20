print("Numbers conversion")
print("""Options
1)Binary
2)Octal
3)Hexadecimal
""")
your_option = int(input("Choose, please: [1-3]"))
your_number = int(input("Your number: "))
if your_option == 1:
    binary = bin(your_number)
    print(f"Your number converted to Binary: {binary}")
elif your_option == 2:
    octal = oct(your_number)
    print(f"Your number convert to Octal: {octal}")
else:
    hexadecimal = hex(your_number)
    print(f"Your number converted to Hexadecimal: {hexadecimal}")











