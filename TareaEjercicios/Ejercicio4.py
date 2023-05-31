#Implementar una cola utilizando una lista
class Cola:
    def __init__(self):
        self.items = []

    def esta_vacia(self):
        return len(self.items) == 0

    def encolar(self, elemento):
        self.items.append(elemento)

    def desencolar(self):
        if self.esta_vacia():
            return None
        return self.items.pop(0)


# Ejemplo del programa
cola = Cola()

cola.encolar(1)
cola.encolar(2)
cola.encolar(3)

print("Contenido de la cola:")
while not cola.esta_vacia():
    elemento = cola.desencolar()
    print(elemento)

