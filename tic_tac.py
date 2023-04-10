def draw_board(board):
    print("     |     |")
    print("  {}  |  {}  |  {}".format(board[0], board[1], board[2]))
    print("_____|_____|_____")

    print("     |     |")
    print("  {}  |  {}  |  {}".format(board[3], board[4], board[5]))
    print("_____|_____|_____")

    print("     |     |")
    print("  {}  |  {}  |  {}".format(board[6], board[7], board[8]))
    print("     |     |")


def input_valid(msg, board, player):
    while True:
        try:
            inp = int(input(msg))
            if board[inp - 1] == " ":
                board[inp - 1] = player
                break
            else:
                print('Эта ячейка уже занята, выберите другую.')
        except ValueError:
            print('Пожалуйста, введите верное число.')
        except IndexError:
            print('Введите число от 1 до 9.')


def check_winner(board, mark):
    if (board[0] == mark and board[1] == mark and board[2] == mark) or \
            (board[3] == mark and board[4] == mark and board[5] == mark) or \
            (board[6] == mark and board[7] == mark and board[8] == mark) or \
            (board[0] == mark and board[3] == mark and board[6] == mark) or \
            (board[1] == mark and board[4] == mark and board[7] == mark) or \
            (board[2] == mark and board[5] == mark and board[8] == mark) or \
            (board[0] == mark and board[4] == mark and board[8] == mark) or \
            (board[2] == mark and board[4] == mark and board[6] == mark):
        return True
    else:
        return False


def tic_tac_toe():
    print('Добро пожаловать в крестики-нолики.')
    print('Игрок 1 играет за "X", игрок 2 играет за "O"')
    board = [' '] * 9

    while True:
        draw_board(board)
        input_valid('Игрок 1, выбери число от 1 до 9: ', board, 'X')

        if check_winner(board, 'X'):
            draw_board(board)
            print('Поздравляю!Игрок 1 победил')
            break

        draw_board(board)
        print('Ничья' if ' ' not in board else '')
        input_valid('Игрок 2, выбери число от 1 до 9: ', board, 'O')

        if check_winner(board, 'O'):
            draw_board(board)
            print('Поздравляю!Игрок 2 победил')
            break

        if ' ' not in board:
            draw_board(board)
            print('Ничья')
            break


if __name__ == "__main__":
    tic_tac_toe()
