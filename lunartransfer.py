# -*- coding: utf-8 -*-
import pygame as pg
from numpy import sin,cos,sqrt,arctan,degrees
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
        
        xmoon=a_moon*cos(-0.015*T)+data.xmax/2
        ymoon=a_moon*sin(-0.015*T)+data.ymax/2        
        data.moon.center=(xmoon,ymoon)
        
        xship=a_parking*cos(-T)+data.xmax/2
        yship=a_parking*sin(-T)+data.ymax/2        
        data.csm.center=(xship,yship)

        
        pg.draw.circle(data.scr, data.Green, (int(data.xmax/2),int(data.ymax/2)), int(a_moon), 3)
        pg.draw.circle(data.scr, data.Red, (int(data.xmax/2),int(data.ymax/2)),int(a_parking),3)        
        data.scr.blit(data.earthi,data.earth)
        data.scr.blit(data.mooni,data.moon)
        data.scr.blit(data.csmi,data.csm)
        
        pg.display.flip()
        
        if key[pg.K_SPACE]:
            running = False
            phi=degrees(arctan((-yship+data.ymax/2)/(xship-data.xmax/2)))
            print('phi = ',phi)
        
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
        
        ra=rp+10*T
        e=(ra-rp)/(ra+rp)
        a=(rp+ra)/2
        orb_rect = pg.Rect(0,0,rp+ra,2*sqrt(ra*rp))
        orb_rect.center = (data.xmax/2)-(e*a) , data.ymax/2
        sur = pg.Surface((data.xmax,data.ymax))
        sur.fill(data.Red)
        pg.draw.ellipse(sur,data.Blue,orb_rect,3)
        sur = pg.transform.rotate(sur,phi)

        
        data.scr.fill(data.Black)
        data.scr.blit(sur,(0,0))
        pg.draw.circle(data.scr, data.Green, (int(data.xmax/2),int(data.ymax/2)), int(a_moon), 3)
        pg.draw.circle(data.scr, data.Red, (int(data.xmax/2),int(data.ymax/2)),int(a_parking),3)        
        data.scr.blit(data.earthi,data.earth)
        data.scr.blit(data.mooni,data.moon)
        data.scr.blit(data.csmi,data.csm)

        pg.display.update()
        
        if key[pg.K_SPACE]==False:
            burning = False       
    
    return 5000
        
def create_ellipse(rp,ra,phi):
    sur = pg.Surface((rp+ra,2*sqrt(ra*rp)))
    pg.draw.ellipse(sur,data.Blue,(data.xmax/2,data.ymax/2,rp+ra,2*sqrt(ra*rp)),3)
    sur = pg.transform.rotate(sur,phi)
    
    return sur
