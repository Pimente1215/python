def sum(a,b):
    print(f" la suma de los numeros es:{a+b}" )
    
def res(a,b):
        print(f" la resta de los numeros es:{a-b}" )
    
def mult(a,b):
        print(f" la multiplicacion de los numeros es:{a*b }" )
    
def div(a,b):
        print(f" la divicion  de los numeros es:{a/b}" )

    
## menu

while(True):
        print("Bienvenido a tu calaculadora de confianza")
        x = int (input("Ingresa el primer numero:"))
        y = int (input("Ingresa el segundo numero:"))
        print("Qué operacion quieres realizar")
        print("Escribe 1: para sumar")
        print("Escribe 2: para restar")
        print("Escribe 3: para multiplicar")
        print("Escribe 4: para dividir")

        response = int(input("Ingresa tu opción:"))

        if response == 1:
            sum(x,y)
        elif response == 2:
            res(x,y)
        elif response ==3:
            mult (x,y)
        elif response == 4:
            div(x,y)
        elif response == 5:
            break
        else:
            print("Chistosito va!")
