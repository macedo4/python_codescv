import math
angulo = float(input("Digite um angulo: "))
rad = math.radians(angulo)
cosseno = math.cos(rad)
tangente = math.tan(rad)
seno = math.sin(rad)
print(f"Cosseno: {cosseno:.2f}")
print(f"Tangente: {tangente:.2f}")
print(f"Seno: {seno:.2f}")