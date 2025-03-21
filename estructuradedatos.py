print("Bienvenidos a mis estructuras de datos")

# Listas, Tuplas, Conjuntos y Diccionarios

#estructura de datos
#lista
numeros = [1,2,3,4,5,6,"ReneJose", True, 10, 11,1,2]
# las listas son mutables
# si permiten valores duplicados
print(numeros)
numeros.append("Ruiz")
print("Despues de agregar")
print(numeros)
print("Despues de meter un valor")
print(numeros[6])
numeros.remove(2)
print("Despues de eliminar")
print(numeros)

#tupla
numeros_primos = (1,2,3,4,5,6,"ReneJose", True, 10, 11)
# las listas son inmutables
# si permiten valores duplicados

#conjuntos
numeros_nuevos={1,2,3,4,5,6, 'ReneJose, True, 10, 11'}

#diccionarios

persona = {
    "nombre" : "Rene Jose",
    "edad" : 31,
    "ciudad" : "Piura",
    "correo" : "jasjjssa@gmail.com"
}