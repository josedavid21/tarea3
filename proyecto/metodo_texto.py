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
  
def main():
    #Definir argumentos de argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("file", help="archivo de texto")
    parser.add_argument("-t", "--time", help= "Tiempo de ejecución del método", action="store_true")
    args = parser.parse_args()
    
    simbolos = '¡!¿?.,:;-=<>*»'
    lista = []
    counts = {}
    palabras = []
    cuenta = []

    tiempoini = time.time_ns()

    with open(args.file,'r') as f:
        lista = "".join(l for l in f.read())         
        lista = lista.split("_")                                          #Cada palabra, separada por "_", lo une a lista

    for i in range(len(lista)):
        for character in simbolos:                                        #No distingue mayúsculas y los simbolos los ignora
            lista[i] = lista[i].replace(character,"").lower()


    if args.time:
        counts = cuentapalabras(lista)

        tiempofin = time.time_ns()
        
        print("El tiempo transcurrido es de: ",str(tiempofin - tiempoini), "nanosegundos")
        
    else: 
        counts = cuentapalabras(lista)

        

    for word, count in counts.items():
      palabras.append(word)
      cuenta.append(count)
    print (tabulate({"Palabra": palabras, "Cantidad" : cuenta}, headers="keys"))            #tabula las palabras y su cuenta

if __name__ == '__main__':
    main()
