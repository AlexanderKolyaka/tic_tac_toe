from gameparts.parts import Board
from gameparts.exceptions import FieldIndexError


def main():
    game = Board()
    game.display()

    while True:
        try:

            row = int(input('Введите номер строки: '))

            if row < 0 or row >= game.filed_size:

                raise FieldIndexError
            
            colum = int(input('Введите номер столбца: '))

            if colum < 0 or colum >= game.filed_size:
                raise FieldIndexError
            
        except FieldIndexError:
            print(
                'Значение должно быть неотрицательным и меньше '
                f'{game.field_size}.'
            )
            print('Пожалуйста, введите значения для строки и столбца заново.')
            # ...и цикл начинает свою работу сначала,
            # предоставляя пользователю ещё одну попытку ввести данные.
            continue
        # Если в блоке try исключения не возникло...
        except ValueError:
            print('Буквы вводить нельзя. Только числа.')
            print('Пожалуйста, введите значения для строки и столбца заново.')
        else:
            # ...значит, введённые значения прошли все проверки
            # и могут быть использованы в дальнейшем.
            # Цикл прерывается.
            break
    game.make_move(row, colum, 'X')
    print('Ход сделан!')
    # Перерисовать поле с учётом сделанного хода.
    game.display()


if __name__ == '__main__':
    main()

