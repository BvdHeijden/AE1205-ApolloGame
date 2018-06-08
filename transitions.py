# -*- coding: utf-8 -*-
import data
import pygame as pg

pg.init()

def intro():
    data.scr.fill(data.Black)
    
    data.bob.center=(data.xmax/3,data.ymax-450)
    data.scr.blit(data.bobi,data.bob)
    
    pg.display.flip()
    
    pg.time.wait(5000)
    
    