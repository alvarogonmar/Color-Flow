import pygame
from settings import *
import math
import numpy
pygame.mixer.init()

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


# WE CAN DELETE
class Audio:
    def __init__(self, frequency):
        duration = 0.4 # DURATION OF THE BIT
        bits = 13 
        sample_rate = 40000 # hz sound
        total_samples = int(round(duration * sample_rate))
        data = numpy.zeros((total_samples, 2), dtype=numpy.int16) # MAKE ARRAY WITH ZEROS
        max_sample = 2**(bits-1) -1 
        for sample in range(total_samples):
            sample_time = float(sample) / sample_rate
            for channel in range(2):
                data[sample][channel] = int(round(max_sample * math.sin(2 * math.pi * frequency * sample_time)))
        self.sound  = pygame.sndarray.make_sound(data)
        self.current_channel = None
    
    def play(self):
        self.current_channel = pygame.mixer.find_channel(True)
        self.current_channel.play(self.sound)

class UIElement: # THING THE USER CAN WATCH OR INTERACT
    def __init__(self, x, y, text, font_path='PressStart2P-Regular.ttf', font_size='', colour=''):
        self.x = x
        self.y = y
        self.text = text
        self.font_path =font_path
        self.font_size = font_size
        self.colour = colour
    
    def draw(self, screen):
        font = pygame.font.Font(self.font_path,self.font_size) # FONT
        text_surface = font.render(self.text, True, self.colour) # TRUE: ACTIVE AN anti-aliasing (SOFT AND HD TEXT)
        screen.blit (text_surface, (self.x, self.y)) # DRAW AN OBJECT ON THE SCREEN
        
