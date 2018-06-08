# -*- coding: utf-8 -*-
import pygame as pg

pg.init()

Black = (  0 ,   0,   0)
White = (255 , 255, 255)
Green = (  0 , 255,   0)
Red =   (255 ,   0,   0)

Colors = [White,Green,Red]

mainfont = pg.font.Font('files\ARCADECLASSIC.ttf', 60)

xmax=1920
ymax=980
reso=(xmax,ymax)
scr=pg.display.set_mode(reso)

bobi=pg.image.load('files\\bob.jpg')
bob=bobi.get_rect()

saturni=pg.image.load('files\\saturn.png')
saturn=saturni.get_rect()

csmi=pg.image.load('files\\csmcmlem.png')
csm=csmi.get_rect()


