from mod import *

Pt = Game()
Pt.Input()
print("Исходное поле:")
Pt.Output()
print("-------------------------")
p = 1
k = 1
while k == 1:
    Pt.work()
    print("После", p, "итерации:")
    Pt.Output()
    print("Для повторной итерации введите 1:")
    k = int(input())
    p += 1