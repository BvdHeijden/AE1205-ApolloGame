# -*- coding: utf-8 -*-
import data
import pygame as pg

pg.init()

def intro():
    data.scr.fill(data.Black)
    
    bob.center=(data.xmax/3,data.ymax-450)
    data.scr.blit(bobi,bob)
    
    pg.display.flip()
    
    pg.time.wait(5000)
    
    