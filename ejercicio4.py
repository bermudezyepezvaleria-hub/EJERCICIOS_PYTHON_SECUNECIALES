print("AREA DE UN TRIANGULO")
print("-" * 40)

base = float(input("Digite la base en centimetros: "))
altura = float(input("Digite la altura en centimetros: "))

area = base * altura / 2

print("-" * 40)
print("Base:", base, "cm")
print("Altura:", altura, "cm")
print("Formula aplicada: base x altura / 2")
print("Area del triangulo:", round(area, 2), "cm2")
