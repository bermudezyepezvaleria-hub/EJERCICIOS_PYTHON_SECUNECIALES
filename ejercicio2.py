print("PROMEDIO DE TRES NOTAS")

estudiante = input("Digite el nombre del estudiante: ")
nota1 = float(input("Digite la nota 1: "))
nota2 = float(input("Digite la nota 2: "))
nota3 = float(input("Digite la nota 3: "))

suma = nota1 + nota2 + nota3
promedio = suma / 3

print("-" * 40)
print("Estudiante:", estudiante)
print("Nota 1:", nota1)
print("Nota 2:", nota2)
print("Nota 3:", nota3)
print("Suma de las notas:", round(suma, 2))
print("Promedio:", round(promedio, 2))
 