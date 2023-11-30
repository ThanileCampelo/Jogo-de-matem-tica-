import random
import time

# Perguntas e respostas gerais de matemática
perguntas_respostas = {
    "Qual é a soma de 2 + 2?": "4",
    "Qual é o resultado de 3 * 5?": "15",
    "Quanto é 10 / 2?": "5",
    "Qual é a raiz quadrada de 16?": "4",
    "Quanto é 7 - 3?": "4"
}

# Função para mostrar uma pergunta aleatória
def mostrar_pergunta(perguntas_respostas):
    pergunta, resposta = random.choice(list(perguntas_respostas.items()))
    print(pergunta)
    return resposta

# Função para processar a resposta do jogador
def processar_resposta(resposta_jogador, resposta_correta):
    if resposta_jogador == resposta_correta:
        print(random.choice(feedback_correto))
        return True
    else:
        print(random.choice(feedback_incorreto), "A resposta correta é:", resposta_correta)
        return False

# Função para praticar tabuada
def praticar_tabuada():
    numero = int(input("Escolha um número para praticar a tabuada (1 a 10): "))
    if numero < 1 or numero > 10:
        print("Número inválido. Escolha um número de 1 a 10.")
        return

    num_perguntas = 10  # Número de perguntas da tabuada
    print(f"Vamos praticar a tabuada do {numero}!\n")

    for _ in range(num_perguntas):
        multiplicador = random.randint(1, 10)
        pergunta = f"Quanto é {numero} x {multiplicador}? "
        resposta_correta = str(numero * multiplicador)

        resposta_jogador = input(pergunta)

        if processar_resposta(resposta_jogador, resposta_correta):
            print()  # Pular uma linha

# Função principal do jogo
def jogo():
    while True:
        print("Bem-vindo ao jogo de matemática!")
        print("Escolha uma opção:")
        print("1. Perguntas gerais de matemática")
        print("2. Praticar tabuada")
        print("3. Sair")

        opcao = input("Opção: ")

        if opcao == "1":
            pontuacao = 0
            num_perguntas = 5  # Número de perguntas gerais de matemática
            tempo_limite = 10  # Tempo limite para responder cada pergunta em segundos

            print(f"\nVocê responderá a {num_perguntas} perguntas. Você tem {tempo_limite} segundos para cada pergunta. Vamos lá!\n")

            for _ in range(num_perguntas):
                resposta_correta = mostrar_pergunta(perguntas_respostas)
                resposta_jogador = input("Sua resposta: ")

                tempo_inicial = time.time()

                if time.time() - tempo_inicial > tempo_limite:
                    print("Tempo esgotado! A resposta correta é:", resposta_correta, "\n")
                    continue

                if processar_resposta(resposta_jogador, resposta_correta):
                    pontuacao += 1

                time.sleep(1)  # Espera 1 segundo antes de mostrar a próxima pergunta

            print("Fim do jogo!")
            print(f"Sua pontuação final é: {pontuacao} de {num_perguntas}\n")

        elif opcao == "2":
            praticar_tabuada()

        elif opcao == "3":
            print("Obrigado por jogar! Até a próxima.")
            break

        else:
            print("Opção inválida. Escolha uma opção válida.")

if __name__ == "__main__":
    feedback_correto = ["Excelente!", "Você acertou!", "Muito bem!"]
    feedback_incorreto = ["Ops, essa não foi a resposta correta.", "Tente novamente.", "Não é dessa vez."]
    jogo()
