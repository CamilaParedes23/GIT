#cree una cola que permita almacenar números 
#enteros y realiza las operaciones de enconlar y desencolar
from collections import deque

class Cola:
    def __init__(self):
        self.items = deque()

    def esta_vacia(self):
        return len(self.items) == 0

    def encolar(self, elemento):
        self.items.append(elemento)

    def desencolar(self):
        if self.esta_vacia():
            return None
        return self.items.popleft()

# Ejemplo de uso
cola = Cola()

cola.encolar(1)
cola.encolar(2)
cola.encolar(3)

print("Cola:")
while not cola.esta_vacia():
    elemento = cola.desencolar()
    print(elemento)
