import pygame
from pygame import mixer
from settings import *
from sprites import *



#GAME LOOP
class Game():
    def __init__(self):
        #START PYGAME
        pygame.init()
        screen = pygame.display.set_mode((640, 500)) #DISPLAY THE SCREEN
        #TITLE AND ICON
        pygame.display.set_caption('Color Flow')
        icon = pygame.image.load('/Users/alvarogonzalez/Documents/PROGRAMMING/Color-Flow/simon_logo.png') #APP ICON
        pygame.display.set_icon(icon)
        # FPS
        self.clock = pygame.time.Clock() 
        self.running = True

        # background = pygame.image.load('') #GAME BACKGROUND

        # ADD BACKGROUND MUSIC
        # mixer.music.load('/Users/alvarogonzalez/Documents/PROGRAMMING/Color-Flow/background_music.wav')
        # mixer.music.play(-1)  # -1 means it repeats every time it ends
    def run(self):

        while self.running:
            self.clock.tick(FPS)  
            self.events()  
            self.draw() 
    
    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:  # Salir si se cierra la ventana
                self.running = False

    def draw(self):
        self.screen.fill(DARKGREY)  
        pygame.display.update()  



        # while running:
        #     for event in pygame.event.get():
        #         if event.type == pygame.QUIT: #QUIT GAME
        #             running = False

game1 = Game()
game1.run()
pygame.quit()