# -*- coding: utf-8 -*-
import pygame as pg
from numpy import sin,cos,sqrt,arccos,degrees
import data

pg.init()

def play():
    
    running = True
    
    data.earth.center=(data.xmax/2,data.ymax/2)
    
    t00=float(pg.time.get_ticks())/1000
    t0=t00
    
    a_moon = data.ymax/2
    a_parking = data.ymax/15
    phi=0.
    
    #parking orbit simulation
    while running:
        pg.event.pump()
        key=pg.key.get_pressed()
        
        t=float(pg.time.get_ticks())/1000
        T=t-t00
        dt=t-t0
        t0=t
        
        data.scr.fill(data.Black)
        
        xmoon=a_moon*cos(-0.15*T)+data.xmax/2
        ymoon=a_moon*sin(-0.15*T)+data.ymax/2        
        data.moon.center=(xmoon,ymoon)
        
        xship=a_parking*cos(-10*T)+data.xmax/2
        yship=a_parking*sin(-10*T)+data.ymax/2        
        data.csm.center=(xship,yship)

        
        pg.draw.circle(data.scr, data.Green, (int(data.xmax/2),int(data.ymax/2)), int(a_moon), 3)
        pg.draw.circle(data.scr, data.Red, (int(data.xmax/2),int(data.ymax/2)),int(a_parking),3)        
        data.scr.blit(data.earthi,data.earth)
        data.scr.blit(data.mooni,data.moon)
        data.scr.blit(data.csmi,data.csm)
        
        pg.display.flip()
        
        if key[pg.K_SPACE]:
            running = False
            if yship < (data.ymax/2):
                phi=degrees(arccos((xship-data.xmax/2)/a_parking))
            else:
                phi=- degrees(arccos((xship-data.xmax/2)/a_parking))
                
            if ymoon < (data.ymax/2):
                phi_moon=degrees(arccos((xmoon-data.xmax/2)/a_moon))
            else:
                phi_moon=- degrees(arccos((xmoon-data.xmax/2)/a_moon))
        
        if key[pg.K_ESCAPE]:
            return 0

      #Paused, waiting for transfer burn start
    paused = True        
    while paused:
        pg.event.pump()
        key=pg.key.get_pressed()
        
        if key[pg.K_SPACE]:
            paused = False
    
    #Burning
    burning = True
    rp=a_parking
    Tb=float(pg.time.get_ticks())/1000
    while burning:
        pg.event.pump()
        key=pg.key.get_pressed()
        T=(float(pg.time.get_ticks())/1000)-Tb
        
        ra=rp+30*T
        e=(ra-rp)/(ra+rp)
        a=(rp+ra)/2
        orb_rect = pg.Rect(0,0,rp+ra,2*sqrt(ra*rp))
        orb_rect.center = (data.xmax/2)-(e*a) , data.ymax/2
        
        data.scr.fill(data.Black)
        sur = create_ellipse(rp,ra,phi)
        data.scr.blit(sur,(data.xmax/2-sur.get_width()/2,data.ymax/2-sur.get_height()/2))
        pg.draw.circle(data.scr, data.Green, (int(data.xmax/2),int(data.ymax/2)), int(a_moon), 3)
        pg.draw.circle(data.scr, data.Red, (int(data.xmax/2),int(data.ymax/2)),int(a_parking),3)        
        data.scr.blit(data.earthi,data.earth)
        data.scr.blit(data.mooni,data.moon)
        data.scr.blit(data.csmi,data.csm)

        pg.display.update()
        
        if key[pg.K_SPACE]==False:
            burning = False       
    
    phi_moon += 540
    phi += 360
    
    phi_moon = phi_moon%360
    phi = phi%360
    
    dphi = phi-phi_moon
    score=-250*dphi+2500
    
    da=abs(a_moon-ra)
    score += -62.5*da + 2500
    
    pg.time.wait(1000)    
    text=data.mainfont_small.render('Well Done!',False,data.Red)
    data.scr.blit(text,(data.xmax/3,100)) 
    
    paused = True
    txtDisplay = False
    
    while paused:    
        pg.event.pump() 
        key=pg.key.get_pressed()
        
        if txtDisplay:
            text=data.mainfont_small.render('press ENTER to continue',False,data.Red)
            data.scr.blit(text,(data.xmax/3,120))    
            txtDisplay=False
        else:
            pg.draw.rect(data.scr,data.Black,(data.xmax/3,120,250,40))
            txtDisplay=True
            
        pg.display.flip()
        
        pg.time.wait(300)
        
        if key[pg.K_RETURN]:
            paused = False     
    
    return max(0,score)
        
def create_ellipse(rp,ra,phi):
    sur = pg.Surface((2*ra,2*sqrt(ra*rp)))
    pg.draw.ellipse(sur,data.Blue,(0,0,rp+ra,2*sqrt(ra*rp)),2)
    sur = pg.transform.rotate(sur,phi)
    
    return sur
