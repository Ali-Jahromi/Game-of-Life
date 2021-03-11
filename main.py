#!/usr/bin/env python3
import matplotlib.pyplot as plt
import os
import random
import time

#Fucntion to draw the world of cells
def draw(u, h, w):
    #Draw in terminal
    print("------------------------------") 
    for x in range(30):
        for y in range(30):
            if y != 29:
                print(u[x][y], end='')
            else:
                print(u[x][y])
    print("------------------------------")
    #Draw 2d plot of matrix
    plt.imshow(u)
    plt.draw()
    plt.ion()
    plt.pause(0.001)
    plt.clf()
#Function to evolve the world based on Conway's defined rules
def evolution(u, h, w):
    #Drawing a temporary world to evolve
    NewWorld = [[0 for x in range(w)] for y in range(h)]
    for x in range(30):
        for y in range(30):
            alivecells = 0
            #Checking all surrouding cells to cound alive ones
            for xd in range(x-1, x+2):
                for yd in range(y-1, y+2):
                    if u[(yd + h) % h][(xd + w) % w] == 1:
                        alivecells += 1
            #If the centering cell is alive reduce the number of alive cells by 1 
            if u[y][x] == 1:
                alivecells -= 1
            #Rules 2, and 4 from Wikipedia
            if alivecells == 3 or (alivecells == 2 and u[y][x] == 1):
                NewWorld[y][x] = 1
    draw(NewWorld, h, w)
    #Copying temporary world to the main world
    for x in range(30):
        for y in range(30):
            worldnum [x][y] = NewWorld[x][y]

if __name__ == "__main__":
    w = 30
    h = 30
    #Generating the main world by 30*30 dimension with random values
    world = [[int((random.random()*100)%10) for x in range(w)] for y in range(h)]
    worldnum = [[0 for x in range(w)] for y in range(h)]
    
    for x in range(30):
        for y in range(30):
            if world[x][y] > 1:
                worldnum[x][y] = 0
            else:
                worldnum[x][y] = 1
    draw(worldnum, h , w)
    
    
    while 1:
        evolution(worldnum, w, h)
        time.sleep(.2)
        os.system('clear')

