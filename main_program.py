# -*- coding: utf-8 -*-

import pygame as pg
import data
import transitions
import Startscreen
import landing

  
pg.init()

#DISPLAY START SCREEN
Startscreen.display()

#Display introduction
transitions.intro()

#Play Landing game
score = landing.play()

pg.quit()