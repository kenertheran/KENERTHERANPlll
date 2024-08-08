from animal import animal

class Ave(animal):
    def __init__(self, nombre, peso, nacimiento, propietario):
        super().__init__(nombre,peso)
        self.nacimiento = nacimiento
        self.propietario = propietario
        
    def calcular_edad(self):
        año_actual = 2024
        edad = año_actual - self.nacimiento
        print('tiene' ,edad, 'años')
        
        if edad > 5:
            print ("MAYOR DE EDAD")
        
        else:
            print  ("MENOR DE EDAD")
        
ave1 = Ave (nombre= "cobaski", peso = "5 kilogramos", nacimiento = 2022, propietario = "kener")
ave1.imprimir_nombre()
ave1.calcular_edad()