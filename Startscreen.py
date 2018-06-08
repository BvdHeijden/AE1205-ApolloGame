# -*- coding: utf-8 -*-
import pygame as pg
import random as rnd
import data

pg.init()

def display():
    paused = True
    start = False
    fr = 500
    txtDisplay = True
    
    while paused:
        pg.event.pump()
        key=pg.key.get_pressed()
        
        pg.time.wait(fr)
        
        if key[pg.K_RETURN]:
            start = True
            paused=False
        if key[pg.K_ESCAPE]:
            start = False
            paused = False
        
        data.scr.fill((0,0,0))
        
        if txtDisplay:
            text=data.mainfont.render('PRESS   ENTER   TO   START',False,(rnd.randint(10,255),rnd.randint(10,255),rnd.randint(10,255)))
            data.scr.blit(text,((data.xmax-text.get_width())/2,data.ymax/2))
            fr=600
            txtDisplay = False
        else:
            fr=300
            txtDisplay = True
                
        pg.display.flip()
    
    return start