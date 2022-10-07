import coch
bici = coch.bicicleta("roja",2,"trial")
def catalogar(lista):
    for vehiculo in lista:
        print(vehiculo.__str__())
        
catalogar()