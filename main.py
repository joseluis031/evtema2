if __name__ == "__main__":  
    main = int(input("Que ejercicio deseas realizar(1y2,3,4 o 5):"))
    if main == 1 or 2:
        from ejercicio1y2.alum import *
        A = Alumno("javi",6)
        print(A)
        A.calif()
        B = Alumno("miguel",4)
        print(B)
        B.calif()
    elif main == 3:
        from ejercicio3.prod import *
        alimento = Producto(203685, "Pasta", 55, "hidratos")
        print(alimento)

        alimento2 = Producto(103685, "Carne", 55, "proteina")
        print(alimento2)
        cambio_pvp(alimento2, 10)
        print(alimento2)