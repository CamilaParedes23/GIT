#Implementar una pila utilizando una lista
class Pila:
    def __init__(self):
        self.items = []

    def esta_vacia(self):
        return len(self.items) == 0

    def apilar(self, elemento):
        self.items.append(elemento)

    def desapilar(self):
        if self.esta_vacia():
            return None
        return self.items.pop()

# Ejemplo del programa
pila = Pila()

pila.apilar(1)
pila.apilar(2)
pila.apilar(3)

print("Contenido de la pila:")
while not pila.esta_vacia():
    elemento = pila.desapilar()
    print(elemento)
