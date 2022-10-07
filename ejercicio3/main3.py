if __name__ == "__main__":  


        from prod import *
        alimento = Producto(203685, "Pasta", 55, "hidratos")
        print(alimento)

        alimento2 = Producto(103685, "Carne", 55, "proteina")
        print(alimento2)
        cambio_pvp(alimento2, 10)
        print(alimento2)