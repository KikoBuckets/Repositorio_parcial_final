total_clientes = 0
clientes_que_compraron = 0
productos = {'Sauco': 0, 'Espino': 0, 'Acebo': 0, 'Sauce': 0}

while True:
  respuesta = input("Hay un cliente si/no: ").lower()

if respuesta == "no":
  
  break

total_clientes +=1

respuesta_compra = input("El cliente compro si/no: ").lower()

if respuesta_compra == "si":
  clientes_que_compraron += 1

  producto_comprado = input("¿Qué producto compró? (Sauco/Espino/Acebo/Sauce): ").title()

  if producto_comprado in productos:
      productos[producto_comprado] += 1

if respuesta_compra == "si":
  clientes_que_compraron += 1

  producto_comprado = input("¿Qué producto compró? (Sauco/Espino/Acebo/Sauce): ").title()

  if producto_comprado in productos:
      productos[producto_comprado] += 1
    
print("\resumen: ")
print("total clientes")
print("Clientes que compraron:", clientes_que_compraron)

for producto, cantidad in productos.items():
    print(f"Clientes que compraron {producto}: {cantidad}")
