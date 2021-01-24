#Jose Pablo Ponce, 19092
#06-03-19
#condicionales2_ejercicio1
#Crear un programa donde se ingrese un numero en base 64 y lo traduzca al abecedario o vicebersa


#crear listas de abecedario y base 64
lista_nombres=['A','B','C','D','E','F','G','H','I','J','K','L', 'M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z', " "]
lista_morse = ["00","01","02","03","04","05","06,","07","08","09","10","11","12","13","14","15","16","17","18","19","20","21","22","23","24","25", "  "]

#mostrar menu
print ("Bienvenido")
cifrar = print ("1. cifrar")
descifrar = print ("2. descifrar")
salir = print ("3. salir")
opcion= input("ingrese opcion")
#volver opcion a entero
opcion = int (opcion)
#crear opcion si se ingresa el cifrar
if opcion == 1:
     
    mensaje=input("Ingrese un mensaje a cifrar: ")
#convertimos el mensaje en mayusculas
    mensajeM=mensaje.upper()
#Contamos cuantas letras tiene el mensaje     
    tamaño_mensaje=len(mensajeM)
#mostrar mensaje de cual es la traduccion     
    print("El mensaje en base64 es: ")
     
#buscar en la nueva variablee de mensaje
    for letras in range(tamaño_mensaje):

        unoxuno=mensajeM[letras]
     
        if unoxuno in lista_nombres:
    
            posicion_letra=lista_nombres.index(unoxuno)
     
            morse=lista_morse[posicion_letra]
     
     
            print(morse,end=' ')
        else:
            print("ERROR NO INGRESO CARACTERES CORRECTOS")

#realizar mismo procedimiento de manera invertida a la opcion 1
elif opcion ==2:
    
    
      
    mensaje=input("Ingrese un mensaje a cifrar: ")
#convertimos el mensaje en mayusculas
    mensajeM=str(mensaje)
#Contamos cuantas letras tiene el mensaje
    tamaño_mensaje=len(mensajeM)
     
    print("El mensaje en base64 es: ")
     
     
    for letras in range(0, tamaño_mensaje, 2):


        unoxuno=mensajeM[letras]+mensajeM[letras+1]
     
        if unoxuno in lista_morse:
     
            posicion_letra=lista_morse.index(unoxuno)
     
            nombres=lista_nombres[posicion_letra]
     
     
            print(nombres,end=' ')
        else:
            print("ERROR NO INGRESO CARACTERES CORRECTOS")
            
     
#salir del programa    
elif opcion ==3:
    exit



    
   