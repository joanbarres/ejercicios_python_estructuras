while(True):
    try:
        print("Escriu 5 numeros i el mostrare el mes gran, per finalitzar el prgrama escriu fi ")
        majorNumero = 0
        numero = 0
        valor = ""
        while(True):
            valor = input()
            if(valor == "fi"):
                break
            else:
                numero = int(valor)
                if(numero > majorNumero):
                    majorNumero = numero


        print(majorNumero)
        break
    except:
        print("Escriu numeros valids o la paraula fi")
