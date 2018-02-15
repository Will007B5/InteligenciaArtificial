cont1=0
cont2=0
xPorT=[]
mtsCuad=[]
x=[5,15,20,25]
t=[375,487,450,500]
addX= sum(x)
addT= sum(t)

print ('|MetrosCuadrados(X)|Precio(t)|')
print ('|        5         |   375   |')
print ('|       15         |   487   |') 
print ('|       20         |   450   |')
print ('|       25         |   500   |')

for a in x:
    xPorT.append(x[cont1] * t[cont1])
    cont1=cont1+1
addMulti= sum(xPorT)

for b in x:
    mtsCuad.append(x[cont2]**2)
    cont2=cont2+1
addCuad= sum(mtsCuad)

despejem1=(addMulti-((addX*addT)/len(x)))
despejem2=addCuad-((addX)**2/len(x))

pendiente= despejem1/despejem2
print ('Pendiente:',pendiente)

despejeb=addT/len(x)-(pendiente)*addX/len(x)
print ('Interseccion:',despejeb)

pred=despejeb+(pendiente*35)
print ('Prediccion para casa de 35 metros:',pred)
pause = raw_input('Pulse ENTER para continual')
