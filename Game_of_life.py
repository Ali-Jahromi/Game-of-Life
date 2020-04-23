import random
import time
import os

def draw(u, h, w):
    for x in range(30):
        for y in range(30):
            if y != 29:
                print(u[x][y], end='')
            else:
                print(u[x][y])

def evolution(u, h, w):
    NewWorld = [[" " for x in range(w)] for y in range(h)]
    for x in range(30):
        for y in range(30):
            alivecells = 0
            for xd in range(x-1, x+2):
                for yd in range(y-1, y+2):
                    if u[(yd + h) % h][(xd + w) % w] == "+":
                        alivecells += 1
            if u[y][x] == "+":
                alivecells -= 1
            if alivecells == 3 or (alivecells == 2 and u[y][x] == "+"):
                NewWorld[y][x] = "+"
    draw(NewWorld, h, w)
    for x in range(30):
        for y in range(30):
            world [x][y] = NewWorld[x][y]


w = 30
h = 30

world = [[int((random.random()*100)%10) for x in range(w)] for y in range(h)]
for x in range(30):
    for y in range(30):
        if world[x][y] > 1:
            world[x][y] = ' '
        else:
            world[x][y] = '+'
#draw(world, w, h)
while 1:
    print("-------------------------------------------")
    evolution(world, w, h)
    time.sleep(.2)
    os.system('clear')

