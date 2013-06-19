import sys
import pygame
import random
import numpy

def count(matrix):
    height, width = matrix.shape
    extended = numpy.ones((height+2, width+2))*0
    extended[1:height+1, 1:width+1] = matrix
    result = numpy.zeros((height, width))

    for i in range(1, cells+1):
        for j in range(1, cells+1):
            result[i-1, j-1] += extended[i-1,j-1] + extended[i,j-1] +\
                                extended[i+1,j-1] + extended[i+1,j] +\
                                extended[i+1,j+1] + extended[i,j+1] +\
                                extended[i-1,j+1] + extended[i-1,j]

    return result

        
def show(world):
    color = {0: (0,0,0), 1: (0,0,255)}

    for i in range(cells):
        for j in range(cells):
            pygame.draw.circle(screen, color[world[i][j]],
                               (20+i+25*i, 20+j+25*j), 5)
            

def nextgen():
    next = count(numpy.array(world))
    result = [[0]*cells for i in range(cells)]

    for i in range(cells):
        for j in range(cells):
            if (world[i][j] == 1 and next[i,j] in range(2,4) or
                world[i][j] == 0 and next[i,j] == 3):

                result[i][j] = 1

    return result


if __name__ == '__main__':
    cells = 25
    tick = 200
    
    world = [[0]*cells for i in range(cells)]
    world = [[random.randrange(0,2) for j in i] for i in world]
    
    screen = pygame.display.set_mode((cells*27, cells*27))
    pygame.display.set_caption("Conway's game of life")
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        screen.fill((0, 0, 0))
        show(world)
        world = nextgen()
        pygame.display.flip()
        pygame.time.wait(tick)
