#Implementa una pila utilizando una estructura de datos adecuada
#y realiza las operaciones de apilar y desapilar
class Pila:
    def __init__(self):
        self.items = []
    
    def esta_vacia(self):
        return len(self.items)==0
    
    def apilar(self, elemento):
        self.items.append(elemento)

    def desapilar(self):
        if self.esta_vacia():
            return None
        return self.items.pop()
    
#Ejemplo
pila = Pila()

pila.apilar(1)
pila.apilar(2)
pila.apilar(3)

print("Pila:")
while not pila.esta_vacia():
    elemento = pila.desapilar()
    print(elemento)