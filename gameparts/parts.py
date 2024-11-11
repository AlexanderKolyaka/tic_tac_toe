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
    
    def __str__(self):
        return (
            'Объект игрового поля размером '
            f'{self.filed_size}x{self.filed_size}'
        )