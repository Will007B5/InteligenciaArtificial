from math import sqrt

moda = []
lista = []
mediana = []


with open("numeros.txt","r") as f:
 lista = f.readlines()
 media = lista[0].split(",")
 moda = lista[1].split(",")
 mediana = lista[2].split(",")

varianza = [13,14,15,15,15,16,17,18,20]

#OBTENCION DE MEDIA
contador = 0
max_index = len(media)-1
m = 0
while contador <=max_index:
    m+=int(media[contador])+int(media[contador+1])
    contador = contador+2    
print("media:",m/len(media))



#MODA
rep = 0
modas = []
for m in moda:
 maximo = moda.count(m)
 if maximo > rep:
     rep = maximo
     
for m in moda:
    maximo = moda.count(m)
    if maximo == rep and m not in modas:
        modas.append(m)
print ("moda:", modas)

#MEDIANA

mediana.sort()
print(mediana)

if len(mediana)%2==0:
    tam = int(len(mediana)/2)
    m = (int(mediana[tam-1])+int(mediana[tam]))/2
else:
    m = mediana[int(len(mediana)/2)]
print("mediana:",m)




##VARIANZA Y MEDIA

contador = 0
max_index = len(varianza)-1
m = 0
cuadrados = []

while contador < max_index:
    m+=int(varianza[contador])+int(varianza[contador+1])
    contador = contador+2    
    real_media = m/len(varianza)
print("Media real: ",real_media)
for v in varianza:
    cuadrados.append((v-real_media)**2)

contador = 0
max_index = len(cuadrados)-1
m = 0

while contador < max_index:
    m+=int(cuadrados[contador])+int(cuadrados[contador+1])
    contador = contador+2    
print("varianza:",m/len(cuadrados),"\n","Desviación Estándar: ",sqrt(m/len(cuadrados)))
