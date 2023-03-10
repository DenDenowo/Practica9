#1. Importar la clase
from Personaje import *

#2. Solicitar atributos para el objeto
print("")
print("### Solicitud de datos Heroe ###")
espH = input("Escribe la especie del héroe: ")
nomH = input("Escribe el nombre del héroe: ")
altH = float(input("Escribe la altura del héroe: "))
cargaH = int(input("¿Cuántas balas se puede recargar?: "))

print("")
print("### Solicitud de datos Villano ###")
espV = input("Escribe la especie del villano: ")
nomV = input("Escribe el nombre del villano: ")
altV = float(input("Escribe la altura del villano: "))
cargaV = int(input("¿Cuántas balas se puede recargar?: "))

#3. Creamos dos objetos
Heroe = Personaje(espH, nomH, altH)
Villano = Personaje(espV, nomV, altV)

Heroe.setNombre("Pepe Pecas")

#4. Acceder a sus atributos
print("")
print("## Atributos y métodos del héroe ##")
print("El personaje pertenece a la raza: " + Heroe.getEspecie())
print("Se llama: " + Heroe.getNombre())
print("Mide: " + str(Heroe.getAltura()) + " metros")
Heroe.correr(True)
Heroe.lanzarGranada()
Heroe.recargarArma(cargaH)

#Ejemplo de lo que no se puede hacer
#Heroe.__pensar()

print("")

print("")
print("## Atributos y métodos del Villano ##")
print("El personaje pertenece a la raza: " + Villano.getEspecie())
print("Se llama: " + Villano.getNombre())
print("Mide: " + str(Villano.getAltura()) + "  metros")
Villano.correr(False)
Villano.lanzarGranada()
Villano.recargarArma(cargaV)
print("")