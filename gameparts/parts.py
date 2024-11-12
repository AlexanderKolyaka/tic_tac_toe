class Board:
    """Класс, который описывает игровое поле."""

    filed_size = 3

    def __init__(self):
        
        self.board = [[' ' for _ in range(3)] for _ in range(3)]

    def make_move(self, row, column, player):
        self.board[row][column] = player

    def display(self):
        for row in self.board:
            print('|'.join(row))
            print('-' * 5)

    def is_board_full(self):
        """Метод, который проверяет, что доска заполнена"""
        # Цикл проходится по всем столбцам игрового поля.
        for i in range(self.filed_size):
            # А потом по всем строчкам.
            for j in range(self.filed_size):
                if self.board[i][j] == ' ':
                    return False
        return True
    
    def check_win(self, player):
        """Метод, который определяет победу"""
        # Тут реализована проверка по вертикали и горизонтали.
        for i in range(3):
            if (all([self.board[i][j] == player for j in range(3)]) or
                    all([self.board[j][i] == player for j in range(3)])):
                return True
        # Тут реализована проверка по диагонали.
        if (
            self.board[0][0] == self.board[1][1] == self.board[2][2] == player
            or
            self.board[0][2] == self.board[1][1] == self.board[2][0] == player
        ):
            return True

        return False

    def save_result(self, player=''):
        """Метод, который добавляет результат в тектстовый файл
        Сделан в 2х вариантах, 1 через контекстный менеджер(более правильный)
        2 вариант,закомментированный реализован просто обычными коммандами"""

        with open('results.txt', 'a') as file:
            if player != '':
                file.write('\n')
                file.write(f'Победитель {player}')

            else:
                file.write('\n')
                file.write('Ничья')


        '''
        file = open('results.txt', 'a', encoding='utf-8') 
        if player != '':
            file.write('\n')
            file.write(f'Победитель {player}')

        else:
            file.write('\n')
            file.write('Ничья')
        file.close()
        '''

    def __str__(self):
        return (
            'Объект игрового поля размером '
            f'{self.filed_size}x{self.filed_size}'
        )