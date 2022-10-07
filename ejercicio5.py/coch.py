class Vehiculo():
    def __init__(self, color, ruedas):
        self.color = color
        self.ruedas = ruedas
    def __str__(self):
        return "color {}, {} ruedas".format( self.color, self.ruedas )


class Coche(Vehiculo):
    def __init__(self, color, ruedas, velocidad, cilindrada):
        Vehiculo.__init__(self, color, ruedas)
        self.velocidad = velocidad
        self.cilindrada = cilindrada
    def __str__(self):
        return Vehiculo.__str__(self) + ", {} km/h, {}cc".format(self.velocidad, self.cilindrada)

class Camion(Vehiculo):
    def __init__(self, color, ruedas, carga):
        Vehiculo.__init__(color,ruedas)
        self.carga = carga
        
    def __str__(self):
        return Vehiculo.__str__(self) + ", {} kg".format(self.carga)
    
class Motocicleta(Vehiculo):
    def __init__(self, color, ruedas, velocidad, cilindrada):
        Vehiculo.__init__(color,ruedas)
        self.velocidad = velocidad
        self.cilindrada = cilindrada
        
    def __str__(self):
        return Vehiculo.__str__(self) + ", {} km/h, {}cc".format(self.velocidad, self.cilindrada)

    def set_velocidad(self,velocidad):
        self.velocidad=velocidad
    def get_velocidad(self):
        return self.velocidad
    
    def set_cilindrada(self,cilindrada):
        self.cilindrada=cilindrada
    def get_cilindrada(self):
        return self.cilindrada
    
    
class bicicleta(Vehiculo):
    def __init__(self, color, ruedas, tipo):
        Vehiculo.__init__(color,ruedas)
        self.tipo = tipo
    
    def __str__(self):
        return Vehiculo.__str__(self) + + ", {}".format(self.tipo)
    
    def set_tipo(self,tipo):
        self.tipo=tipo
    def get_tipo(self):
        return self.tipo

    
    
        
        
