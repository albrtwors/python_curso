class Productos:
    def __init__(self, nombre, precio, categoría, disponibilidad, marca):
        self.nombre = nombre
        self.precio = precio
        self.categoría = categoría
        self.disponibilidad = disponibilidad
        self.marca = marca

class Ropa(Productos):
    def __init__(self, nombre, precio, categoría, disponibilidad, marca, talla, material):
        super().__init__(nombre, precio, categoría, disponibilidad, marca)
        self.talla = talla
        self.material = material

class Electrodomésticos(Productos):
    def __init__(self, nombre, precio, categoría, disponibilidad, marca, potencia, consumo_energético):
        super().__init__(nombre, precio, categoría, disponibilidad, marca)
        self.potencia = potencia
        self.consumo_energético = consumo_energético

class Computadoras(Electrodomésticos):
    def __init__(self, nombre, precio, categoría, disponibilidad, marca, potencia, consumo_energético, procesador, ram, gráfica):
        super().__init__(nombre, precio, categoría, disponibilidad, marca, potencia, consumo_energético)
        self.procesador = procesador
        self.ram = ram
        self.gráfica = gráfica

comput1 = Computadoras("Asus Vivobook", 600, "Laptops", "No disponible", "Asus", "120w", "650w", "Ryzen 5", "16GB", "Radeon Vega 8")

print(f"Marca: {comput1.marca}")
print(f"Nombre: {comput1.nombre}")