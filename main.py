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

        #BACKGROUND IMAGE
        self.background_image = pygame.image.load('/Users/alvarogonzalez/Documents/PROGRAMMING/Color-Flow/black_image2.jpg')
        self.background_image = pygame.transform.scale(self.background_image, (850, 780))

        # FPS
        self.clock = pygame.time.Clock() 

        # COLOURS
        self.flash_colours = [RED, BLUE, GREEN, YELLOW]
        self.colours = [DARKRED, DARKBLUE, DARKGREEN, DARKYELLOW]

         # COUNTER FOR CHANGING THE COLORS
        self.text_color_title = 0  # FIRST COLOR
        self.color_change_interval = 500  # CHANGE COLOR EVERY 0.5 SECONDS
        self.last_color_change_time = pygame.time.get_ticks()  # GETS THE LAST TIME COLOR CHANGED

        # SOUNDS
        self.beep = [Audio(BEEP1), Audio(BEEP2), Audio(BEEP3), Audio(BEEP4)]
        self.steve = mixer.Sound('/Users/alvarogonzalez/Documents/PROGRAMMING/Color-Flow/steve_uo.mp3')
        
        # ADD BACKGROUND MUSIC
        mixer.music.load('/Users/alvarogonzalez/Documents/PROGRAMMING/Color-Flow/dress_to_impress.mp3')
        mixer.music.play(-1)  # -1 means it repeats every time it ends
        mixer.music.set_volume(0.15) # MUSIC VOLUME

        self.buttons = [
            Button(150, 210, DARKRED),    # Left top
            Button(430, 210, DARKBLUE),   # Right top
            Button(150, 490, DARKGREEN),  # Left botton
            Button(430, 490, DARKYELLOW)  # Right botton
        ]

    def get_high_score(self):
        with open('high_score.txt', 'r') as file:
            score = file.read()
        return int(score)

    def save_score(self):
        with open('high_score.txt', 'w') as file:
            if self.score > self.high_score: # IF CURRENT SCORE IS MORE THAN THE HIGH SCORE +
                file.write(str(self.score)) # + WRITE THAT SCORE INTO THE FILE
            else:
                file.write(str(self.high_score))

    def new_round(self):
        self.waiting_input = False
        self.pattern = []
        self.current_step = 0
        self.score = 0
        self.high_score = self.get_high_score()

    
    def run(self):
        self.running = True
        while self.running:
            self.clock.tick(60) #FPS
            self.click_button = None
            self.events() 
            self.draw()
            self.update()

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
                self.save_score()
                self.running = False


    def button_animation(self, colour):
        for colours1 in range(len(self.colours)):
            if self.colours[colours1] == colour:
                sound =self.beep[colours1]
                flash_colour = self.flash_colours[colours1]
                button = self.buttons[colours1]

        original_surface = self.screen.copy()
        flash_surface = pygame.Surface((BUTTON_SIZE, BUTTON_SIZE))
        flash_surface = flash_surface.convert_alpha() 
        r, g, b = flash_colour
        
        sound.play()
        
        for start, end, step in ((0, 255, 1), (255, 0, -1)):
            for alpha in range(start, end, ANIMATION_SPEED * step):
                self.screen.blit(original_surface, (0, 0))
                flash_surface.fill((r, g, b, alpha))
                self.screen.blit(flash_surface, (button.x, button.y))
                pygame.display.update()
                self.clock.tick(60)
        self.screen.blit(original_surface, (0, 0))
    
    def game_over_animation(self):
        original_surface = self.screen.copy()
        flash_surface = pygame.Surface((self.screen.get_size()))
        flash_surface = flash_surface.convert_alpha()
        self.steve.play()

        r, g, b = PURPLE
        for _ in range(3):
            for start, end, step in ((0, 255, 1), (255, 0, -1)):
                for alpha in range(start, end, GAME_OVER_ANIMATION_SPEED * step):
                    self.screen.blit(original_surface, (0, 0))
                    flash_surface.fill((r, g, b, alpha))
                    self.screen.blit(flash_surface, (0, 0))
                    pygame.display.update()
                    self.clock.tick(60)

    def draw(self):
        self.screen.blit(self.background_image, (0, 0))

        UIElement(100, 100, f'Score: {str(self.score)}', 'PressStart2P-Regular.ttf', 25, WHITE).draw(self.screen)
        UIElement(500, 100, f'High Score {str(self.high_score)}', 'PressStart2P-Regular.ttf', 25, WHITE).draw(self.screen)

        # GET ACTUAL TIME
        current_time = pygame.time.get_ticks()

        # CHANGE THE TEXT COLOR EVERY O.5s
        if current_time - self.last_color_change_time > self.color_change_interval:
            self.text_color_title = (self.text_color_title + 1) % len(self.flash_colours)
            self.last_color_change_time = current_time  # UPDATES THE TIME OF THE LAST COLOUR CHANGED

        # SELECT THE ACTUAL COLOR
        current_color = self.flash_colours[self.text_color_title]
        
        # DRAWS THE TEXT WITH THE ACTUAL COLOR
        UIElement(220, 20, f'Color Flow', 'PressStart2P-Regular.ttf', 40, current_color).draw(self.screen)



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
    game.new_round() # START A NEW GAME ROUND
    game.run()  