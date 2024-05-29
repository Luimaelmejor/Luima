vocales=["a","e","i","o","u"]
nombre=input("Introduzca su nombre: ") 
numeroVoc=0 

for item in list(nombre):
    
 if item in vocales:
    numeroVoc+=1

if numeroVoc>=3:
    print(nombre)
else:
    print("No tiene 3 vocales")
    