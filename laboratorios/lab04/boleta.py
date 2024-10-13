# Clase Boleta
class Boleta:
    def __init__(self, tipo_cliente, cantidad_pasajes, genero_cliente, tipo_servicio):
        self.tipo_cliente = tipo_cliente
        self.cantidad_pasajes = cantidad_pasajes
        self.genero_cliente = genero_cliente
        self.tipo_servicio = tipo_servicio
        self.importe_bruto = 0
        self.monto_descuento = 0
        self.importe_neto = 0
        self.calcular_importes()

    def calcular_importes(self):
        precios = {1: 70, 2: 140, 3: 280}
        descuento = 0
        precio = precios.get(self.tipo_servicio, 0)

        if self.cantidad_pasajes == 1:
            descuento = 0
        elif 2 <= self.cantidad_pasajes <= 5:
            descuento = 0.05
        elif 6 <= self.cantidad_pasajes <= 10:
            descuento = 0.12
        elif self.cantidad_pasajes >= 11:
            descuento = 0.15

        self.importe_bruto = self.cantidad_pasajes * precio
        self.monto_descuento = self.importe_bruto * descuento
        self.importe_neto = self.importe_bruto - self.monto_descuento

    def mostrar_boleta(self):
        print(f"Importe Bruto: ${self.importe_bruto:.2f}")
        print(f"Monto Descuento: ${self.monto_descuento:.2f}")
        print(f"Importe Neto: ${self.importe_neto:.2f}")

    def get_tipo_cliente(self):
        return self.tipo_cliente

    def get_genero_cliente(self):
        return self.genero_cliente

    def get_importe_neto(self):
        return self.importe_neto
