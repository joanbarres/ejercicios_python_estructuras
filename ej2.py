while(True):
    try: 
        numeroInici= int(input("Escriu un numero"))
        numeroFinal= int(input("Escriu altre numero"))
        resultat = 0

        while(numeroInici <= numeroFinal):
          resultat += numeroInici
          numeroInici = numeroInici+1
          print(resultat)
        break
    except:
        print("Introdueix numeros valids")
 