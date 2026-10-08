print("CONSUMO DE GASOLINA")
print("-" * 40)

vehiculo = input("Digite el nombre del vehiculo: ")
kilometros = float(input("Digite los kilometros recorridos: "))
litros = float(input("Digite los litros consumidos: "))

rendimiento = kilometros / litros

print("-" * 40)
print("Vehiculo:", vehiculo)
print("Kilometros recorridos:", kilometros)
print("Litros consumidos:", litros)
print("Rendimiento:", round(rendimiento, 2), "km por litro")

