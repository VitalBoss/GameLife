#1-Живая клетка  0-Мертвая клетка
#Пусть клетки, которые находятся за пределами области n*m считаются мертвыми
import random

class Game:
    n = 0
    m = 0
    Pole = []
    life = 0
    def __init__(self):
        print('Введите размеры поля игры "Жизнь" ')
        print('Кол-во строк:')
        self.n = int(input())
        print('Кол-во столбцов:')
        self.m = int(input())
        for i in range(self.n):
            self.Pole.append([0]*self.m)

    def __del__(self):
        for i in range(self.n):
            for j in range(self.m):
                self.Pole[i][j] = 0

    def Output(self):
        for i in range(self.n):
            print(*self.Pole[i], sep=" ")

    def Input(self):
        for i in range(self.n):
            for j in range(self.m):
                buf = random.randint(0, 1)
                if buf == 1:
                    self.Pole[i][j] = 1

    def check_neighbours(self, i, j):
        if (i-1) >= 0:
            if self.Pole[i-1][j] == 1:
                self.life += 1
        if (j-1) >= 0:
            if self.Pole[i][j-1] == 1:
                self.life += 1
        if (i+1) <= self.n-1:
            if self.Pole[i+1][j] == 1:
                self.life += 1
        if (j+1) <= self.m-1:
            if self.Pole[i][j+1] == 1:
                self.life += 1
        if ((i-1) >= 0) and ((j-1) >= 0):
            if self.Pole[i-1][j-1] == 1:
                self.life += 1
        if ((i+1) <= self.n-1) and ((j-1) >= 0):
            if self.Pole[i+1][j-1] == 1:
                self.life += 1
        if ((i+1) <= self.n-1) and ((j+1) <= self.m-1):
            if self.Pole[i+1][j+1] == 1:
                self.life += 1
        if ((i-1) >= 0) and ((j+1) <= self.m-1):
            if self.Pole[i-1][j+1] == 1:
                self.life += 1

    def change(self, i, j, buf):
        if buf[i][j] == 1:
            if (self.life == 2) or (self.life == 3):
                buf[i][j] = 1
            else:
                buf[i][j] = 0
        else:
            if self.life == 3:
                buf[i][j] = 1

    def copy(self, field, buf):
        for i in range(self.n):
            for j in range(self.m):
                field[i][j] = buf[i][j]

    def work(self):
        buf = []
        for i in range(self.n):
            buf.append([0]*self.m)
        self.copy(buf, self.Pole)
        for i in range(self.n):
            for j in range(self.m):
                self.check_neighbours(i, j)
                self.change(i, j, buf)
                self.life = 0
        self.copy(self.Pole, buf)




