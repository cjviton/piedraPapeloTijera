import random

print ("1 =  Piedra")
print ("2 =  Papel")
print ("3 =  Tijera")


tirada = input ("Escoge tu tirada: ")

tiradaordenador = random.randint(1,3)



if tiradaordenador == 1:
    print("El ordenador a sacado Piedra")
elif tiradaordenador == 2:
    print("El ordenador a sacado Papel")
elif tiradaordenador == 3:
    print("El ordenador a sacado Tijera")

    
