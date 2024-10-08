import pygame
from settings import *

class Button:
    def __init__(self, x, y, colour): # x AND y IS WHERE WE WANT TO SHOW THE BUTTONS
        self.x = x
        self.y = y
        self.colour = colour

    def draw(self, screen):
        # DRAW THE RECTANGLE ON THE SCREEN (self.colour=colour, self.x = position on x, self.y = position on y, BUTTON_SIZE= WIDTH AND HEIGHT)))
        pygame.draw.rect(screen, self.colour, (self.x, self.y, BUTTON_SIZE, BUTTON_SIZE))

    def click(self, mouse_x, mouse_y): #CLICKING 
        # RETURN TRUE IF MOUSE_X AND MOUSE_Y ARE INSIDE OF THE RECTANGLE 
        return self.x <= mouse_x <= self.x + BUTTON_SIZE and self.y <= mouse_y <= self.y + BUTTON_SIZE
    