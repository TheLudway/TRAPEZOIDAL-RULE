import fractions

n = int(input("Ingrese el número de parejas ordenadas: " )) - 1 # n intervals
b = float(input("Último límite de integración: " ))  # Input the last limit of integration (x-axis normally)
a = float(input("Primer límite de integración: " ))  # Input the first limit of integration (x-axis nomalli)
delta_x = (b-a)/n  # Delta x
diccionario = {}  # In this dictionary would be all the 
Resultado = 0  # Se asigna un resultado con una variable para poder manipular a futuro

for i in range(n+1):  # Se pide que se repita la acción de pedir datos n número de veces
    x = input("Valor x de la pareja ordenada: " ) # Se pide la coordenada x
    try:     #Verificación del x para ver si es una fracción o no
        if not x.isnumeric():
            x = fractions.Fraction(x)
    except ValueError:
        (x + "NO ES UN NÚMERO")
    doubleofx = float(x) 
    y = input("Valor y de la pareja ordenada: " ) # Se pide la coordenada y
    try:    #Verificación del y para ver si es una fracción o no
        if not y.isnumeric():
            y = fractions.Fraction(y)
    except ValueError:
        (y + "NO ES UN NÚMERO")
    doubleofy = float(y) 
    diccionario.update({doubleofx:doubleofy}) # x and y se almacenan en el diccionario

#OPERACIÓN PARA LA REGLA DEL TRAPECIO
Resultado += diccionario.get(a)
diccionario.pop(a)
Resultado += diccionario.get(b)
diccionario.pop(b)
for i in diccionario.values():
    Resultado += i*2
Resultado *= delta_x/2
print(Resultado)
