import pygame
from pygame import mixer
from settings import *
from sprites import *
import random


#GAME LOOP
class Game():
    def __init__(self):
        pygame.init() #START PYGAME
        screen = pygame.display.set_mode((640, 500)) #DISPLAY THE SCREEN

        #TITLE AND ICON
        pygame.display.set_caption('Color Flow')
        icon = pygame.image.load('/Users/alvarogonzalez/Documents/PROGRAMMING/Color-Flow/simon_logo.png') #APP ICON
        pygame.display.set_icon(icon)

        # FPS
        self.clock = pygame.time.Clock() 
        self.running = True

        # ADD BACKGROUND MUSIC
        # mixer.music.load('/Users/alvarogonzalez/Documents/PROGRAMMING/Color-Flow/background_music.wav')
        # mixer.music.play(-1)  # -1 means it repeats every time it ends
    
    def new(self):
        pass
    
    def run(self):
        pass

    def update(self):
        pass

    def draw(self):
        pass

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit(0) #FINISH THE PROGRAM

    