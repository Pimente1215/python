sum = lambda a,b: a + b 
rest = lambda a,b: a-b
mult = lambda a,b: a*b
div = lambda  a,b: a/b


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
            print("sum(x,y)") 
        elif response == 2:
            print ("res(x,y)")
        elif response ==3:
            print ("mult(x,y)")
        elif response == 4:
            print ("div(x,y)")
        elif response == 5:
            break
        else:
            print("Chistosito va!")
