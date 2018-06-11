# -*- coding: utf-8 -*-
import pygame as pg

pg.init()

Black = (  0 ,   0,   0)
White = (255 , 255, 255)
Green = (  0 , 255,   0)
Red =   (255 ,   0,   0)
Moon =  (165 , 108,  21)

Colors = [White,Green,Red]

mainfont = pg.font.Font('files\ARCADECLASSIC.ttf', 30)

xmax=1080
ymax=720
reso=(xmax,ymax)
scr=pg.display.set_mode(reso)

xsens=50
ysens=250
fGrav=100

mu=10

    
bobi=pg.image.load('files\\bob.png')
bobi=pg.transform.scale(bobi,(385,600))
bob=bobi.get_rect()

saturni=pg.image.load('files\\saturn.png')
saturni=pg.transform.scale(saturni,(225,170))
saturn=saturni.get_rect()

csmi=pg.image.load('files\\csmcmlem.png')
csmi=pg.transform.scale(csmi,(30,30))
csm=csmi.get_rect()

lemi=pg.image.load('files\\lem.png')
lemi=pg.transform.scale(lemi,(85,64))
lem=lemi.get_rect()

sfci=pg.image.load('files\moon-surface.png')
sfci=pg.transform.scale(sfci,(xmax,ymax))
sfc=sfci.get_rect()

sfc2i=pg.image.load('files\moon-surface-2.png')
sfc2i=pg.transform.scale(sfc2i,(xmax,ymax))
sfc2=sfc2i.get_rect()

earthi=pg.image.load('files\earth.png')
earthi=pg.transform.scale(earthi,(70,70))
earth=earthi.get_rect()

mooni=pg.image.load('files\moon.png')
mooni=pg.transform.scale(mooni,(40,40))
moon=mooni.get_rect()

rock1i=pg.image.load('files\\rock_1.png')
rock1=rock1i.get_rect()

rock2i=pg.image.load('files\\rock_2.png')
rock2=rock2i.get_rect()

rock3i=pg.image.load('files\\rock_3.png')
rock3=rock3i.get_rect()

rock4i=pg.image.load('files\\rock_4.png')
rock4=rock4i.get_rect()

rocks=[[rock1i,rock1],[rock2i,rock2],[rock3i,rock3],[rock4i,rock4]]
