import pygame
import random

def count(i, j):
    count_s = 0
    if i == 0:
        if j == 0:
            if world[i][j+1] == 1: count_s += 1
            if world[i+1][j] == 1: count_s += 1
            if world[i+1][j+1] == 1: count_s += 1
            return count_s
        elif j == cells-1:
            if world[i][j-1] == 1: count_s += 1
            if world[i+1][j] == 1: count_s += 1
            if world[i+1][j-1] == 1: count_s += 1
            return count_s
        else:
            if world[i][j-1] == 1: count_s += 1
            if world[i][j+1] == 1: count_s += 1
            if world[i+1][j] == 1: count_s += 1
            if world[i+1][j-1] == 1: count_s += 1
            if world[i+1][j+1] == 1: count_s += 1
            return count_s
    elif i == cells-1:
        if j == 0:
            if world[i-1][j] == 1: count_s += 1
            if world[i][j+1] == 1: count_s += 1
            if world[i-1][j+1] == 1: count_s += 1
            return count_s
        elif j == cells-1:
            if world[i][j-1] == 1: count_s += 1
            if world[i-1][j] == 1: count_s += 1
            if world[i-1][j-1] == 1: count_s += 1
            return count_s
        else:
            if world[i][j-1] == 1: count_s += 1
            if world[i][j+1] == 1: count_s += 1
            if world[i-1][j] == 1: count_s += 1
            if world[i-1][j-1] == 1: count_s += 1
            if world[i-1][j+1] == 1: count_s += 1
            return count_s
    else:
        if j == 0:
            if world[i-1][j] == 1: count_s += 1
            if world[i+1][j] == 1: count_s += 1
            if world[i][j+1] == 1: count_s += 1
            if world[i-1][j+1] == 1: count_s += 1
            if world[i+1][j+1] == 1: count_s += 1
            return count_s
        elif j == cells-1:
            if world[i-1][j] == 1: count_s += 1
            if world[i+1][j] == 1: count_s += 1
            if world[i][j-1] == 1: count_s += 1
            if world[i-1][j-1] == 1: count_s += 1
            if world[i+1][j-1] == 1: count_s += 1
            return count_s
        else:
            if world[i][j-1] == 1: count_s += 1
            if world[i][j+1] == 1: count_s += 1
            if world[i-1][j] == 1: count_s += 1
            if world[i+1][j] == 1: count_s += 1
            if world[i-1][j-1] == 1: count_s += 1
            if world[i+1][j-1] == 1: count_s += 1
            if world[i-1][j+1] == 1: count_s += 1
            if world[i+1][j+1] == 1: count_s += 1
            return count_s
        
def show(world):
    for i in range(cells):
        for j in range(cells):
            if world[i][j] == 0:
                pygame.draw.circle(screen, (0,0,0), (20+i+25*i, 20+j+25*j), 5)
            else:
                pygame.draw.circle(screen, (0,0,255), (20+i+25*i,20+j+25*j), 5)
            
def nextgen():
    tmp = [[0]*cells for i in range(cells)]
    for i in range(cells):
        for j in range(cells):
            count_out = count(i, j)
            if world[i][j] == 1:
                if count_out in range(2,4):
                    tmp[i][j] = 1
            if world[i][j] == 0 and count_out == 3:
                tmp[i][j] = 1
    return tmp

if __name__ == '__main__':
    cells = 25
    tick = 200
    
    world = [[0]*cells for i in range(cells)]
    world = [[random.randrange(0,2) for j in i] for i in world]
    
    screen = pygame.display.set_mode((cells*27, cells*27))
    pygame.display.set_caption("Conway's game of life")
    running = 1
    
    while running:
        event = pygame.event.poll()
        if event.type == pygame.QUIT:
            running = 0
        screen.fill((0, 0, 0))
        show(world)
        world = nextgen()
        pygame.display.flip()
        pygame.time.wait(tick)