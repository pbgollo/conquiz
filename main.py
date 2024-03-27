import csv
import random

def printa_divisao():
    print("---------------------------------------")

def printa_bem_vindo():
    printa_divisao()
    print("*                                     *")
    print("*           Seja Bem-Vindo!           *")
    print("*                                     *")

def menu_principal():
    opcao = pega_opcao_principal()

    while opcao != 0:
        if opcao in range(1, 10):
            responder_questoes(opcao)
        else:
            print("> Opção inválida!")

        opcao = pega_opcao_principal()

    print("> Programa finalizado com sucesso!")
    printa_divisao()

def pega_opcao_principal():
    printa_divisao()
    print("| [1] Português        [2] Matemática |")
    print("| [3] Informática      [4] Inglês     |")
    print("| [5] Sistemas         [6] Legislação |")
    print("| [7] Atualidades      [8] Lógica     |")
    print("| [9] Simulado         [0] Sair       |")
    printa_divisao()
    opcao = int(input("> Escolha uma opção: "))
    return opcao

def processar_quebra_de_linha(pergunta):
    return pergunta.replace('\\n', '\n')

def responder_questoes(opcao):
    arquivo = f"questoes_{opcao}.csv"

    with open(arquivo, newline='', encoding='utf-8') as file:
        reader = csv.reader(file, delimiter=';')
        next(reader) 
        questoes = list(reader)
        selecionadas = random.sample(questoes, 10)

        pontuacao = 0

        for indice, questao in enumerate(selecionadas, start=1):
            pergunta_formatada = processar_quebra_de_linha(questao[0])
            print(f"\n{indice}. {pergunta_formatada}")
            alternativas = questao[1:-1]
            for i, alternativa in enumerate(alternativas, start=1):
                print(f" {chr(64 + i)}. {alternativa}")
            resposta_usuario = input("> Escolha uma alternativa: ").upper()
            gabarito = questao[-1]

            if resposta_usuario == gabarito:
                pontuacao += 1

        print(f"\n> Gabarito:")
        for indice, questao in enumerate(selecionadas, start=1):
            print(f" {indice}. {questao[-1]}")

        print(f"\nPontuação final: {pontuacao}/10")

def main():
    printa_bem_vindo()
    menu_principal()

if __name__ == "__main__":
    main()