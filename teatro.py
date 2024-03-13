class Teatro:
    def __init__(self, precio_boleto):
        self.precio_boleto = precio_boleto

    def calcular_descuento(self, edad):
        if 5 <= edad <= 14:
            return 0.35  # Descuento del 35% para la Categoría 1
        elif 15 <= edad <= 19:
            return 0.25  # Descuento del 25% para la Categoría 2
        elif 20 <= edad <= 45:
            return 0.10  # Descuento del 10% para la Categoría 3
        elif 46 <= edad <= 65:
            return 0.25  # Descuento del 25% para la Categoría 4
        elif edad >= 66:
            return 0.35  # Descuento del 35% para la Categoría 5
        else:
            return 0  # No hay descuento para edades menores de 5 años

    def dinero_perdido_por_categoria(self, edades):
        perdido_total = 0  # Inicializar la cantidad total de dinero perdido

        for edad in edades:
            descuento = self.calcular_descuento(edad)
            perdido_total += self.precio_boleto * descuento

        return perdido_total

# Datos de entrada
precio_boleto = float(input("Ingrese el precio del boleto: "))
cantidad_clientes = int(input("Ingrese la cantidad de clientes: "))
edades_clientes = []


for i in range(cantidad_clientes):
    while True:
        edad = int(input(f"Ingrese la edad del cliente {i+1}: "))
        if edad >= 5:
            edades_clientes.append(edad)
            break
        else:
            print("La edad mínima para entrar al teatro es de 5 años.")

# Proceso
teatro = Teatro(precio_boleto)
perdida_total = teatro.dinero_perdido_por_categoria(edades_clientes)

# Salida
print(f"\nCantidad total de dinero perdido debido a los descuentos: {perdida_total} unidades monetarias")
