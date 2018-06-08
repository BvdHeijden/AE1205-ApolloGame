# -*- coding: utf-8 -*-

import pygame as pg
import random as rnd
import data
import transitions
import Startscreen
import landing

  
pg.init()

##DISPLAY START SCREEN
#Continue = Startscreen.display()
#
##Display introduction
#Continue = transitions.intro()

score = landing.play()

pg.quit()