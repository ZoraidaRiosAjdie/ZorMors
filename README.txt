
# ZorMors
--------------------------------------------------------------------------------------------------------------------------------
-------------------------------------------------CONVERSOR A LENGUAJE MORSE-----------------------------------------------------
--------------------------------------------------------------------------------------------------------------------------------
Abstract:
Se trata de un código diseñado en lenguaje python que permite la traducción de textos en lenguaje castellano.

--------------------------------------------------------------------------------------------------------------------------------
--------------------------------------------------------EXPLICACIÓN-------------------------------------------------------------
--------------------------------------------------------------------------------------------------------------------------------

Se carga el módulo sys:
--------------------------------------------------------------------------------------------------------------------------------
1 from sys import argv
--------------------------------------------------------------------------------------------------------------------------------
Se utiliza para abrir el fichero 
Crear una variable, en este caso llamado mensaje.En la que le decimos que lea el fichero
--------------------------------------------------------------------------------------------------------------------------------
2 fe = open(argv[1],"r")
3 mensaje = fe.read().strip()
--------------------------------------------------------------------------------------------------------------------------------
Se crean dos listas una con las letras grecolatinas en mayúsculas, y la otra con el código morse que queramos
--------------------------------------------------------------------------------------------------------------------------------
4 lista1=['A','B','C','D','E','F','G','H','I','J','K','L', 'M','N','Ñ','O','P','Q','R','S','T','U','V','W','X','Y','Z']
5 lista2 = ['.-','-...','-.-.','-..','.','..-.','--.','....','..','.---','-.-','.-..','--','-.','--.--','---', '.--.',
               '--.-','.-.','...','_','..-','...-','.--','-..-','-.--','--..']
--------------------------------------------------------------------------------------------------------------------------------
Creamos una lista más, llamda codigo que mas adelante se ha utilizado. Después se crea una variable que hace que mensaje entero
se ponga en mayúsculas, para poder que coincidan con la lista de letras grecolatinas. Tras eso, ponemos una variable, que he
llamado tamaño, para que contanga la longitud de del mensaje con las letras en mayuscula. 
--------------------------------------------------------------------------------------------------------------------------------
6 codigo=[]
7 men=mensaje.upper()
8 tamaño=len(men)
--------------------------------------------------------------------------------------------------------------------------------
Como complemento ponemos un print con el mensaje. Tras eso ponemos un bucle for para recorrer la longitud del texto con cada una
de las letras se observa mediante las listas anteriormente definidas la letra correspondiente, al estar las listas ordenadas la 
sustitucion de una letra se reduce a buscar la misma posicion en las lista de simbolos morse, finalmente se muestra por pantalla 
la traducción de la letra a morse.
--------------------------------------------------------------------------------------------------------------------------------
9 print("el texto en codigo morse es: ",end=' ')
10 for i in range(tamaño):
11     uno=men[i]
12     if uno in lista1:
13         posicion=lista1.index(uno)
14         morse=lista2[posicion]
15         codigo.append(morse)
16         print(morse,end="")
17         mensaje = fe.read().strip()
--------------------------------------------------------------------------------------------------------------------------------
Finalmente se cierra el archivo de donde se encuentra el texto
--------------------------------------------------------------------------------------------------------------------------------
18 fe.close()
--------------------------------------------------------------------------------------------------------------------------------

--------------------------------------------------------------------------------------------------------------------------------
-----------------------------------------------------------Requisitos-----------------------------------------------------------
--------------------------------------------------------------------------------------------------------------------------------
-Hace falta tener tanto el programa t.py como el fichero file.txt en el mismo directorio
-Hace falta tener un interprete python(es recomendado tener la version 3.7)
-Hace falta instalado tener el paquete build-essentials
---------------------------------------------------------------------------------------------------------------------------------
-----------------------------------------------------------Ejecución-------------------------------------------------------------
---------------------------------------------------------------------------------------------------------------------------------
-Para ejecutarlo, hay que hacerlo desde la terminal
-el comando a introducir, una vez en el directorio del script es:
	~$ py t3.py file.txt
-el script saldra por pantalla, en la misma terminal
