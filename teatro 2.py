class Teatro:
    def __init__(self, precio_boleto):
        self.precio_boleto = precio_boleto

    def calcular_descuento(self, edad, genero):
        descuento = 0
        
        if 5 <= edad <= 14:
            descuento = 0.35  # Descuento del 35% para la Categoría 1
        elif 15 <= edad <= 19:
            descuento = 0.25  # Descuento del 25% para la Categoría 2
        elif 20 <= edad <= 45:
            descuento = 0.10  # Descuento del 10% para la Categoría 3
        elif 46 <= edad <= 65:
            descuento = 0.25  # Descuento del 25% para la Categoría 4
        elif edad >= 66:
            descuento = 0.35  # Descuento del 35% para la Categoría 5
        
        # Aplicar descuento adicional si el cliente es mujer
        if genero.lower() == 'mujer':
            descuento += 0.05
        
        return descuento

    def dinero_perdido_por_categoria(self, clientes):
        perdido_total = 0  # Inicializar la cantidad total de dinero perdido

        for cliente in clientes:
            edad = cliente['edad']
            genero = cliente['genero']
            descuento = self.calcular_descuento(edad, genero)
            perdido_total += self.precio_boleto * descuento

        return perdido_total

# Datos de entrada
precio_boleto = float(input("Ingrese el precio del boleto: "))
cantidad_clientes = int(input("Ingrese la cantidad de clientes: "))
clientes = []

for i in range(cantidad_clientes):
    while True:
        edad = int(input(f"Ingrese la edad del cliente {i+1}: "))
        genero = input(f"Ingrese el género del cliente {i+1} (hombre/mujer): ")
        if edad >= 5:
            clientes.append({'edad': edad, 'genero': genero})
            break
        else:
            print("La edad mínima para entrar al teatro es de 5 años.")

# Proceso
teatro = Teatro(precio_boleto)
perdida_total = teatro.dinero_perdido_por_categoria(clientes)

# Salida
print(f"\nCantidad total de dinero perdido debido a los descuentos: ${perdida_total:.2f}")
