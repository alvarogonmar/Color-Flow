import pygame
from pygame import mixer
from settings import *
from sprites import *
import random


#GAME LOOP
class Game:
    def __init__(self):
        pygame.init() #START PYGAME
        self.screen = pygame.display.set_mode((1000, 740)) #DISPLAY THE SCREEN

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
        self.buttons = [
            Button(230, 220, DARKRED),    # Left, top
            Button(520, 220, DARKBLUE),   # Right top
            Button(230, 490, DARKGREEN),  # Left botton
            Button(520, 490, DARKYELLOW)  # Right botton
        ]
    def new(self):
        pass
    
    def run(self):
        self.playing = True
        while self.playing:
            self.clock.tick(60) #FPS
            self.events() 
            self.draw()
            self.update()

    def update(self):
        pass

    def draw(self):
        self.screen.fill(BACKGROUNDCOLOUR)
        for button in self.buttons:
            button.draw(self.screen)
        pygame.display.update()

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit(0) #FINISH THE PROGRAM

game = Game()
while True: # INFINITE LOOP TO KEEP THE GAME RUNNING
    game.new() # START A NEW GAME ROUND
    game.run()  