class BienesRaices:
    def __init__(self, costo_casa, ingresos_comprador):
        self.costo_casa = costo_casa
        self.ingresos_comprador = ingresos_comprador

    def calcular_pago_pie(self):
        if self.ingresos_comprador >= 80000:
            porcentaje_pie = 0.15
        else:
            porcentaje_pie = 0.30
        
        monto_pie = porcentaje_pie * self.costo_casa
        return monto_pie

    def calcular_pagos_mensuales(self):
        if self.ingresos_comprador >= 80000:
            plazo_anios = 10
        else:
            plazo_anios = 7
        
        monto_pie = self.calcular_pago_pie()
        monto_prestamo = self.costo_casa - monto_pie
        num_meses = plazo_anios * 12
        pago_mensual = monto_prestamo / num_meses
        return pago_mensual

# Datos de entrada
costo_casa = float(input("Ingrese el costo de la casa: "))
ingresos_comprador = float(input("Ingrese los ingresos del comprador: "))

# Crear objeto BienesRaices
bienes_raices = BienesRaices(costo_casa, ingresos_comprador)

# Calcular el pie y los pagos mensuales
monto_pie = bienes_raices.calcular_pago_pie()
pago_mensual = bienes_raices.calcular_pagos_mensuales()

# Mostrar resultados
print(f"\nEl comprador debe pagar un pie de ${monto_pie:.2f}")
print(f"El comprador debe pagar ${pago_mensual:.2f} mensuales durante el plazo del préstamo.")
