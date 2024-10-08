import pygame
from pygame import mixer
from settings import *
from sprites import *
import random


#GAME LOOP
class Game:
    def __init__(self):
        pygame.init() #START PYGAME
        self.screen = pygame.display.set_mode((850, 780)) #DISPLAY THE SCREEN

        #TITLE AND ICON
        pygame.display.set_caption('Color Flow')
        icon = pygame.image.load('/Users/alvarogonzalez/Documents/PROGRAMMING/Color-Flow/simon_logo.png') #APP ICON
        pygame.display.set_icon(icon)

        # FPS
        self.clock = pygame.time.Clock() 

        # COLOURS
        self.flash_colours = [YELLOW, BLUE, RED, GREEN]
        self.colours = [DARKYELLOW, DARKBLUE, DARKRED, DARKGREEN]

        # SOUNDS
        self.beep = [Audio(BEEP1), Audio(BEEP2), Audio(BEEP3), Audio(BEEP4)]

        # ADD BACKGROUND MUSIC
        # mixer.music.load('/Users/alvarogonzalez/Documents/PROGRAMMING/Color-Flow/background_music.wav')
        # mixer.music.play(-1)  # -1 means it repeats every time it ends
        self.buttons = [
            Button(150, 210, DARKRED),    # Left top
            Button(430, 210, DARKBLUE),   # Right top
            Button(150, 490, DARKGREEN),  # Left botton
            Button(430, 490, DARKYELLOW)  # Right botton
        ]
    def new(self):
        self.waiting_input = False
        self.pattern = []
        self.current_step = 0
        self.score = 0

    
    def run(self):
        self.running = True
        while self.running:
            self.clock.tick(60) #FPS
            self.events() 
            self.draw()
            self.update()
            self.clicked_button = None

    #PATTERN DEF
    def update(self):
        if not self.waiting_input: # IF IF NOT WAITING FOR INPUT, THAT MEANS THE PROGRAM HAVE TO GIVE US THE PATTERN
            pygame.time.wait(1000)
            self.pattern.append(random.choice(self.colours)) #CHOOSING A RANDOM COLOR FROM THE LIST AND ADDING IT TO THE PATTERN
            for button in self.pattern:
                self.button_animation(button) # FLASH COLOUR
                pygame.time.wait(200)
            self.waiting_input = True
        else: 
            # PUSH THE CORRECT BUTTON
            if self.click_button and self.click_button == self.pattern[self.current_step]:
                self.button_animation(self.click_button)
                self.current_step += 1

                #PUSHED THE LAST BUTTON
                if self.current_step == len(self.pattern):
                    self.score += 1
                    self.waiting_input = False
                    self.current_step = 0

            elif self.click_button and self.click_button != self.pattern[self.current_step]:
                self.game_over_animation()
                self.save_Score()
                self.running = False


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
            
            #CHECK IF THE MOUSE IS PRESSED
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = pygame.mouse.get_pos()
                for button in self.buttons:
                    if button.click(mouse_x, mouse_y): # CLASS IN SPRITES
                        self.click_button = button.colour
game = Game()
while True: # INFINITE LOOP TO KEEP THE GAME RUNNING
    game.new() # START A NEW GAME ROUND
    game.run()  