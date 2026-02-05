def filtrar_numeros(lista_numeros):
    return [num for num in lista_numeros if num % 2 == 1]

entrada = input("digite uma lista de números separados por vírgula: ")
lista_numeros = [int(num) for num in entrada.split(",")]
resultado = filtrar_numeros(lista_numeros)

print("números ímpares na lista:", resultado)
