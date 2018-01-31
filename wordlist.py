fichero = open('myWordlist.txt','w')

numero_Inicial = 5000000000
numero_Final =   6000000000

while numero_Inicial != numero_Final:

    numero_Inicial += 1
    fichero.write(str(numero_Inicial) + "\n")

fichero.close()