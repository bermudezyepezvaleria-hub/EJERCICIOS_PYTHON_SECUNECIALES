print("CONVERSION DE TEMPERATURA")

celsius = float(input("Digite los grados Celsius: "))

fahrenheit = celsius * 9 / 5 + 32
kelvin = celsius + 273.15

print("Grados Celsius:", celsius)
print("Grados Fahrenheit:", round(fahrenheit, 2))
