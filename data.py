# -*- coding: utf-8 -*-
import pygame as pg

pg.init()

Black = (  0 ,   0,   0)
White = (255 , 255, 255)
Green = (  0 , 255,   0)
Red =   (255 ,   0,   0)
Moon =  (165 , 108,  21)

Colors = [White,Green,Red]

mainfont = pg.font.Font('files\ARCADECLASSIC.ttf', 60)

xmax=900
ymax=720
reso=(xmax,ymax)
scr=pg.display.set_mode(reso)

xsens=50
ysens=250
fGrav=100
    
bobi=pg.image.load('files\\bob.png')
bobi=pg.transform.scale(bobi,(385,600))
bob=bobi.get_rect()

saturni=pg.image.load('files\\saturn.png')
saturni=pg.transform.scale(saturni,(225,170))
saturn=saturni.get_rect()

csmi=pg.image.load('files\\csmcmlem.png')
csm=csmi.get_rect()

lemi=pg.image.load('files\\lem.png')
lemi=pg.transform.scale(lemi,(169,128))
lem=lemi.get_rect()

