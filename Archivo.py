from sys import exit #Se importa exit
import re #Se importa re
import shutil #Se importa shutil para poder copiar el archivo

class Archivo: #Se crea la clase archivo
	def __init__(self,nombre): #Se define la clase
		try: #Si no se puede abrir el archivo no lo hace
			self.f = open(nombre, 'r') #Se abre el archivo con el modo solo lectura
			self.nombre=nombre #Se le asigna un nombre
		except: #Entra la excepcion en caso de que no se pueda abrir el archivo
			print("No se puede abrir el archivo ", nombre) 
			exit() #Sale del programa

	def muestra(self): #Se defina la funcion para mostrar el texto del archivo
		i = 1 #Variable i se iguala a 1
		for linea in self.f: #Se usa para recorrer linea por linea todo el archivo
			print("{:3}.-{}".format(i,linea)) #Imprime cada linea del archivo con un prefijo igual a el numero de la linea
			i+=1 #Se aumenta i
		print() #Se imprime un salto de linea
		self.f.seek(0) #Define a 0 la posicion en el texto del archivo

	def cuentaVocales(self): #Se defina la funcion para contar vocales
		def vocales(s):#Se define la funcion vocales y se asigna a la variable s
			contador = 0 #Contador igual a 0
			for i in range(len(s)): #Para recorrer todo el texto del archivo
				if s[i] in set("aeiouáéíóú"): #Compara si alguna vocal de las que se definen esta en la posicion i del texto si es asi entra en el if
					contador += 1 #Aumenta el contador en 1 en caso de que haya alguna vocal
			print("Vocales: ", contador) #Imprime el numero de vocales que hay en el texto
			return contador #Regresa el contador

		contador = 0 #Contador igual 0
		for linea in self.f: #Recorre el texto linea por linea
			contador += vocales(linea) #Aumenta el contador en 1
		self.f.seek(0) #Declara a 0 la posicion en el texto del archivo
		return contador #Regresa el contador

	def cuentaConsonantes(self): #Se define la funcion para contar consonantes
		def consonantes(s): #Se define la funcion consonantes y se asigna a la variable s
			contador = 0 #Contador igual a 0
			for i in range(len(s)): #Para recorrer todo el texto del archivo
				if s[i] in set("bcdfghjklmnñpqrstvwxyzBCDFGHJKLMNÑPQRSTVWXYZ"): #Compara si alguna consonantes de las que se definen esta en la posisicon i del texto si es asi entra el if
					contador += 1 #Aumenta el contador en 1 en case de que haya alguna consonante
			print("Consonantes: ", contador) #Imprime el numero de consonates que hay en el texto
			return contador #Regresa el contador
		contador = 0 #Contador igual a 0
		for linea in self.f: #Recorre el texto linea por linea
			contador += consonantes(linea) #Aumenta el contador en 1
		self.f.seek(0)#Declara a 0 la posicion en el texto del archivo
		return contador #Regresa el contador

	def cuentaEspacios(self): #Se define la funcion para contar espacios
		def espacios(s): #Se define la funcion espacios y se asigna a la variable s
			contador = 0 #Contador igual a 0
			for i in range(len(s)): #Para recorrer todo el texto del archivo
				if s[i] in set(" "): #Compara si algun espacio esta en la posicion i del texto si es que si entra el if
					contador += 1	#Aumenta el contador en 1 en caso de que haya algun espacio
			print("Espacios: ", contador) #Imprime el numero de espacios que hay en el texto
			return contador #Regresa el contador
		contador = 0 #Contador igual a 0
		for linea in self.f: #Recorre el texto linea por linea
			contador += espacios(linea) #Aumenta el contador en 1
		self.f.seek(0) #Declara a 0 en la posision en el texto del archivo
		return contador #Regresa el contador

	def cuentaSignos(self): #Se define la funcion para contar signos de puntuacion
		def signos(s): #Se define la funcion signos y se asgina a la variable s
			contador = 0 #Contador igual a 0
			for i in range(len(s)): #Para recorrer todo el tecto del archivo
				if s[i] in set(".,:;()*¿?![]-_"): #Compara si algun signo esta en la posicion i del texto si es que si entra en el if
					contador += 1	#Aumenta el contador en 1
			print("Signos de puntuacion: ", contador) #Imprime el numero de signos que hay en el texto
			return contador #Regresa el contador
		contador = 0 #Contador igual a 0
		for linea in self.f: #Recorre el texto linea por linea
			contador += signos(linea) #Aumenta el contador en 1
		self.f.seek(0) #Declara a 0 la posisicion en el texto del archivo
		return contador #Regresa el contador

	def cuentaPalabras(self):
		cadena2 = self.f.read()
		npalabras = 0
		np = cadena2.split()
		npalabras = len(np)
		print("Cantidad de palabras:",npalabras)

	def cuentaLineas(self):
		i = 0
		for linea in self.f:
			i += 1
		print("Numero de lineas: ", i)
		self.f.seek(0)
		
	def cuentaMayusculas(self):
		def mayusculas(s):
			contador = 0
			for i in range(len(s)):
				if s[i] in set("ABCDEFGHIJKLMNÑOPKRSTUVWXYZ"):
					contador += 1	
			print("Mayusculas: ", contador)
			return contador
		contador = 0
		for linea in self.f:
			contador += mayusculas(linea)
		self.f.seek(0)
		return contador

	def cuentaMinusculas(self):
		def minusculas(s):
			contador = 0
			for i in range(len(s)):
				if s[i] in set("abcdefghijklmnñopqrstuvwxyz"):
					contador += 1	
			print("Minusculas: ", contador)
			return contador
		contador = 0
		for linea in self.f:
			contador += minusculas(linea)
		self.f.seek(0)
		return contador

	def copyfile(self):
		fuente = "/home/kayle/Escritorio/UNI/8vo/Concurrente/PROGRAMAS/prueba.txt"
		destino = "/home/kayle/Escritorio/UNI/8vo/Concurrente/PROGRAMAS/pruebaCOPIA.txt"
		try:
			shutil.copyfile(fuente, destino)
			print("\nARCHIVO COPIADO CORRECTAMENTE\n")
		except:
			print("Error")

	def convierteMayuscula(self):
		print("###############################################################################\nTEXTO EN MAYUSCULAS:")
		for linea in self.f:
			print("{}".format(linea.upper()))
		print()
		self.f.seek(0)

	def convierteMinuscula(self):
		print("###############################################################################\nTEXTO EN MINUSCULAS:")
		for linea in self.f:
			print("{}".format(linea.lower()))
		print()
		self.f.seek(0)

	def Hexadecimal(self):
		s = self.f.read()
		print("Texto convertido a hexadecimal\n")
		for i in range(len(s)):
			print(hex(ord(s[i])))

nomb = input("Nombre del archivo  \n") #Se pregunta que archivo se va a abrir
archivo = Archivo(nomb) #
archivo.muestra() #Muestra el texto del archivo
archivo.cuentaVocales() #Muestra el numero de vocales
archivo.cuentaConsonantes() #Muestra el numeor de consonantes
archivo.cuentaEspacios() #Muestra el numeero de espacios
archivo.cuentaSignos() #Muestra el numero de signos
archivo.cuentaPalabras() #Muestra el numero de palabras
archivo.cuentaLineas() #Muestra el numero de lineos
archivo.cuentaMayusculas() #Muestra cuantas mayusculas hay en el texto
archivo.cuentaMinusculas() #Muestra cuantas minusculas hay en el texto
archivo.copyfile() #Copea el archivo a otro
archivo.convierteMayuscula() #Convierte el texto del archivo a pura letra mayuscula
archivo.convierteMinuscula() #Convierte el texto del archivo a pura letra minuscula
archivo.Hexadecimal() #Convierte el texto del archivo a hexadecimal
