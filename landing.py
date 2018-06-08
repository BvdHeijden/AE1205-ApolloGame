# -*- coding: utf-8 -*-
import pygame as pg
import data
import random as rnd

pg.init()

def play():
    landed = False
    score=0
   
    posx=rnd.randint(10,data.xmax-10)
    posy=0
    velx=0
    vely=20
    fuel=1.
    
    t0=float(pg.time.get_ticks())/1000

    while not landed:
        pg.event.pump()
        key=pg.key.get_pressed()
        pg.time.wait(5)
        
        t=float(pg.time.get_ticks())/1000
        dt=t-t0
        t0=t
        
        data.scr.fill(data.Black)
        pg.draw.rect(data.scr,data.Moon,(0,data.ymax-40,data.xmax,40))
        
        rocks=rnd.sample(data.rocks, rnd.randint(1,4))
        for rock in rocks:
            rock[1].center=rnd.randint(1,data.xmax),data.ymax-56
            data.scr.blit(rock[0],rock[1])
        
        data.lem.center=posx,posy-(data.lem.height/2)
        data.scr.blit(data.lemi,data.lem)
        text=data.mainfont.render(str(round(fuel*100)),False,data.Red)
        data.scr.blit(text,(5,100))
        
        
        pg.display.flip()
        
        accx=0
        accy=data.fGrav
        
        if key[pg.K_LEFT] and fuel > 0:
            accx=-data.xsens
            fuel+=-0.001
        
        if key[pg.K_RIGHT] and fuel > 0:
            accx=data.xsens
            fuel+=-0.001
        
        if key[pg.K_UP] and fuel > 0:
            accy+=-data.ysens
            fuel+=-0.003
        
        if key[pg.K_ESCAPE]:
            landed = True
            pg.quit()
            
            
        velx+=accx * dt
        vely+=accy * dt
        posx+=velx * dt
        posy=min(posy+(vely * dt),data.ymax-40)
        
        if posy == data.ymax-40:
            landed = True
            score=max((100-vely)*50,0)
            pg.time.wait(2000)
        
    
    return score