class Producto:
    def __init__(self,codigo,nombre,pvp,tipo):
        self.codigo = codigo
        self.nombre = nombre
        self.pvp = pvp
        self.tipo = tipo
        print("El producto se ha creado con exito")

    def __str__(self):
        return f"REFERENCIA\t {self.codigo}\n" \
               f"NOMBRE\t\t {self.nombre}\n" \
               f"PVP\t\t {self.pvp}\n" \
               f"DESCRIPCIÓN\t {self.tipo}\n"