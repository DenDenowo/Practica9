class Personaje:
  #Creamos el constructor
  def __init__(self, esp, nom, alt):
    self.nombre = nom
    self.especie = esp
    self.altura = alt
    
  def correr(self,estado):
    if estado == True:
        print('El personaje '+self.nombre+' está corriendo')
    else:
      print('El personaje '+self.nombre+' está quieto')
        
            
        
  def lanzarGranada(self):
    print('El personaje '+self.nombre+' lanzó una granada')

  def recargarArma(self,municiones):
    cargador=5
    cargador = cargador + municiones
    print('El personaje '+self.nombre+' recargó su arma y ahora tiene: '+str(cargador)+' municiones')

  def recargarArma(self,municiones):
    cargador=5
    cargador = cargador + municiones
    print('El personaje '+self.nombre+' recargó su arma y ahora tiene: '+str(cargador)+' municiones')