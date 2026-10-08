print("CONVERSION DE MINUTOS")
print("-" * 40)

minutos = int(input("Digite la cantidad de minutos: "))

horas = minutos // 60
minutos_restantes = minutos % 60
horas_decimales = minutos / 60

print("-" * 40)
print("Minutos digitados:", minutos)
print("Equivale a:", horas, "horas y", minutos_restantes, "minutos")
print("En formato decimal:", round(horas_decimales, 2), "horas")
