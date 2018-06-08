# -*- coding: utf-8 -*-
import pygame as pg
import random as rnd
import data

pg.init()

def display():
    paused = True
    start = False
    txtDisplay = True
    
    while paused:
        pg.event.pump()
        key=pg.key.get_pressed()
        
        data.scr.fill(data.Black)
        
        text=data.mainfont.render('Barts  ultra-realistic   Apollo  Simulator',False,data.White)
        data.scr.blit(text,((data.xmax-text.get_width())/2,200))
        
        if txtDisplay:
            text=data.mainfont.render('Press  ENTER   to   start',False,data.Red)
            data.scr.blit(text,((data.xmax-text.get_width())/2,data.ymax/2))
            txtDisplay = False
        else:
            txtDisplay = True
        
        pg.display.flip()
        
        pg.time.wait(300)
        
        if key[pg.K_RETURN]:
            start=True
            paused = False
        
    return start
            