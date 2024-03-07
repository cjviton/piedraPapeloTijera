import random

print("Bienvenido a piedra, papel o tijera. v 0.3")

def repetir():
    print ("1 =  Piedra")
    print ("2 =  Papel")
    print ("3 =  Tijera")


    tirada = int(input ("Escoge tu tirada: "))
    tiradaordenador = random.randint(1,3)



    if tiradaordenador == 1:
        print("El ordenador ha sacado Piedra")
    elif tiradaordenador == 2:
        print("El ordenador ha sacado Papel")
    elif tiradaordenador == 3:
        print("El ordenador ha sacado Tijera")

        
    if tirada == 1 and tiradaordenador == 1:
        print ("EMPATE")
    elif tirada == 1 and tiradaordenador == 2:
        print ("MÁQUINA GANA")
    elif tirada == 1 and tiradaordenador == 3:
        print ("JUGADOR GANA")
    elif tirada == 2 and tiradaordenador == 1:
        print ("JUGADOR GANA")
    elif tirada == 2 and tiradaordenador == 2:
        print ("EMPATE")
    elif tirada == 2 and tiradaordenador == 3:
        print ("MÁQUINA GANA")
    elif tirada == 3 and tiradaordenador == 1:
        print ("MÁQUINA GANA")
    elif tirada == 3 and tiradaordenador == 2:
        print ("JUGADOR GANA")
    elif tirada == 3 and tiradaordenador == 3:
        print ("EMPATE")

    repetir()
repetir()
