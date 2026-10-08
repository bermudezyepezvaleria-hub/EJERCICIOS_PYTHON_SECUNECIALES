PORC_SALUD = 0.04
PORC_PENSION = 0.04

print("LIQUIDACION DE SALARIO")
print("-" * 40)

empleado = input("Digite el nombre del empleado: ")
valor_hora = float(input("Digite el valor de la hora: "))
horas = float(input("Digite las horas trabajadas: "))

salario_bruto = valor_hora * horas
salud = salario_bruto * PORC_SALUD
pension = salario_bruto * PORC_PENSION
salario_neto = salario_bruto - salud - pension

print("-" * 40)
print(f"Empleado: {empleado}")
print(f"Valor hora: ${valor_hora:,.2f}")
print(f"Horas trabajadas: {horas}")
print(f"Salario bruto: ${salario_bruto:,.2f}")
print(f"Descuento salud (4%): ${salud:,.2f}")
print(f"Descuento pensión (4%): ${pension:,.2f}")
print(f"Salario neto a pagar: ${salario_neto:,.2f}")
