import fractions

n = int(input("Ingrese el número de parejas ordenadas: " )) - 1 # n intervals
b = float(input("Último límite de integración: " ))  # Input the last limit of integration (x-axis normally)
a = float(input("Primer límite de integración: " ))  # Input the first limit of integration (x-axis nomalli)
delta_x = (b-a)/n  # Delta x
diccionario = {}  # In this dictionary would be all the couples
Resultado = 0  # Future variable

for i in range(n+1):  # get all the couples
    x = input("Valor x de la pareja ordenada: " ) # x axis
    try:     # See if x axis is a fraction
        if not x.isnumeric():
            x = fractions.Fraction(x)
    except ValueError:
        (x + "NO ES UN NÚMERO")
    doubleofx = float(x) 
    y = input("Valor y de la pareja ordenada: " ) # y axis
    try:    # see if y is a fraction
        if not y.isnumeric():
            y = fractions.Fraction(y)
    except ValueError:
        (y + "NO ES UN NÚMERO")
    doubleofy = float(y) 
    diccionario.update({doubleofx:doubleofy}) # Dictionary get updated by x and y

# sum the first and last value of the dictionary, then quit that values and the values rest multiply by 2 and sum to the final result
Resultado += diccionario.get(a)
diccionario.pop(a)
Resultado += diccionario.get(b)
diccionario.pop(b)
for i in diccionario.values():
    Resultado += i*2
Resultado *= delta_x/2
print(Resultado)

"""
⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣿⣶⣄⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⢀⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣦⣄⣀⡀⣠⣾⡇⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀
⠀⠀⠀⠀⢀⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⠿⢿⣿⣿⡇⠀⠀⠀⠀
⠀⣶⣿⣦⣜⣿⣿⣿⡟⠻⣿⣿⣿⣿⣿⣿⣿⡿⢿⡏⣴⣺⣦⣙⣿⣷⣄⠀⠀⠀
⠀⣯⡇⣻⣿⣿⣿⣿⣷⣾⣿⣬⣥⣭⣽⣿⣿⣧⣼⡇⣯⣇⣹⣿⣿⣿⣿⣧⠀⠀
⠀⠹⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠸⣿⣿⣿⣿⣿⣿⣿⣷⠀
"""
