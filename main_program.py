# -*- coding: utf-8 -*-

import pygame as pg
import transitions
import Startscreen
import launch
import lunartransfer
import landing

  
pg.init()

again = True

#Display Start screen
Startscreen.display()

while again:
    score=0
    
    #Display introduction
    transitions.intro()
    
    #Play launch game
    score += launch.play()
    
    #Display lunar transfer explanation
    transitions.lunar()           
    
    #Play lunar transfer game
    score += lunartransfer.play()
    
    #Display landing explanation
    transitions.landing()
    
    #Play Landing game
    score += landing.play()
    
    #Display final score and end scene
    again = transitions.ending(score)

pg.quit()   