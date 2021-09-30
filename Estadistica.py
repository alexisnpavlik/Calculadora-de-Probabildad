from dataset import datos_sin_agrupar 
from dataset import datos_agrupados




global media_aritmetica
global mediana


def bus_media(dataset):
    suma=0
    for i in datos_sin_agrupar:
        suma+=i
    media_aritmetica=suma/len(datos_sin_agrupar)

def bus_mediana(datos_sin_agrupar):
    datos_sin_agrupar.sort()
    print(datos_sin_agrupar)

    if len(datos_sin_agrupar)%2 ==0:
        print("Es par")
        mediana=(datos_sin_agrupar[int(len(datos_sin_agrupar)/2)-1] + datos_sin_agrupar[int(len(datos_sin_agrupar)/2)])/2
        print("Su mediana es:",mediana)

    elif len(datos_sin_agrupar)%2 !=0:
        print("Es Impar")
        mediana=datos_sin_agrupar[int(((len(datos_sin_agrupar)+1)/2)-1)]
        print("Su mediana es:",mediana)

def run():
    bus_mediana(datos_sin_agrupar)

if __name__=="__main__":
    run()



