numeroInici= int(input("Escriu un numero: "))
numeroFinal= int(input("Escriu altre numero: "))
resultatParells = 0
resultatImparells = 0

while(numeroInici <= numeroFinal):
  if numeroInici % 2 == 0:
    resultatParells = resultatParells + numeroInici
  else:
    resultatImparells = resultatImparells + numeroInici
  numeroInici = numeroInici+1


print("La suma dels numeros parells es: ", resultatParells) 
print("La suma dels numeros imparells es: ", resultatImparells)