# -*- coding: utf-8 -*-
import pygame as pg
import data

pg.init()

def play():
    
    data.scr.fill(data.Black)
    
    h=0
    data.landscape.bottomleft=(0,data.ymax)
    data.saturn.bottomleft=(data.xmax/2-10,data.ymax-20)
    
    #Explanation
    data.scr.blit(data.landscapei,data.landscape)
    data.scr.blit(data.saturni,data.saturn)
    pg.display.flip()
    
    pg.time.wait(1000)    
    text=data.mainfont_small.render('Bobs Saturn V rocket is standing on the launch pad at the beautiful island of Palau.',False,data.Red)
    data.scr.blit(text,(10,30))    
    pg.display.flip()

    pg.time.wait(500)    
    text=data.mainfont_small.render('Your job is to time the launch perfectly.',False,data.Red)
    data.scr.blit(text,(10,60))    
    pg.display.flip() 

    pg.time.wait(500)    
    text=data.mainfont_small.render('Press SPACEBAR at the exact moment the launch timer is at T-0 seconds.',False,data.Red)
    data.scr.blit(text,(10,90))    
    pg.display.flip()     

    #Waiting for timer start
    paused = True
    txtDisplay = True
    while paused:
        pg.event.pump() 
        key=pg.key.get_pressed()
        
        if txtDisplay:
            text=data.mainfont_small.render('Ready?  Press ENTER to start the launch timer',False,data.Red)
            data.scr.blit(text,(10,140))
            txtDisplay=False
        else:
            pg.draw.rect(data.scr,(121,189,217),(10,140,500,50))
            txtDisplay=True
            
        pg.display.flip()
        
        pg.time.wait(300)
        
        if key[pg.K_RETURN]:
            paused = False
 
    #Counting down
    counting = True
    Tstart = float(pg.time.get_ticks())/1000
    T=10.
    T0 = Tstart + T
    while counting:
        pg.event.pump()
        key = pg.key.get_pressed()
        
        t=float(pg.time.get_ticks())/1000
        T=T0-t
        
        data.scr.fill(data.Black)
        data.scr.blit(data.landscapei,data.landscape)
        data.scr.blit(data.saturni,data.saturn)
        text='T-'+str(round(T,4))
        text=data.mainfont_small.render(text,False,data.Red)
        data.scr.blit(text,(data.xmax*2/3,data.ymax*1/3))
        pg.display.flip()
        
        if key[pg.K_SPACE]:
            counting = False
            
    return 5000
        
        
        
        