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
    target=rnd.randint(0,data.xmax-100)
    
    
    t0=float(pg.time.get_ticks())/1000

    while not landed:
        pg.event.pump()
        key=pg.key.get_pressed()
        pg.time.wait(5)
        
        t=float(pg.time.get_ticks())/1000
        dt=t-t0
        t0=t
        
        data.scr.fill(data.Black)
        data.scr.blit(data.sfci,data.sfc)        
        
        data.lem.center=posx,posy-(data.lem.height/2)
        data.scr.blit(data.lemi,data.lem)
        text=data.mainfont.render(str(round(fuel*100)),False,data.Red)
        data.scr.blit(text,(5,100))
        
        sh=pg.Surface((85,5))
        sh.set_alpha(200)
        sh.fill(data.Black)
        data.scr.blit(sh,(posx-43,data.ymax-40))
        tgt=pg.Surface((100,5))
        tgt.fill(data.Red)
        data.scr.blit(tgt,(target,data.ymax-40))
                
        pg.display.update()
        
        accx=0
        accy=data.fGrav
        
        if key[pg.K_LEFT] and fuel > 0:
            accx=-data.xsens
            fuel+=-0.003
        
        if key[pg.K_RIGHT] and fuel > 0:
            accx=data.xsens
            fuel+=-0.003
        
        if key[pg.K_UP] and fuel > 0:
            accy+=-data.ysens
            fuel+=-0.009
        
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
            
            if abs(posx-target-50)>50:
                score=0
                
            paused = True
            txtDisplay = False
            
            while paused:    
                pg.event.pump() 
                key=pg.key.get_pressed()
                
                if txtDisplay:
                    text=data.mainfont_small.render('Well Done! press ENTER to continue',False,data.Red)
                    data.scr.blit(text,(data.xmax/3,120))    
                    txtDisplay=False
                else:
                    pg.draw.rect(data.scr,data.Black,(data.xmax/3 + 120,120,250,40))
                    txtDisplay=True
                    
                pg.display.flip()
                
                pg.time.wait(300)
                
                if key[pg.K_RETURN]:
                    paused = False     
            
    return score