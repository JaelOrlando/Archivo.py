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

	def cuentaPalabras(self):#Se define la funcion para contar palabras
		cadena2 = self.f.read() #Se lee el texto del archivo
		npalabras = 0 #Se define un contador igual a 0 
		np = cadena2.split() #Sirve para dividir el texto por palabras
		npalabras = len(np) #Cuenta el numero de divisiones
		print("Cantidad de palabras:",npalabras) #Imprime el numero de palabras que hay en el texto

	def cuentaLineas(self): #Se define la funcion para contar lineas
		i = 0 #Se crea un contador igual a 0
		for linea in self.f: #Sirve para que recorra el texto linea por linea
			i += 1 #Aumenta el contador si es que cambia una linea
		print("Numero de lineas: ", i) #Imprime el numero de lineas que hay en el texto
		self.f.seek(0) #Se define el inicio en del texto en la posicion 0
		
	def cuentaMayusculas(self): #Se define la funcion que cuenta mayusculas
		def mayusculas(s): #Se define la funcion mayusculas y se le asigna a la variable s
			contador = 0 #Contador igual a 0
			for i in range(len(s)): #Para recorrer todo el texto del archivo
				if s[i] in set("ABCDEFGHIJKLMNÑOPKRSTUVWXYZ"): #Compara si alguna letra mayuscula esta en la posicion i si es asi entra el if
					contador += 1	#Aumenta el contador en 1 en caso de que haya alguna mayuscula
			print("Mayusculas: ", contador) #Imprime cuantas mayusculas hay en el texto
			return contador #Regresa el contador
		contador = 0 #Contador igual a 0 
		for linea in self.f: #Recorre el texto linea por linea
			contador += mayusculas(linea) #Aumenta el contador en 1
		self.f.seek(0) #Define el inicio del texto en la posicion 0
		return contador  #Regresa el contador

	def cuentaMinusculas(self): #Se define la funcion cuenta minusculas
		def minusculas(s): #Se define la funcion minusculas y se le asgina a la variable s
			contador = 0 #Contador igual a 0
			for i in range(len(s)): #Para recorrer todo el texto deñ archivo
				if s[i] in set("abcdefghijklmnñopqrstuvwxyz"): #Compara si alguna letra minuscula esta en la posicion i si es asi entra el if
					contador += 1	#Aumenta el contador
			print("Minusculas: ", contador) #Imprime cuantas minusculas hay en el texto
			return contador #Regresa el contador
		contador = 0 #Contador igual a 0
		for linea in self.f: #Recorre el texto linea por linea
			contador += minusculas(linea) #Aumenta el contador en 1
		self.f.seek(0) #Define el inicio del texto en la posicion 0
		return contador #Regresa el contador

	def copyfile(self): #Se define la funcion copyfile
		fuente = "/home/kayle/Escritorio/UNI/8vo/Concurrente/PROGRAMAS/prueba.txt" #Se pone la ruta del archivo a copia
		destino = "/home/kayle/Escritorio/UNI/8vo/Concurrente/PROGRAMAS/pruebaCOPIA.txt" #Se ingresa la ruta a donde se va a copiar el archivo
		try: #Si no encuentra el archivo no lo hace
			shutil.copyfile(fuente, destino) #Se utiliza la funcion shutil con los parametros fuente y destino
			print("\nARCHIVO COPIADO CORRECTAMENTE\n") #Arroja un mensaje que se a copiado correctamente
		except: #Si no encuentra el archivo manda error
			print("Error") #Imprime error

	def convierteMayuscula(self): #Se define la funcion para convertir todo el texto a mayusculas
		print("###############################################################################\nTEXTO EN MAYUSCULAS:") #Se imprime el mensaje para diferenciar desde donde las convierte
		for linea in self.f: #Recorre el texto linea por linea
			print("{}".format(linea.upper())) #Imprime el texto ya en mayusculas utilizando la funcion upper
		print() #Imprime un salto de linea
		self.f.seek(0) #Define el inicio del texto en la posicion 0

	def convierteMinuscula(self): #Se define la funcion para convertir todo el texto a minusculas
		print("###############################################################################\nTEXTO EN MINUSCULAS:") #Se imprime el mensaje para deferenciar desde donde las convierte
		for linea in self.f: #Recorre el texto linea por linea
			print("{}".format(linea.lower())) #Imprime el texto ya en minusculas utilizando la funcion lower
		print() #Imprime un salto de linea
		self.f.seek(0) #Define el inicio del texto en la posicion 0

	def Hexadecimal(self): #Se define la funcion hexadecimal
		s = self.f.read() #Se le asigna a la variable s el texto del archivo
		print("Texto convertido a hexadecimal\n") #Se imprime un mensaje para saber desde donde convirtio a hexadecimal
		for i in range(len(s)): #Para recorrer todo el texto 
			print(hex(ord(s[i]))) #Convierte la posicion i del texto a formato hexadecimal

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
