# Importando las librerías neceasias
import argparse
import time 
from playsound import playsound

parser = argparse.ArgumentParser()
parser.add_argument("Dir",help="La dirección donde se encuentra el archivo mp3 que se desea reproducir incluyendo a este último, por ejemplo: /home/cristofhersj/Music/Sound.mp3",type=str)
parser.add_argument("num",help="El número de veces que desee reproducir el archivo mp3",type=int)
parser.add_argument("-t", "--time", help= "Es el tiempo de ejecución del método. ", action="store_true")
args= parser.parse_args()


# Se define la función que reproduce el sonido entradas: 
# Dir: la dirección del mp3 por reproducir, 
# NUM: la cantidad de veces que se desea reproducir
# Salidas: Se reproduce el .mp3 seleccionado

def Presentador_de_sonido(Dir, NUM):
    for i in range(NUM):
        NOMBRE_ARCHIVO = str(Dir)
        playsound(NOMBRE_ARCHIVO)
        
# Se define la función principal que contiene el scripting y ejecuta 
# las funciones dependiendo de si se pide el tiemmpo de ejecución o no 
def main2():
    if args.time:
        tiempoini = time.time_ns() 
        Presentador_de_sonido(args.Dir,args.num)
        tiempofin = time.time_ns()
        print("El tiempo transcurrido es de: ",str(tiempofin - tiempoini), "nanosegundos")
    else: 
        Presentador_de_sonido(args.Dir,args.num)
    
if __name__ == "__main__":
    main2()
