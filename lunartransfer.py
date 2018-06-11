# -*- coding: utf-8 -*-
import pygame as pg
from numpy import sin,cos
import data

pg.init()

def play():
    
    running = True
    
    data.earth.center=(data.xmax/2,data.ymax/2)
    
    t00=float(pg.time.get_ticks())/1000
    t0=t00
    
    while running:
        pg.event.pump()
        
        t=float(pg.time.get_ticks())/1000
        T=t-t00
        dt=t-t0
        t0=t
        
        data.scr.fill(data.Black)        
        xmoon=data.ymax*cos(-0.01*T)/2+data.xmax/2
        ymoon=data.ymax*sin(-0.01*T)/2+data.ymax/2        
        data.moon.center=(xmoon,ymoon)
        
        pg.draw.circle(data.scr, data.Green, (int(data.xmax/2),int(data.ymax/2)), int(data.ymax/2), 3)        
        data.scr.blit(data.earthi,data.earth)
        data.scr.blit(data.mooni,data.moon)
        
        
        pg.display.flip()
