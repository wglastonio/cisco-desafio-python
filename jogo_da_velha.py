# Desafio Cisco em Python
# #MaratonLATAM2023_Python_INBRATI
# 25jun2023

def display_board(board):
# A função aceita um parâmetro contendo o status atual da placa
# e o imprime no console.
    print("\n+-------+-------+-------+")
    print("|       |       |       |")
    print(f"|   {board[0][0]}   |   {board[0][1]}   |   {board[0][2]}   |")
    print("|       |       |       |")
    print("+-------+-------+-------+")
    print("|       |       |       |")
    print(f"|   {board[1][0]}   |   {board[1][1]}   |   {board[1][2]}   |")
    print("|       |       |       |")
    print("+-------+-------+-------+")
    print("|       |       |       |")
    print(f"|   {board[2][0]}   |   {board[2][1]}   |   {board[2][2]}   |")
    print("|       |       |       |")
    print("+-------+-------+-------+\n")
    return

def enter_move(board):
# A função aceita o status atual do tabuleiro, pergunta ao usuário sobre sua jogada, 
# verifica a entrada e atualiza o quadro de acordo com a decisão do usuário.
    count = 1
    while True:
        while True:
            try:
                move = int(input("Digite seu movimento: "))
                if move not in range(1, 10):
                    print("Jogada inválida!!")
                    continue
                else:
                    break
            except:
                print("Jogada Inválida!!")
                continue

        for i in range(0, 3):
            for j in range(0, 3):
                if move == count:
                    if (board[i][j] != 'O') and (board[i][j] != 'X'):
                        board[i][j] = 'O'
                        return board
                    else:
                        print("Jogada Inválida!!")
                        break
                else:
                    count += 1
        count = 1
        continue

def make_list_of_free_fields(board):
# A função navega pelo tabuleiro e constrói uma lista de todas as casas livres; 
# a lista consiste em tuplas, enquanto cada tupla é um par de números de linha e coluna.
    free = []
    for i in range(0, 3):
        for j in range(0, 3):
            if (board[i][j] != 'O') and (board[i][j] != 'X'):
                free.append((i, j))
    return free

def victory_for(board, sign):
    # A função analisa o estado da placa a fim de verificar se 
    # o jogador usando 'O's ou 'X's ganhou o jogo
    turn = []
    winner = False
    for i in range(0, 3):
        for j in range(0, 3):
            if (board[i][j] == sign):
                turn.append((i, j))
    if len(turn) > 2:
        if (turn[0][0] == turn[1][0]) and (turn[0][0] == turn[2][0]):
            winner = True
        if (turn[0][1] == turn[1][1]) and (turn[0][1] == turn[2][1]):
            winner = True
        if (turn[0][0] == turn[0][1]) and (turn[1][0] == turn[1][1]) and (turn[2][0] == turn[2][1]):
            winner = True
    return winner

def draw_move(board):
# A função desenha o movimento do computador e atualiza o tabuleiro.
    from random import randrange
    free = make_list_of_free_fields(board)
    pc_move = free[randrange(len(free))]
    board[pc_move[0]][pc_move[1]] = 'X'
    return board

# Inicia o jogo
print("\n--- Iniciando o Jogo ---")

# Simula o computador iniciando na posição 5
board = [[1, 2, 3], [4, 'X', 6], [7, 8, 9]]

# Conta as rodadas e mostra o quadro
turn = 1
display_board(board)

# Entra na rotina do jogo
while  turn <= 5:

    # Verifica de alcançou o máximo de rodadas
    # Como a jogada do computador ocorre na sequeência são contadas a metade
    # Se alcançar o máximo de rodadas, informa jogo empatado
    if turn == 5:
        print("Jogo empatou!")
        break

    # Jogada do usuário e verifica se venceu
    board = enter_move(board)
    display_board(board)
    if (victory_for(board, 'O')):
        print("Você ganhou!")
        break

    # Jogada do computador e verifica se venceu
    board = draw_move(board)
    display_board(board)
    if (victory_for(board, 'X')):
        print("Você perdeu!")
        break

    # Atualiza o número de rodadas
    turn += 1

