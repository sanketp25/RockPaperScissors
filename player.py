import pygame
from button import Button

class Player:
    def __init__(self):
        self.rock = Button(100,350,100,100,(255,0,0),"Rock")
        self.paper = Button(310,350,100,100,(0,255,0),"Paper")
        self.scissor = Button(520,350,100,100,(0,0,255),"Scissor")
    def draw(self,window):
        self.rock.draw(window)
        self.paper.draw(window)
        self.scissor.draw(window)
