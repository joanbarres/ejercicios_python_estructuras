while(True):
    try:
        print("Escriu 5 numeros i el mostrare el mes gran: ")
        count = 0
        majorNumero = 0

        while(count < 5):
            numero = int(input())
            if(majorNumero < numero):
                majorNumero = numero
            count = count + 1

        print(majorNumero)
        break
    except: 
        print("Introdueix numeros valids")