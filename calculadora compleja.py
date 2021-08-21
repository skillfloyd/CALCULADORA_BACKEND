#calculadora con validacion backend

primero=input('Ingrese primer número: ')

try:
    primero=int(primero)
except:
    primero='te hackeo prro'

if primero=='te hackeo prro':
    print('El valor ingresado no es un entero')
    exit()

segundo=input('Ingrese segundo número: ')

try:
    segundo=int(segundo)
except:
    segundo='te hackeo prro'

if segundo=='te hackeo prro':
    print('El valor ingresado no es un entero')
    exit()

simbolo=input('ingrese operación: ')

if simbolo=='+':
    print('Suma:', primero+segundo)
elif simbolo == '-':
    print('Resta:', primero-segundo)
elif simbolo == '*':
    print('Multiplicación:', primero*segundo)
elif simbolo == '/':
    print('División:', primero/segundo)
else:
    print('El símbolo ingresado no es válido')

