# -*- coding: utf-8 -*-
import pygame as pg

pg.init()

Black = (  0 ,   0,   0)
White = (255 , 255, 255)
Green = (  0 , 255,   0)
Red   = (255 ,   0,   0)
Blue  = (  0 ,   0, 255)
Moon  = (165 , 108,  21)

Colors = [White,Green,Red]

mainfont = pg.font.Font('files\\fonts\\ARCADECLASSIC.ttf', 30)
mainfont_small = pg.font.Font('files\\fonts\\SF Atarian System Extended.ttf',20)

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
saturni=pg.transform.scale(saturni,(30,int(30*6.1)))
saturn=saturni.get_rect()

saturn_firei=pg.image.load('files\\saturn_fire.png')
saturn_firei=pg.transform.scale(saturn_firei,(30,30*10))
saturn_fire=saturn_firei.get_rect()

landscapei=pg.image.load('files\\landscape.png')
landscapei=pg.transform.scale(landscapei,(xmax,int(xmax*6.667)))
landscape=landscapei.get_rect()

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

