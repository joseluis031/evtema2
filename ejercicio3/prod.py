class Producto:
    def __init__(self,codigo,nombre,pvp,tipo):
        self.codigo = codigo
        self.nombre = nombre
        self.pvp = pvp
        self.tipo = tipo
        print("El producto se ha creado con exito")

    def __str__(self):
        return f"CODIGO\t {self.codigo}\n" \
               f"NOMBRE\t\t {self.nombre}\n" \
               f"PVP\t\t {self.pvp}\n" \
               f"TIPO\t {self.tipo}\n"
               
alimento = Producto(203685, "Pasta", 55, "hidratos")
print(alimento)

alimento2 = Producto(103685, "Carne", 55, "proteina")
print(alimento2)