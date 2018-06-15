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

    
def lunar():
    data.scr.fill(data.Black)    
    
    pg.time.wait(1000)    
    text=data.mainfont_small.render('Bob has now reached parking orbit.',False,data.White)
    data.scr.blit(text,(20,20))    
    pg.display.flip()     

    pg.time.wait(1000)    
    text=data.mainfont_small.render('You now have to help him reach the moon!',False,data.White)
    data.scr.blit(text,(20,50))    
    pg.display.flip()   
    
    pg.time.wait(1000)    
    text=data.mainfont_small.render('On the next screen, you will see a time-warped overview of the orbits.',False,data.White)
    data.scr.blit(text,(20,80))    
    pg.display.flip()  
    
    pg.time.wait(1000)    
    text=data.mainfont_small.render('Press and hold SPACEBAR to stop the time-warp and activate the lunar transfer burn.',False,data.White)
    data.scr.blit(text,(20,110))    
    pg.display.flip()     

    pg.time.wait(1000)    
    text=data.mainfont_small.render('Release the spacebar when you have reached a suitable orbit.',False,data.White)
    data.scr.blit(text,(20,140))    
    pg.display.flip()     

    pg.time.wait(1000)    
    text=data.mainfont_small.render('Try to get your encounter with the moon as close as possible!',False,data.White)
    data.scr.blit(text,(20,170))    
    pg.display.flip() 
    
    paused = True
    txtDisplay = False
    
    while paused:    
        pg.event.pump() 
        key=pg.key.get_pressed()
        
        if txtDisplay:
            text=data.mainfont.render('Press  ENTER  to  start',False,data.Red)
            data.scr.blit(text,(20,240))
            txtDisplay=False
        else:
            pg.draw.rect(data.scr,data.Black,(20,240,data.xmax,50))
            txtDisplay=True
            
        pg.display.flip()
        
        pg.time.wait(300)
        
        if key[pg.K_RETURN]:
            paused = False
    
    
def landing():
    data.scr.fill(data.Black)    
    
    pg.time.wait(1000)    
    text=data.mainfont_small.render('After some fine-tuning, Bob has finally reached the moon.',False,data.White)
    data.scr.blit(text,(20,20))    
    pg.display.flip()     

    pg.time.wait(1000)    
    text=data.mainfont_small.render('You now have to help him land on the surface',False,data.White)
    data.scr.blit(text,(20,50))    
    pg.display.flip()   
    
    pg.time.wait(1000)    
    text=data.mainfont_small.render('Be carefull, you only have a limited amount of fuel!',False,data.White)
    data.scr.blit(text,(20,80))    
    pg.display.flip()  
    
    pg.time.wait(1000)    
    text=data.mainfont_small.render('press the arrow keys to control the lander.',False,data.White)
    data.scr.blit(text,(20,140))    
    pg.display.flip()     

    pg.time.wait(1000)    
    text=data.mainfont_small.render('make a landing on the RED target.',False,data.White)
    data.scr.blit(text,(20,170))    
    pg.display.flip()     

    pg.time.wait(1000)    
    text=data.mainfont_small.render('Try to make your landing as soft as possible!',False,data.White)
    data.scr.blit(text,(20,200))    
    pg.display.flip()     

    paused = True
    txtDisplay = False
    
    while paused:    
        pg.event.pump() 
        key=pg.key.get_pressed()
        
        if txtDisplay:
            text=data.mainfont.render('Press  ENTER  to  start',False,data.Red)
            data.scr.blit(text,(20,270))
            txtDisplay=False
        else:
            pg.draw.rect(data.scr,data.Black,(20,270,data.xmax,50))
            txtDisplay=True
            
        pg.display.flip()
        
        pg.time.wait(300)
        
        if key[pg.K_RETURN]:
            paused = False

def ending(score):
    data.scr.fill(data.Black)    
    
    pg.time.wait(1000)    
    text=data.mainfont_small.render('You Did It!! nice job.',False,data.White)
    data.scr.blit(text,(20,20))    
    pg.display.flip()     

    pg.time.wait(1000)
    text='your final score was '+str(round(score))    
    text=data.mainfont_small.render(text,False,data.White)
    data.scr.blit(text,(20,50))    
    pg.display.flip()     
   
    pg.time.wait(1000)    
    text=data.mainfont_small.render('Press ENTER to play again or ESCAPE to quit',False,data.White)
    data.scr.blit(text,(20,100))    
    pg.display.flip()  
    
    paused = True
    while paused:
        pg.event.pump()
        key=pg.key.get_pressed()
        
        if key[pg.K_RETURN]:
            again = True
            paused = False
        
        if key[pg.K_ESCAPE]:
            again = False
            paused = False
    
    return again
