

# print("Bem vindo ao cardápio interativo do restaurante. Você poderá escolher uma opção de prato principal, uma opção e sobremesa e uma opção de bebida.")

# class comida:
# 	"""docstring for ClassName"""
# 	def __init__(self, numero):
# 		self.numero = numero
# 		self.preco = self.findPreco()
# 		self.calorias = self.findCalorias()
# 		self.nome = self.findNome()

# 	def findPreco(numero):
# 		precos = {
# 		1 : 8.50, 2 : 12.30,
# 		3 : 7.50, 4 : 10.50,
# 		5 : 1.50, 6 : 3.50,
# 		7 : 3.00, 8: 2.50,
# 		9 : 1.00, 10 : 2.50,
# 		11 : 3.5, 12 : 2.00,
# 		}

# 		return(precos[numero])

# 	def findNome(numero):
# 		nomes = {
# 		1 : "Vegetariano", 2 : "Peixe",
# 		3 : "Frango", 4 : "Carne",
# 		5 : "Abacaxi", 6 : "Sorvete DIet",
# 		7 : "Mousse Diet", 8: "Mousse de Chocolate",
# 		9 : "Chá", 10 : "Suco de Laranja",
# 		11 : "Suco de Melão", 12 : "Refrigerante Diet",
# 		}

# 	def findCalorias(numero):
# 		calorias = {
# 		1 : 180, 2 : 230,
# 		3 : 250, 4 : 350,
# 		5 : 75, 6 : 110,
# 		7 : 170, 8: 200,
# 		9 : 20, 10 : 70,
# 		11 : 100, 12 : 65,
# 		}

# def obter_inteiro_positivo(mensagem):
#     while True:
#         try:
#             valor = int(input(mensagem))
#             if 4 >= valor > 0:
#                 return valor
#             else:
#                 print("Por favor, digite um número entre zero e quatro.")
#         except ValueError:
#             print("Entrada inválida. Digite um número inteiro válido.")
		



# while True:
# 	pratos = []
# 	#n = obter_inteiro_positivo("Por favor, escolha uma das opções de prato principal abaixo\n1 - Vegetariano 180 Kcal R$8,50\n2 - Peixe 230 Kcal R$12,30\n3 - Carne 350 Kcal R$10,50")
# 	n = 4
# 	prato = comida(n)


print("Bem-vindo ao cardápio interativo do restaurante. Você poderá escolher uma opção de prato principal, uma sobremesa e uma bebida.")

class Comida:
    """Classe para representar um item do cardápio."""
    def __init__(self, numero):
        self.numero = numero
        self.preco = self.findPreco()
        self.calorias = self.findCalorias()
        self.nome = self.findNome()

    def findPreco(self):
        precos = {
            1: 8.50, 2: 12.30,
            3: 7.50, 4: 10.50,
            5: 1.50, 6: 3.50,
            7: 3.00, 8: 2.50,
            9: 1.00, 10: 2.50,
            11: 3.50, 12: 2.00,
        }
        return precos.get(self.numero, 0)

    def findNome(self):
        nomes = {
            1: "Vegetariano", 2: "Peixe",
            3: "Frango", 4: "Carne",
            5: "Abacaxi", 6: "Sorvete Diet",
            7: "Mousse Diet", 8: "Mousse de Chocolate",
            9: "Chá", 10: "Suco de Laranja",
            11: "Suco de Melão", 12: "Refrigerante Diet",
        }
        return nomes.get(self.numero, "Desconhecido")

    def findCalorias(self):
        calorias = {
            1: 180, 2: 230,
            3: 250, 4: 350,
            5: 75, 6: 110,
            7: 170, 8: 200,
            9: 20, 10: 70,
            11: 100, 12: 65,
        }
        return calorias.get(self.numero, 0)

def obterInteiroPositivo(mensagem, limiteinf, limitesup):
    while True:
        try:
            valor = int(input(mensagem))
            if limiteinf <= valor <= limitesup:
                return valor
            else:
                print(f"Por favor, digite um número entre {limiteinf} e {limitesup}.")
        except ValueError:
            print("Entrada inválida. Digite um número inteiro válido.")

# Loop principal do programa
while True:
	pratos = []
	preco_total = 0
	calorias_total = 0
# Escolha de almoço
	print("\nEscolha uma opção de prato principal:")
	print("1 - Vegetariano (180 Kcal, R$8,50)")
	print("2 - Peixe (230 Kcal, R$12,30)")
	print("3 - Frango (250 Kcal, R$7,50)")
	print("4 - Carne (350 Kcal, R$10,50)")

	numero_prato = obterInteiroPositivo("Digite o número do prato principal desejado:", 1, 4)
	prato = Comida(numero_prato)
	pratos.append(prato)

	print(f"Você escolheu: {prato.nome}")

# Escolha de sobremesa
	print("\nEscolha uma opção de Sobremesa:")
	print("5 - Abacaxi (75 Kcal, R$1,50)")
	print("6 - Sorvete Diet (110 Kcal, R$3,50)")
	print("7 - Mousse Diet (170 Kcal, R$3,00)")
	print("8 - Mousse de Chocolate (200 Kcal, R$2,50)")

	numero_prato = obterInteiroPositivo("Digite o número da sobremesa desejada: ", 5, 8)
	prato = Comida(numero_prato)
	pratos.append(prato)

	print(f"Você escolheu: {prato.nome}")

# Escolha de bebida
	print("\nEscolha uma opção de Bebida:")
	print("9 - Chá (20 Kcal, R$1,00)")
	print("10 - Suco de Laranja (70 Kcal, R$2,50)")
	print("11 - Suco de Melão (100, R$3,00)")
	print("12 - Refrigerante Diet (65 Kcal, R$2,50)")

	numero_prato = obterInteiroPositivo("Digite o número da sobremesa desejada: ", 9, 12)
	prato = Comida(numero_prato)
	pratos.append(prato)

	print(f"Você escolheu: {prato.nome}")


	print("\nSeu pedido final é:")

	for item in pratos:
		print(f"{item.nome} - {item.calorias} Kcal, R${item.preco}")
		preco_total += item.preco
		calorias_total += item.calorias

	print(f"Totalizado R${round(preco_total, 2)} e {calorias_total} Kcal")


	confirmar = input("Deseja confirmar o pedido? (s/n): ").strip().lower()
	if confirmar == 's':
		print("Obrigado por utilizar o cardápio interativo! Seu pedido estará pronto em breve.")
		break
	else: 
		continuar = input("Deseja fazer outro pedido? (s/n)").strip().lower()
		if continuar != "s":
			("Obrigado por utilizar o cardápio interativo! Até breve mais!")
			break


