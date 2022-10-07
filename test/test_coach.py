class Alumno:   #no se si hay que hacer test pero no hace test a nada
    def __init__(self,nombre,nota):
        self.nombre=nombre
        self.nota=nota
    def __str__(self):
        return f"el alumno {self.nombre} ha sido creado con exito"
    def calif(self):
        a = self.nota
        if a>=5:
            print("el alumno ha sido aprobado")
        elif a < 5:
            print("el alumno no ha aprobado")
        else:
            pass
        
if __name__ == "__main__":  

        A = Alumno("javi",6)
        print(A)
        A.calif()
        B = Alumno("miguel",4)
        print(B)
        B.calif()