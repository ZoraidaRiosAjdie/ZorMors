from sys import argv
fe = open(argv[1],"r")
mensaje = fe.read().strip()
lista1=['A','B','C','D','E','F','G','H','I','J','K','L', 'M','N','Ñ','O','P','Q','R','S','T','U','V','W','X','Y','Z']
lista2 = ['.-','-...','-.-.','-..','.','..-.','--.','....','..','.---','-.-','.-..','--','-.','--.--','---', '.--.',
               '--.-','.-.','...','_','..-','...-','.--','-..-','-.--','--..']
codigo=[]
men=mensaje.upper()
tamaño=len(men)
print("el texto en codigo morse es: ",end=' ')
for i in range(tamaño):
    uno=men[i]
    if uno in lista1:
        posicion=lista1.index(uno)
        morse=lista2[posicion]
        codigo.append(morse)
        print(morse,end="")
        mensaje = fe.read().strip()
fe.close()