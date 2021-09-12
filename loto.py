"""
== Лото ==
Правила игры в лото.
Игра ведется с помощью спе циальных карточек, на которых отмечены числа,
и фишек (бочонков) с цифрами.
Количество бочонков — 90 штук (с цифрами от 1 до 90).
Каждая карточка содержит 3 строки по 9 клеток. В каждой строке по 5 случайных цифр,
расположенных по возрастанию. Все цифры в карточке уникальны. Пример карточки:

--------------------------
    9 43 62          74 90
 2    27    75 78    82
   41 56 63     76      86
--------------------------

В игре 2 игрока: пользователь и компьютер. Каждому в начале выдается
случайная карточка.

Каждый ход выбирается один случайный бочонок и выводится на экран.
Также выводятся карточка игрока и карточка компьютера.

Пользователю предлагается зачеркнуть цифру на карточке или продолжить.
Если игрок выбрал "зачеркнуть":
    Если цифра есть на карточке - она зачеркивается и игра продолжается.
    Если цифры на карточке нет - игрок проигрывает и игра завершается.
Если игрок выбрал "продолжить":
    Если цифра есть на карточке - игрок проигрывает и игра завершается.
    Если цифры на карточке нет - игра продолжается.

Побеждает тот, кто первый закроет все числа на своей карточке.
Пример одного хода:
Новый бочонок: 70 (осталось 76)
------ Ваша карточка -----
 6  7          49    57 58
   14 26     -    78    85
23 33    38    48    71
--------------------------
-- Карточка компьютера ---
 7 87     - 14    11
      16 49    55 88    77
   15 20     -       76  -
--------------------------
Зачеркнуть цифру? (y/n)

Подсказка: каждый следующий случайный бочонок из мешка удобно получать
с помощью функции-генератора.

Подсказка: для работы с псевдослучайными числами удобно использовать
модуль random: http://docs.python.org/3/library/random.html

"""
import random
import os

class Matrix:
    def __init__(self, list_of_lists):

        self.result = '┌───┬───┬───┬───┬───┬───┬───┬───┬───┐\n'
        self.list_of_lists = list_of_lists
        for i in range(3):
            self.result += '│'
            for j in range(9):
                if self.list_of_lists[i][j] == 0:
                    self.result += '   │'
                else:
                    if self.list_of_lists[i][j] < 10:
                        self.result += f'  {str(self.list_of_lists[i][j])}│'
                    else:
                        self.result += f' {str(self.list_of_lists[i][j])}│'
            if i != 2:
                self.result += '\n├───┼───┼───┼───┼───┼───┼───┼───┼───┤\n'
            else:
                self.result += '\n└───┴───┴───┴───┴───┴───┴───┴───┴───┘'

    def __str__(self):
        return self.result


class LottoCard:
    def __init__(self):
        self.n_l = []
        g = self.gen_num()
        self.numbers_matrix = [[next(g) for j in range(5)] for i in range(3)]
        for i in range(len(self.numbers_matrix)):
            self.numbers_matrix[i].sort()
        self.n_l = []
        self.number_or_null = 0
        self.index_table = []
        for i in range(3):
            self.index_table.append([])
            self.count_of_none = 4
            self.count_of_number = 5
            self.index = 0
            for j in range(9):
                self.number_or_none = random.randint(0, 1)
                if ((self.number_or_none == 0) and (self.count_of_none > 0)) or (self.count_of_number == 0):
                    self.count_of_none -= 1
                    self.index_table[i].append(0)
                elif ((self.number_or_none != 0) and (self.count_of_number > 0)) or (self.count_of_none == 0):
                    self.index_table[i].append(self.numbers_matrix[i][self.index])
                    self.index += 1
                    self.count_of_number -= 1
        self.numbers_matrix = self.index_table

    def get_matrix(self):
        self.get = Matrix(self.numbers_matrix)
        return self.get

    def gen_num(self):
        while True:
            n = random.randint(1, 90)
            if n not in self.n_l:
                self.n_l.append(n)
                yield n


class LottoGame:
    def __init__(self, one_player, two_player):
        self.one_player = one_player
        self.two_player = two_player
        self.list_of_numbers_game = []
        self.count = 90
        self.matrix1_1 = self.one_player.numbers_matrix
        self.matrix2_1 = self.two_player.numbers_matrix
        self.matrix1_2 = Matrix(self.matrix1_1)
        self.matrix2_2 = Matrix(self.matrix2_1)
        self.p1 = 15
        self.p2 = 15

    def print_game(self):
        print(' Ваша карточка')
        print(self.matrix1_2)
        print('\n Карточка компьютера')
        print(self.matrix2_2)

    def game_start(self):
        move = self.get_random_number
        if move != 0:
            print(f' Новый бочонок: {move} (осталось {self.count})')
            self.print_game()

            solution = input('Зачеркнуть? (y/n)')
            if solution == 'y':
                if move in self.matrix1_1[0]:
                    self.p1 -= 1
                    for i in range(len(self.matrix1_1[0])):
                        if move == self.matrix1_1[0][i]:
                            self.matrix1_1[0][i] = 0
                elif move in self.matrix1_1[1]:
                    self.p1 -= 1
                    for i in range(len(self.matrix1_1[1])):
                        if move == self.matrix1_1[1][i]:
                            self.matrix1_1[1][i] = 0
                elif move in self.matrix1_1[2]:
                    self.p1 -= 1
                    for i in range(len(self.matrix1_1[2])):
                        if move == self.matrix1_1[2][i]:
                            self.matrix1_1[2][i] = 0
                else:
                    print('Вы проиграли')
                    self.p2 = 0
                self.matrix1_2 = Matrix(self.matrix1_1)
            else:
                if move in self.matrix1_1[0]:
                    print('Вы проиграли')
                    self.p2 = 0
                elif move in self.matrix1_1[1]:
                    print('Вы проиграли')
                    self.p2 = 0
                elif move in self.matrix1_1[2]:
                    print('Вы проиграли')
                    self.p2 = 0
            if move in self.matrix2_1[0]:
                self.p2 -= 1
                for i in range(len(self.matrix2_1[0])):
                    if move == self.matrix2_1[0][i]:
                        self.matrix2_1[0][i] = 0
            elif move in self.matrix2_1[1]:
                self.p2 -= 1
                for i in range(len(self.matrix2_1[1])):
                    if move == self.matrix2_1[1][i]:
                        self.matrix2_1[1][i] = 0
            elif move in self.matrix2_1[2]:
                self.p2 -= 1
                for i in range(len(self.matrix2_1[2])):
                    if move == self.matrix2_1[2][i]:
                        self.matrix2_1[2][i] = 0
            self.matrix2_2 = Matrix(self.matrix2_1)
            os.system('cls||clear')
            if (self.p1 != 0) and (self.p2 != 0):
                self.game_start()
            else:
                if self.p1 < self.p2:
                    print('Вы выиграли')
                elif self.p1 == self.p2:
                    print('Игра окончена: Победила дружба :)')
                elif self.p1 > self.p2:
                    print('Вы проиграли')

    @property
    def get_random_number(self):
        while True:
            n = random.randint(1, 90)
            if (n not in self.list_of_numbers_game) and (self.count != 0):
                self.list_of_numbers_game.append(n)
                self.count -= 1
                return n
            if self.count == 0:
                return 0


user = LottoCard()
computer = LottoCard()
game = LottoGame(user, computer)
game.game_start()
