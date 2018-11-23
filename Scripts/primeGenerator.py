from sys import stdin
from math import sqrt


def prime(a, b):
    for i in range(a, b+1):
        p = True
        if i == 1:
            p = False
        elif i == 2 or i == 3:
            p = True
        elif i % 2 == 0 or i % 3 == 0:
            p = False
        else:
            for j in range(5, int(sqrt(i)+1), 6):
                if i % j == 0 or i % (j+2) == 0:
                    p = False
                    break
        if p:
            print(i)


for _ in range(int(stdin.readline())):
    a, b = map(int, stdin.readline().split())
    prime(a, b)
