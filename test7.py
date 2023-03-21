"""crear una función que reciba como parametro un string e indique si es un palindromo
  si no lo es indicar si eliminando 1 caracter pdoria ser un palindromo
"""

strInput = input("Inserte una frase : ")
def palindromo(strInput):
    strOrigin = strInput.replace(" ", "")
    strOutput = strInput[::-1].replace(" ", "")
    
    if ( strOrigin == strOutput):
        print("La frase es palindromo")
    else:
        for i in range(0,len(strOrigin),1):
            listOrigin = list(strOrigin)
            del listOrigin[i]
            print(listOrigin)
            if listOrigin == listOrigin[::-1]:
                print("quitando un caracter es palindromo")
                break

palindromo(strInput)

""" radaro 

adaro
rdaro
rdro
radar

"""