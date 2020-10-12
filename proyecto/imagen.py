#Tarea 3 Microcontroladores y microprocesadores
#Grupo Mendez, Rojas, Solís, Soto 
#Presentador de imágenes
#

#Para el manejo de imágenes se utiliza la biblioteca PIL (pillow)

from PIL import Image
import argparse
import time 

'''Para el script'''
parser= argparse.ArgumentParser(description= 'Presentador de imágenes')

#Se agrega argumento para manejar escala de presentación
parser.add_argument('escala', type=int, help= 'Se elige un número para determinar la escala de presentación en donde: 1 representa 1:1, 2 representa 1:2 y 3 representa 2:1')

#Con esto se agrega el argumento de direccion
parser.add_argument('direccion', type=str, help= 'Se escribe la ruta donde se encuentra la imagen que se desea presentar. Por ejemplo: /home/jose/Desktop/imagen.jpg')

#Bandera de tiempo de ejecución
parser.add_argument('--time', action= 'store_true' , help= 'Bandera que muestra el tiempo de ejecución del método')

#Para poder utilizar agumentos agregados
args = parser.parse_args()

#########################
'''Funcionamiento:  el siguiente método se encarga de desplegar en pantalla la imagen deseada (cuyo nombre se ingresa como parámetro "foto"), asimismo se puede elegir entre una presentación 1:1, 1:2, 2:1 según sea el parámetro "esc". Cabe destacar que se utilizan distintas funcionalidades de PIL, las cuales se explicarán brevemente según aparezcan en el código'''
'''
Entradas: 
	esc: puede tomar el valor de 0,1 o 2 según la escala que se desee para la presentación de la imagen. Donde 0 representa 1:1, 1 representa 1:2 y 2 representa 2:1.
	foto: representa la ruta de la imagen por representar. 
Salidas:
	Como salida se espera una imagen -la cual puede estar a escala o no respecto a la original- es importante rescatar que la función como tal retorna None.
'''
def presentadorimg(esc, foto):
	#escala 1:1
	imagen = Image.open(foto) 
	'''"Abre" e identifica la imagen y se la asigna a una variable, en este caso llamada imagen'''
	if esc == 1:
		imagen.show() 
		'''Despliega en pantalla la imagen'''
		tiempo_fin = time.time_ns()
	#escala 1:2	
	elif esc == 2:
		size = imagen.size 
		'''Le asigna a una variable una tupla la cual contiene los datos de ancho y altura -en dicho orden- de la imagen cargada'''
		'''La siguiente sección de códgo se encarga de escalar (en este caso 1:2) la imagen, se emplea la información de la tupla (se divide entre dos la anchura y altura, asimismo dicha información se asigna a variables). Importante destacar que se asegura que los parámetros de resize sean enteros'''
		###
		
		ancho = size[0] 
		altura = size[1]
		nuevoancho= int (ancho/2)
		nuevaaltura= int (altura/2)
		newimage = imagen.resize((nuevoancho,nuevaaltura)) 
		
		'''Le asigna a una variable la imagen ya modificada'''

		###
		
		newimage.show()
			
	#escala 2:1
	#Este caso es semejante al anterior, pero con una presentación 2:1
	elif esc == 3:
		size = imagen.size
		ancho = size[0]
		altura = size[1]
		nuevoancho= int (ancho*2)
		nuevaaltura= int (altura*2)
		newimage = imagen.resize((nuevoancho,nuevaaltura))
		newimage.show()
		
'''A continuación se presenta la sección main '''	
'''Se encarga de contener la función de presentador de imágenes, asimismo toma el tiempo de ejecución del método, en caso de haberlo solicitado mediante la bandera --time, lo imprime en pantalla '''
def Main():
	tiempo_ini = time.time_ns() #tiempo1
	#Llamada a función presentador de imágenes con parámetros
	#ingresados mediante argparse.
	
	presentadorimg(args.escala, args.direccion)
	
	tiempo_fin = time.time_ns() #tiempo2
	
	#Impresión de tiempo de ejecución del método (tiempo1-tiempo2)
	if args.time:
		print ("Tiempo de ejecución del método: ", str(tiempo_fin-tiempo_ini), "ns")
	
	
if __name__ == '__main__':	
	Main()
	
	
	
	
	
	
	
	
