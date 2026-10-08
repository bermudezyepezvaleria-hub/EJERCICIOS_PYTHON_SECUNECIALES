print("TOTAL DE LA COMPRA")
print("-" * 40)

producto = input("Ingrese el nombre del producto: ")
cantidad = int(input("Ingrese la cantidad: "))
precio = float(input("Ingrese el precio unitario: "))

subtotal = cantidad * precio
iva = subtotal * 0.19
total = subtotal + iva

print("-" * 40)
print("Producto:", producto)
print("Cantidad:", cantidad)
print("Precio unitario:", precio)
print("Subtotal:", round(subtotal, 2))
print("IVA (19%):", round(iva, 2))
print("Total a pagar:", round(total, 2))
