# -*- coding: utf-8 -*-
import data
import pygame as pg

pg.init()

def intro():
    data.scr.fill(data.Black)    
    data.bob.center=(data.xmax*0.2,data.bob.height/2)
    
    pg.time.wait(1000)    
    text=data.mainfont.render('This   is   Bob',False,data.White)
    data.scr.blit(text,(data.bob.right+20,100))    
    pg.display.flip()     

    pg.time.wait(500)
    data.scr.blit(data.bobi,data.bob)
    pg.display.flip() 
    
    pg.time.wait(1000)    
    text=data.mainfont.render('Bob  wants  to  fly  to  the  moon  today.',False,data.White)
    data.scr.blit(text,(data.bob.right+20,150))
    pg.display.flip()
    
    pg.time.wait(1000)    
    text=data.mainfont.render('Can  you  help  him??',False,data.White)
    data.scr.blit(text,(data.bob.right+20,200))
    pg.display.flip()

    paused = True
    txtDisplay = True
    
    while paused:
        pg.event.pump() 
        key=pg.key.get_pressed()
        
        if txtDisplay:
            text=data.mainfont.render('Press  ENTER  to  start',False,data.Red)
            data.scr.blit(text,(data.bob.right+20,270))
            txtDisplay=False
        else:
            pg.draw.rect(data.scr,data.Black,(data.bob.right+20,270,data.xmax,50))
            txtDisplay=True
            
        pg.display.flip()
        
        pg.time.wait(300)
        
        if key[pg.K_RETURN]:
            paused = False

    
    