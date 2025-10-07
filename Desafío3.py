""" #Mi intento
largest_num = None
for num in [34, 28, 19, 11, 60, 29, 56]:
    if num > largest_num: #Error 
        largest_num = num
    print(largest_num) """

#Con ayuda IA
largest_num = None
for num in [34, 28, 19, 11, 60, 29, 56]:
    if largest_num is None or num > largest_num:
        largest_num = num
    print(largest_num)


#Ayuda con IA
def longitud(valor):
    if type(valor) is not list and type(valor) is not str:
        return -1
    contador = 0
    for elemento in valor:
        contador += 1
        return contador

cadena = input ("Ingresa la frase que necesitas medir: ")
print("Longitud de cadena:", longitud(cadena))
