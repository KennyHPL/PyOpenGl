import pygame as pg
import numpy as np
import threading
import time

WIDTH = 150; HEIGHT = 150
dampening = .99
done = False

def calcBuffer(buffer2, buffer1, endRow, endCol, startRow, startCol):
    for i in range(startRow, endRow):
        for j in range(startCol, endCol):
            buffer2[i][j] = ((buffer1[i-1][j]+
                             buffer1[i+1][j]+
                             buffer1[i][j-1]+
                             buffer1[i][j+1])/2 - buffer2[i][j]) * dampening

def setScreen(screen, buffer2, endRow, endCol, startRow, startCol):
    for i in range(startRow, endRow):
        for j in range(startCol, endCol):
            color = (buffer2[i][j])
            if color > 255:
                color = 255
            elif color < 0:
                color = 0
            screen.set_at((i,j), (color,color,color))

buffer1 = np.zeros((WIDTH,HEIGHT), dtype='int')
buffer2 = np.zeros((WIDTH,HEIGHT), dtype='int')
pg.init()
clock = pg.time.Clock()
screen = pg.display.set_mode((WIDTH,HEIGHT))
pg.display.set_caption('Water')

while not done:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            done = True
        if event.type == pg.KEYDOWN:
            key = event.key
            if key == pg.K_ESCAPE:
                done = True

    pressed = False
    if(pg.mouse.get_pressed()[0] == True):
        pos = pg.mouse.get_pos()
        buffer1[pos[0]][pos[1]] = 255
        pressed = True

    t1 = threading.Thread(target =calcBuffer,
                          args=(buffer2, buffer1, WIDTH//2, HEIGHT//2, 1, 1))
    t2 = threading.Thread(target =calcBuffer,
                          args=(buffer2, buffer1, WIDTH-1, HEIGHT-1, WIDTH//2+1, HEIGHT//2))
    t3 = threading.Thread(target =calcBuffer,
                          args=(buffer2, buffer1, WIDTH-1, HEIGHT//2, WIDTH//2+1, 1))
    t4 = threading.Thread(target =calcBuffer,
                          args=(buffer2, buffer1, WIDTH//2, HEIGHT-1, 1, HEIGHT//2))
    t1.start();t2.start();t3.start();t4.start()
    t1.join();t2.join();t3.join();t4.join()

    t1 = threading.Thread(target =setScreen,
                          args=(screen, buffer2, WIDTH//2, HEIGHT//2, 1, 1))
    t2 = threading.Thread(target =setScreen,
                          args=(screen, buffer2, WIDTH, HEIGHT, WIDTH//2, HEIGHT//2))
    t3 = threading.Thread(target =setScreen,
                          args=(screen, buffer2, WIDTH, HEIGHT//2, WIDTH//2, 1))
    t4 = threading.Thread(target =setScreen,
                          args=(screen, buffer2, WIDTH//2, HEIGHT, 1, HEIGHT//2))
    t1.start();t2.start();t3.start();t4.start()
    t1.join();t2.join();t3.join();t4.join()

    temp = buffer2
    buffer2 = buffer1
    buffer1 = temp

    pg.display.flip()
    clock.tick(60)
