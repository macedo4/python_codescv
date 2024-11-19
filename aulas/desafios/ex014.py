print("Conversor de temperaturas")
print("Fahrenheit para Celsius")
fahrenheit = float(input("Temperatura em fahrenheit: "))
celsius = (fahrenheit - 32) * 5 / 9
print(f"{fahrenheit}°F equivalem a {celsius:.2f}°C")
print("Celsius para Fahrenheit")
celsius = float(input("Temperatura em Celsius: "))
fahrenheit = (celsius * 9 / 5) + 32
print(f"{celsius}°C equivalem a {fahrenheit:.2f}°F")