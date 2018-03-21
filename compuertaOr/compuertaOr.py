entradaA = (0, 0, 1, 1)
entradaB = (0, 1, 0, 1)
pesos = (-10, 20, 20)

print('ECUACION')
print('g({} + {}x1 + {}x2)'.format(pesos[0], pesos[1], pesos[2]))
print('')

for a in entradaA:
    for b in entradaB:
        salida = pesos[0] + (20 * a + (20 * b))
        print('g(-10 + 20('+str(a)+') + 20('+str(b)+')) = '+str(salida))
        
        if salida<0:
            print('SALIDA = 0')
            print('')
        else:
            print('SALIDA = 1')
            print('')
