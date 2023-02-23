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

#3. Instanciar un objeto
Heroe = Personaje()

#4. Acceder a sus atributos

Heroe.nombre 
Heroe.especie 
Heroe.altura 

#5. Acceder a sus metodos

        
print('Atributos del personaje: ')
print("El personaje pertenece a la raza: " + Heroe.especie + " Se llama: " + Heroe.nombre + " Mide: " + str(Heroe.altura) + " metros")
print('')

print('Metodos del personaje: ')



Heroe.correr(True)