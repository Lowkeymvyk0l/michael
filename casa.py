class Casa:
    def __init__(self, costo, ingresos_comprador):
        self.costo = costo
        self.ingresos_comprador = ingresos_comprador

    def calcular_pie(self):
        if self.ingresos_comprador >= 80000:
            return 0.15 * self.costo
        else:
            return 0.30 * self.costo

    def calcular_pagos_mensuales(self):
        if self.ingresos_comprador >= 80000:
            monto_prestamo = self.costo - self.calcular_pie()
            num_meses = 10 * 12  
        else:
            monto_prestamo = self.costo - self.calcular_pie()
            num_meses = 7 * 12  

        pago_mensual = monto_prestamo / num_meses
        return pago_mensual


costo_casa = float(input("Ingrese el costo de la casa: "))
ingresos_comprador = float(input("Ingrese los ingresos del comprador: "))


casa = Casa(costo_casa, ingresos_comprador)


pie = casa.calcular_pie()
pago_mensual = casa.calcular_pagos_mensuales()


print(f"\nEl comprador debe pagar un pie de ${pie:.2f}")
print(f"El comprador debe pagar ${pago_mensual:.2f} mensuales durante el plazo del préstamo.")
