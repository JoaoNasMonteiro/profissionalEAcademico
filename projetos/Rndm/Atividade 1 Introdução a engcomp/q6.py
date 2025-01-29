
def obterNumeroPositivo():
    while True:
        try:
            valor = int(input("Insira o número ue se quer calcular o fatorial."))
            if valor < 0:
                print("Por favor, insira um número inteiro positivo ou zero.")
            else:
                return valor
        except ValueError:
            print("Entrada inválida. Por favor, insira um número inteiro.")


n = obterNumeroPositivo()

i = n
r = 1

while i > 1:
	r = i * r 
	i -= 1
	#print(f"i = {i}, r = {r}")

print(f"{n}! é igual a {r}")

