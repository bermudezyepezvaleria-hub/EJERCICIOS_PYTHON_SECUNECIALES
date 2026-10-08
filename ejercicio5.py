print("CALCULO DE EDAD")
print("-" * 40)

anio_actual = 2026

nombre = input("Digite el nombre de la persona: ")
anio_nacimiento = int(input("Digite el año de nacimiento: "))

edad = anio_actual - anio_nacimiento
meses = edad * 12
dias = edad * 365

print("-" * 40)
print("Persona:", nombre)
print("Año actual:", anio_actual)
print("Año de nacimiento:", anio_nacimiento)
print("Edad en años:", edad)
print("Edad aproximada en meses:", meses)
print("Edad aproximada en dias:", dias)
