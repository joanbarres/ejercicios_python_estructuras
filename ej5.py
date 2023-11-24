
credencialUsuari = "root"
credencialContrasenya = "toor"
intentsRestants = 3

while (intentsRestants > 0):
    intentsRestants = intentsRestants - 1
    usuari = input("Usuari: ")
    contrasenya = input("Contraseña: ")
    if(usuari == credencialUsuari  and contrasenya == credencialContrasenya):
        print("Benvingut")
        break
    else:
        print("Usuari o contrasenya incorrectes, el queden ", intentsRestants, " intents restants" )
else:
    print("Introdueix numeros valids")