def ordenar_por_nome(lista_pessoas):
    return sorted(lista_pessoas, key=lambda x: x[0])

#coletando dados do usuário
n = int(input("quantas pessoas deseja inserir?"))
lista_pessoas = []

for i in range(n):
    nome = input(f"Nome da pessoa {i+1}: ")
    idade = int(input(f"Idade de {nome}: "))
    lista_pessoas.append((nome, idade))

#ordenando e mostrando resultado
ordenado = ordenar_por_nome(lista_pessoas)
print("\nLista ordenada pelo nome:")
for nome, idade in ordenado:
    print(f"{nome}: {idade} anos")