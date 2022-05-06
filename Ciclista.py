class Ciclista:

	#creando el constructor
	def __init__(self):
		self.__nombre = None
		self.__edad = None
		self.__pais = None
		self.__tiempo = None
	
	#Metodos get
	@property
	def nombre(self):
		return self.__nombre
	
	@property
	def edad(self):
		return self.__edad

	@property
	def pais(self):
		return self.__pais

	@property
	def tiempo(self):
		return self.__tiempo
	
	@nombre.setter
	def nombre(self,nombre):
		while True:
			try:
				nombre = int(nombre)
				print("El nombre debe ser un texto")
				nombre = input("Repita el nombre ")
			except:		
				self.__nombre =nombre
				break
		
	@edad.setter
	def edad(self,edad):
		while True:
			try:
				if (edad<0):
					print("Digite edad valida")
					edad = input("Repita la edad ")
			except:		
				self.__edad =edad
				break
		
			

	@nombre.setter
	def pais(self,pais):
		while True:
			try:
				pais = int(pais)
				print("El pais debe ser un texto")
				pais = input("Repita el pais ")
			except:		
				self.__pais =pais
				break
	
	@tiempo.setter
	def tiempo(self,tiempo):
		while True:
			try:
				if (tiempo<0):
					print("Digite tiempo valida")
					tiempo = input("Repita la tiempo ")
			except:		
				self.__tiempo =tiempo
				break


	def clasificar(self,ciclistas):
		time=ciclistas[0].get('tiempo')
		for ciclista in  ciclistas:
			if(ciclista.get('tiempo') < time):
				time = ciclista.get('tiempo')
		print(f"El ganador es {ciclista.get('nombre')} con un tiempo de {time} minutos")

