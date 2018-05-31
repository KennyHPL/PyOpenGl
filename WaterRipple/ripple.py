import pygame as pg
import numpy as np
import threading
from helpers import *
import time


WIDTH = 200; HEIGHT = 200
dampening = .99
done = False
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

    if(pg.mouse.get_pressed()[0] == True):
        pos = pg.mouse.get_pos()
        buffer1[pos[0]][pos[1]] = 255

    before = time.time()

    t1 = threading.Thread(target =calcBuffer,
                          args=(screen, buffer2, buffer1, dampening,
                                0, WIDTH//2+1, 0, HEIGHT//2+1))
    t2 = threading.Thread(target =calcBuffer,
                          args=(screen, buffer2, buffer1, dampening,
                                WIDTH//2, WIDTH, HEIGHT//2, HEIGHT))
    t3 = threading.Thread(target =calcBuffer,
                          args=(screen, buffer2, buffer1, dampening,
                                WIDTH//2, WIDTH, 0, HEIGHT//2+1))
    t4 = threading.Thread(target =calcBuffer,
                          args=(screen, buffer2, buffer1, dampening,
                                0, WIDTH//2+1, HEIGHT//2, HEIGHT))
    t1.start();t2.start();t3.start();t4.start()
    t1.join();t2.join();t3.join();t4.join()

    after = time.time()
    print(after-before)

    temp = buffer2
    buffer2 = buffer1
    buffer1 = temp

    pg.display.flip()
    clock.tick(60)
