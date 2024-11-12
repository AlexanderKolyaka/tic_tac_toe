from gameparts.parts import Board
from gameparts.exceptions import FieldIndexError, CellOccupiedError


def main():
    game = Board()
    current_player = 'X'
    # Это флаговая переменная. По умолчанию игра запущена и продолжается.
    running = True
    game.display()

    # Тут запускается основной цикл игры.
    while running:

        print(f'Ход делают {current_player}')

        while True:

            try:

                row = int(input('Введите номер строки: '))

                if row < 0 or row >= game.filed_size:

                    raise FieldIndexError
                
                colum = int(input('Введите номер столбца: '))

                if colum < 0 or colum >= game.filed_size:
                    raise FieldIndexError
                
                if game.board[row][colum] != ' ':
                    raise  CellOccupiedError
                
            except FieldIndexError:
                print(
                    'Значение должно быть неотрицательным и меньше '
                    f'{game.filed_size}.'
                )
                print('Пожалуйста, введите значения для строки и столбца заново.')
                # ...и цикл начинает свою работу сначала,
                # предоставляя пользователю ещё одну попытку ввести данные.
                continue
            # Если в блоке try исключения не возникло...

            except ValueError:

                print('Буквы вводить нельзя. Только числа.')
                print('Пожалуйста, введите значения для строки и столбца заново.')
                continue

            except Exception as e:

                print(f'Возникла ошибка:{e}')
                
            else:
                # ...значит, введённые значения прошли все проверки
                # и могут быть использованы в дальнейшем.
                # Цикл прерывается.
                break

        game.make_move(row, colum, current_player)
        print('Ход сделан!')
        # Перерисовать поле с учётом сделанного хода.
        game.display()
        # После каждого хода надо делать проверку на победу и на ничью.
        if game.check_win(current_player):
            print(f'Победили {current_player}.')
            running = False
            game.save_result(current_player)
        elif game.is_board_full():
            print('Ничья!')
            game.save_result()
            running = False
        
        # Тернарный оператор, через который реализована смена игроков.
        # Если current_player равен X, то новым значением будет O,
        # иначе — новым значением будет X.
        current_player = 'O' if current_player == 'X' else 'X'


if __name__ == '__main__':
    main()

