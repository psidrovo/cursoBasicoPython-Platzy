# def imprimir_mensaje():
#     print("Menaje especial: ")
#     print('Estoy aprendiendo a usar funciones')

# imprimir_mensaje()
# imprimir_mensaje()

# def conversacion(mensaje):
#     print('hola')
#     print('Como estas')
#     print('Elegiste la opcion ' + str(mensaje))
#     print('Adios')


# opcion = int(input('Elige una ocpion (1,2,3): '))

# if opcion == 1:
#     conversacion(opcion)
# elif opcion == 2:
#     conversacion(opcion)
# elif opcion ==3:
#     conversacion(opcion)
# else:
#     print('Escribe la opcion correcta')

from re import S


def suma(a,b):
    print('Se suma dos numero')
    resultado = a +b
    return resultado

sumatoria =  suma(1,4)

print("Resultado "+ str(sumatoria))