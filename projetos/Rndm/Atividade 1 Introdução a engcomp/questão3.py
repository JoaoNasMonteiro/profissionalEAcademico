

# Definir classe de aluno
class Aluno:
    def __init__(self, nome, nota1, nota2, media_final, aprovado):
        self.nome = nome
        self.nota1 = nota1
        self.nota2 = nota2
        self.media_final = media_final
        self.aprovado = aprovado

# Função para obter um número inteiro positivo
def obter_inteiro_positivo(mensagem):
    while True:
        try:
            valor = int(input(mensagem))
            if valor > 0:
                return valor
            else:
                print("Por favor, digite um número maior que zero.")
        except ValueError:
            print("Entrada inválida. Digite um número inteiro válido.")

# Função para obter uma nota válida entre 0 e 10
def obter_nota_valida(mensagem):
    while True:
        try:
            nota = float(input(mensagem))
            if 0 <= nota <= 10:
                return nota
            else:
                print("A nota deve estar entre 0 e 10.")
        except ValueError:
            print("Entrada inválida. Digite um número válido.")

# Input de quantidade de alunos na turma
qtd = obter_inteiro_positivo("Bem vindo(a) à calculadora de aprovação. Para começar, digite a quantidade de alunos na turma:\n")

# Lista para armazenar os alunos
alunos = []

# Coletar dados de cada aluno
for i in range(qtd):
    print(f"\nAluno(a) {i + 1}:")
    nome = input("Digite o nome do(a) estudante: ")
    nota1 = obter_nota_valida("Digite a nota da primeira avaliação: ")
    nota2 = obter_nota_valida("Digite a nota da segunda avaliação: ")

    media_final = (nota1 + nota2) / 2
    aprovado = media_final >= 7

    # Adicionar o aluno à lista
    alunos.append(Aluno(nome, nota1, nota2, media_final, aprovado))

# Exibir resultados
print("\nResultados:")
for aluno in alunos:
    print(f"Nome: {aluno.nome}")
    print(f"Média final: {aluno.media_final:.2f}")
    if aluno.aprovado:
        print("Status: Aprovado")
    else:
        print("Status: Reprovado")
    