from Ciclista import Ciclista
ciclistas=[]
ciclista = Ciclista()

respuesta= "y"
while(respuesta=="y"):
	ciclista.nombre = input("Nombre: ")
	ciclista.edad =int(input("Edad: "))
	ciclista.pais = input("Pais: ")
	ciclista.tiempo = int(input("Tiempo: "))
	cicli=dict(nombre=ciclista.nombre,edad=ciclista.edad,pais=ciclista.pais,tiempo=ciclista.tiempo)
	ciclistas.append(cicli)
	respuesta= input("Desea ingresar otro ciclista(y/n): ")

print(ciclista.clasificar(ciclistas))