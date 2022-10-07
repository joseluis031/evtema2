from ejercicio5.py.coch import Vehiculo
import coch
bici = coch.bicicleta("roja",2,"trial")
camion = coch.Camion("rojo",8,3000)
def catalogar(lista):
    for vehiculo in lista:
        print(vehiculo.__str__())
        
catalogar()
        