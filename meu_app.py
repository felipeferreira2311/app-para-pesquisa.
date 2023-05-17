
print("hello word")


contador_ios = 0
contador_android = 0
soma_idades = 0
quantidade_entrevistados = 0

while True:
    resposta = input("Qual sistema operacional é utilizado em seu celular? (iOS ou Android): ")
    if resposta.lower() == "ios":
        contador_ios += 1
    elif resposta.lower() == "android":
        contador_android += 1

    idade = int(input("Qual a sua idade? "))
    soma_idades += idade

    quantidade_entrevistados += 1

    resposta_encerramento = input("Deseja encerrar a pesquisa? (s/n): ")
    if resposta_encerramento.lower() == "s":
        break

idade_media = soma_idades / quantidade_entrevistados

print("Resultados da pesquisa:")
print("Quantidade de entrevistados:", quantidade_entrevistados)
print("Quantidade de usuários iOS:", contador_ios)
print("Quantidade de usuários Android:", contador_android)
print("Idade média dos entrevistados:", idade_media)
