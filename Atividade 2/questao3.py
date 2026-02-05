def elementos_exclusivos(lista1, lista2):
    return list(set(lista1) ^ set(lista2))

entrada1 = input("digite a primeira lista de elementos separados por vírgula: ")
lista1 = [elem.strip() for elem in entrada1.split(",")]
entrada2 = input("digite a segunda lista de elementos separados por vírgula: ")
lista2 = [elem.strip() for elem in entrada2.split(",")]
resultado = elementos_exclusivos(lista1, lista2)    
print("elementos exclusivos nas duas listas:", resultado)