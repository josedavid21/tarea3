# importando las librerías necesarias
import argparse
import time
from tabulate import tabulate
# función para contar las palabras, 
# entradas: lista extraída del .txt
# salidas: Cantidad de palabras (int)

def cuentapalabras(lista):
  counts = {}
  for word in lista:
    if word not in counts:
      counts[word] = 0
    counts[word] += 1
  return counts

# función para tabular los datos extraídos:
# entradas: dirección del archivo por leer y 
# dirección del archivo por crear y guardar
# salidas: txt de la tabla realizada
def tabular(direccion,salvar):
    
    
    simbolos = '¡!¿?.,:;-=<>*»'
    lista = []
    counts = {}
    palabras = []
    cuenta = []


    with open(direccion,'r') as f:
        lista = "".join(l for l in f.read())         
        lista = lista.split("_")                                          #Cada palabra, separada por "_", lo une a lista

    for i in range(len(lista)):
        for character in simbolos:                                        #No distingue mayúsculas y los simbolos los ignora
            lista[i] = lista[i].replace(character,"").lower()
    counts = cuentapalabras(lista)

        
    tab = open(salvar,"w+")
    for word, count in counts.items():
      palabras.append(word)
      cuenta.append(count)
    tab.write( tabulate({"Palabra": palabras, "Cantidad" : cuenta}, headers="keys"))
    tab.close()
# Función principal   
def main3():
    #Definir argumentos de argparse
    parser = argparse.ArgumentParser()
    parser= argparse.ArgumentParser(description= 'Permite contar cada palabra de un archivo .txt y genera otro archivo txt con una tabla que dice la cantidad de cada palabra. IMPORTANTE: Las palabras estan separadas por un _ y no hay cambios de línea')
    parser.add_argument("file", help="Es la ruta de archivo de texto por leer, indique el nombre y la dirección, por ejemplo home/cristofhersj/Documents/texto.txt", type = str)
    parser.add_argument("save", help= "Guardar los resultados en un nuevo .txt, indique el nombre y la dirección del nuevo archivo junto con su extensión, por ejemplo: 'home/cristofhersj/Documents/texto.txt'.", type = str  )
    parser.add_argument("-t", "--time", help= "Tiempo de ejecución del método", action="store_true")
    args = parser.parse_args()
    # Se implementa la función para medir el tiempo 
    # utilizado según se pida por el usuario o no
    if args.time:
      tiempoini = time.time_ns()            
      tabular(args.file,args.save)
      tiempofin = time.time_ns()           
      print("El tiempo transcurrido es de: ",str(tiempofin - tiempoini), "nanosegundos")
    else:
      tabular(args.file,args.save)          

if __name__ == '__main__':   
    main3()
