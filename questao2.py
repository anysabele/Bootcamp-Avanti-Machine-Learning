def filtras_numeros_primos(lista_numeros):
    def eh_primo(num):
        if num < 2:
            return False
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                return False
        return True

    return [num for num in lista_numeros if eh_primo(num)]

entrada = input("digite uma lista de números separados por vírgula: ")
lista_numeros = [int(num) for num in entrada.split(",")]
resultado = filtras_numeros_primos(lista_numeros)
print("números primos na lista:", resultado)