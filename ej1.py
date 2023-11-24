while(True):
    try:
        valorUsuari= int(input("Introduce un numero: "))
        if valorUsuari > 0:
          print("Es un numero positiu")
        elif valorUsuari < 0:
          print("Es un numero negatiu")
        else:
          print("Es igual a 0")
        break
    except:
        print("Introdueix numeros valids")