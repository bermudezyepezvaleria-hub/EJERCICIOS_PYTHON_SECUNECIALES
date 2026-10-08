print("PERIMETRO Y AREA DE UN RECTANGULO")
print("-" * 40)

largo = float(input("Digite el largo en metros: "))
ancho = float(input("Digite el ancho en metros: "))

perimetro = 2 * (largo + ancho)
area = largo * ancho

print("-" * 40)
print("Largo:", largo, "m")
print("Ancho:", ancho, "m")
print("Formula aplicada: 2 x (largo + ancho)")
print("Perimetro:", round(perimetro, 2), "m")
print("Area:", round(area, 2), "m2")
