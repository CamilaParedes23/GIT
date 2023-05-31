#crear un programa que permita crear una lsita de nombres
#y luego se muestren los nombres en orden alfabético

def lista_nombres():
    nombres=[]
    cantidad=int(input("Ingrese la cantidad de nombres que desea agregar: "))
    for i in range(cantidad):
        nombre=input(f"Ingrese el nombre {i+1}: ")
        nombres.append(nombre)
    #ordenar la lista de nombres en orden alfabético
    nombres.sort()
    print("\El orden alfabético es: ")
    for nombre in nombres:
        print(nombre)

lista_nombres()