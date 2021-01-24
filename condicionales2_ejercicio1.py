#Jose Pablo Ponce, 19092
#06-03-19
#condicionales2_ejercicio1
#Crear un programa donde se ingrese el nombre de una pareja de perros y me indique el nivel de compatibilidad
vocales =("aeiouAEIOU")
#vueltas = True
#while vueltas :

perro1= input ("ingrese nombre de perro 1")
perro2= input ("ingrese nombre de perro 2")

perrofinal = perro1+perro2
print (perrofinal)
contador=0
contador2=0
for letra in perrofinal:
    contador +=1
    if letra in vocales:
        contador2 +=1
print (contador)
print (contador2)

print (contador2 / contador * 100) 


