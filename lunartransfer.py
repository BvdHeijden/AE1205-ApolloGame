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
        key=pg.key.get_pressed()
        
        t=float(pg.time.get_ticks())/1000
        T=t-t00
        dt=t-t0
        t0=t
        
        data.scr.fill(data.Black)
        
        xmoon=data.ymax*cos(-0.01*T)/2+data.xmax/2
        ymoon=data.ymax*sin(-0.01*T)/2+data.ymax/2        
        data.moon.center=(xmoon,ymoon)
        
        xship=data.ymax*cos(-T)/15+data.xmax/2
        yship=data.ymax*sin(-T)/15+data.ymax/2        
        data.csm.center=(xship,yship)

        
        pg.draw.circle(data.scr, data.Green, (int(data.xmax/2),int(data.ymax/2)), int(data.ymax/2), 3)
        pg.draw.circle(data.scr, data.Red, (int(data.xmax/2),int(data.ymax/2)),int(data.ymax/15),3)        
        data.scr.blit(data.earthi,data.earth)
        data.scr.blit(data.mooni,data.moon)
        data.scr.blit(data.csmi,data.csm)
               
        pg.display.flip()
        
        if key[pg.K_SPACE]:
            running = False
            break
    
    paused = True        
    while paused:
        pg.event.pump()
        key=pg.key.get_pressed()
        
        if key[pg.K_SPACE]:
            paused = False
    
    burning = True
    while burning:
        pg.event.pump()
        key=pg.key.get_pressed()
