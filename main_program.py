# -*- coding: utf-8 -*-

import pygame as pg
import data
import transitions
import Startscreen
import lunartransfer
import landing

  
pg.init()

score=0

##Display Start screen
#Startscreen.display()
#
##Display introduction
#transitions.intro()
#
##Play lunar transfer game
#score += lunartransfer.play()

#Play Landing game
score += landing.play()

pg.quit()