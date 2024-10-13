# Clase RegistroVentas
class RegistroVentas:
    def __init__(self):
        self.boletas = []
        self.total_clientes_masculinos = 0
        self.total_ventas_entre_70_y_500 = 0
        self.total_ventas_femeninas_entre_140_y_1000 = 0
        self.acumulado_ventas = 0
        self.acumulado_importe_neto_tipo_1 = 0
        self.contador_clientes_tipo_1 = 0

    def registrar_boleta(self, boleta):
        self.boletas.append(boleta)
        self.acumulado_ventas += boleta.get_importe_neto()
        if boleta.get_tipo_cliente() == 1:
            self.acumulado_importe_neto_tipo_1 += boleta.get_importe_neto()
            self.contador_clientes_tipo_1 += 1
        if boleta.get_genero_cliente().lower() == 'm':
            self.total_clientes_masculinos += 1
        if 70 <= boleta.get_importe_neto() <= 500:
            self.total_ventas_entre_70_y_500 += 1
        if boleta.get_genero_cliente().lower() == 'f' and 140 <= boleta.get_importe_neto() <= 1000:
            self.total_ventas_femeninas_entre_140_y_1000 += 1

    def mostrar_resultados(self):
        print("Resultados:")
        print(f"Cantidad de clientes de género masculino: {self.total_clientes_masculinos}")
        print(f"Cantidad de ventas con Importe Neto >= 70 y <= 500: {self.total_ventas_entre_70_y_500}")
        print(f"Cantidad de ventas de clientes femeninos con Importe Neto >= 140 y <= 1000: {self.total_ventas_femeninas_entre_140_y_1000}")
        print(f"Acumulado del Importe de Ventas: ${self.acumulado_ventas:.2f}")
        print(f"Acumulado del Importe Neto de clientes tipo 1: ${self.acumulado_importe_neto_tipo_1:.2f}")
        if self.contador_clientes_tipo_1 > 0:
            promedio_importe_neto_tipo_1 = self.acumulado_importe_neto_tipo_1 / self.contador_clientes_tipo_1
            print(f"Promedio del Importe Neto de clientes tipo 1: ${promedio_importe_neto_tipo_1:.2f}")
        else:
            print("No hay clientes de tipo 1 registrados.")
