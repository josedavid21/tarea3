import argparse
import time
from tabulate import tabulate

def cuentapalabras(lista):
  counts = {}
  for word in lista:
    if word not in counts:
      counts[word] = 0
    counts[word] += 1
  return counts

  
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
    print(tabulate({"Palabra": palabras, "Cantidad" : cuenta}, headers="keys"))
    tab.close()
  
def main3():
                #Definir argumentos de argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("file", help="ruta de archivo de texto por leer, por ejemplo home/cristofhersj/Documents/", type = str)
    parser.add_argument("save", help= "Guardar los resultados en un nuevo .txt, indique el nombre y la dirección del nuevo archivo junto con su extensión, por ejemplo: 'home/cristofhersj/Documents/texto.txt'.", type = str  )
    parser.add_argument("-t", "--time", help= "Tiempo de ejecución del método", action="store_true")
   
    args = parser.parse_args()
    if args.time:
      tiempoini = time.time_ns()            
      tabular(args.file,args.save)
      tiempofin = time.time_ns()           
      print("El tiempo transcurrido es de: ",str(tiempofin - tiempoini), "nanosegundos")
    else:
      tabular(args.file,args.save)          

if __name__ == '__main__':   
    main3()
