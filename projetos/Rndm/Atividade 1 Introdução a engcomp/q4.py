

def obter_numero(mensagem):
    while True:
        try:
            valor = int(input(mensagem))
            return valor
        except ValueError:
            print("Por favor, insira um número inteiro válido.")

# Solicita os números inicial e final
print("Digite os valores para o intervalo.")
while True:
    NI = obter_numero("Número inicial: ")
    NF = obter_numero("Número final: ")

    if NI <= NF:
        break
    else:
        print("O número inicial deve ser menor ou igual ao número final. Tente novamente.")

somaPares = 0
somaImpares = 0
qtdPrimos = 0

# Determina se o número é primo
def isPrimo(numero):
    if numero < 2:
        return False
    for i in range(2, int(numero / 2) + 1):
        if numero % i == 0:
            return False
    return True

i = NI
while NI <= i <= NF:
    print("i =", i)

    # Verifica se é ímpar ou par
    if i % 2 == 0:
        print('é par')
        somaPares += i
    else:
        print('é impar')
        somaImpares += i

    # Verifica se é primo
    if isPrimo(i):
        print("é primo")
        qtdPrimos += 1
    else:
        print("não é primo")

    i += 1

# Exibe os resultados
print(f"A sequência possui {qtdPrimos} números primos.\nA soma dos números pares na sequência é {somaPares}, enquanto a soma dos numeros ímapres é {somaImpares}.")