def encontrar_segundo_maior(lista_numeros):
    numeros_unicos = list(set(lista_numeros))
    numeros_unicos.sort()
    if len(numeros_unicos) < 2:
        return None
    return numeros_unicos[-2]

entrada = input("digite uma lista de números separados por vírgula: ")
lista_numeros = [int(num) for num in entrada.split(",")]
resultado = encontrar_segundo_maior(lista_numeros)
print("o segundo maior número na lista é:", resultado)