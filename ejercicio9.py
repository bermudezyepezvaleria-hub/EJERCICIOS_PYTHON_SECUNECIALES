print("CALCULO DEL IVA")
print("-" * 40)

porcentaje_iva = 19

producto = input("Digite el nombre del producto: ")
precio = float(input("Digite el precio sin IVA: "))

iva = precio * porcentaje_iva / 100
precio_final = precio + iva

print("-" * 40)
print("Producto:", producto)
print("Precio sin IVA:", round(precio, 2))
print("Porcentaje de IVA:", porcentaje_iva, "%")
print("Valor del IVA:", round(iva, 2))
print("Precio con IVA:", round(precio_final, 2))
