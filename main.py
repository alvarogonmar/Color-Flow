import pygame
from pygame import mixer
from settings import *
from sprites import *
import random

# GAME LOOP
class Game:
    def __init__(self):
        # Initialize the game by setting up the window, sounds, images, and colors
        pygame.init()  
        self.screen = pygame.display.set_mode((850, 780))  # Set game window size

        # Title and window icon
        pygame.display.set_caption('Color Flow')
        icon = pygame.image.load(
            '/Users/alvarogonzalez/Documents/PROGRAMMING/Color-Flow/images/simon_logo.png'
        )  # Set the application icon
        pygame.display.set_icon(icon)

        # Background image setup
        self.background_image = pygame.image.load(
            '/Users/alvarogonzalez/Documents/PROGRAMMING/Color-Flow/images/black_image2.jpg'
        )
        self.background_image = pygame.transform.scale(self.background_image, (850, 780))

        # Frames per second (FPS)
        self.clock = pygame.time.Clock()

        # Colors for the buttons
        self.flash_colors = [RED, BLUE, GREEN, YELLOW]
        self.colors = [DARKRED, DARKBLUE, DARKGREEN, DARKYELLOW]

        # Variables for changing the title color
        self.text_color_title = 0  # First color
        self.color_change_interval = 500  # Change color every 0.5 seconds
        self.last_color_change_time = pygame.time.get_ticks()  # Track last color change time

        # Sound effects setup
        self.beep = [Audio(BEEP1), Audio(BEEP2), Audio(BEEP3), Audio(BEEP4)]
        self.steve = mixer.Sound(
            '/Users/alvarogonzalez/Documents/PROGRAMMING/Color-Flow/sounds/steve_uo.mp3'
        )

        # Background music setup
        mixer.music.load(
            '/Users/alvarogonzalez/Documents/PROGRAMMING/Color-Flow/sounds/dress_to_impress.mp3'
        )
        mixer.music.play(-1)  # Loop background music
        mixer.music.set_volume(0.15)  # Set music volume

        # Setup for buttons on the screen
        self.buttons = [
            Button(150, 210, DARKRED),  # Top left button
            Button(430, 210, DARKBLUE),  # Top right button
            Button(150, 490, DARKGREEN),  # Bottom left button
            Button(430, 490, DARKYELLOW),  # Bottom right button
        ]

    def get_high_score(self):
        # Get the highest score from the file
        with open('high_score.txt', 'r') as file:
            score = file.read()
        return int(score)

    def save_score(self):
        # Save the current score if it is higher than the previous high score
        with open('high_score.txt', 'w') as file:
            if self.score > self.high_score:
                file.write(str(self.score))
            else:
                file.write(str(self.high_score))

    def new_round(self):
        # Reset game variables for a new round
        self.waiting_input = False
        self.pattern = []
        self.current_step = 0
        self.score = 0
        self.high_score = self.get_high_score()

    def run(self):
        # Main game loop
        self.running = True
        while self.running:
            self.clock.tick(60)  # Limit to 60 frames per second
            self.click_button = None
            self.events()
            self.draw()
            self.update()

    def update(self):
        # Handle game updates, including pattern generation and player input
        if not self.waiting_input:
            pygame.time.wait(1000)  # Wait 1 second before adding to the pattern
            self.pattern.append(random.choice(self.colors))  # Add random color to pattern
            for button in self.pattern:
                self.button_animation(button)  # Flash color animation for each button
                pygame.time.wait(200)  # Pause between flashes
            self.waiting_input = True  # Ready for player input
        else:
            if self.click_button and self.click_button == self.pattern[self.current_step]:
                # If the correct button is clicked, animate the button
                self.button_animation(self.click_button)
                self.current_step += 1

                if self.current_step == len(self.pattern):
                    # If all steps are completed, increment score and reset for next round
                    self.score += 1
                    self.waiting_input = False
                    self.current_step = 0
            elif self.click_button and self.click_button != self.pattern[self.current_step]:
                # If incorrect button is clicked, show game over animation and reset the game
                self.game_over_animation()
                self.save_score()
                self.running = False

    def button_animation(self, color):
        # Animate button flashing and play corresponding sound
        for colors1 in range(len(self.colors)):
            if self.colors[colors1] == color:
                sound = self.beep[colors1]
                flash_color = self.flash_colors[colors1]
                button = self.buttons[colors1]

        original_surface = self.screen.copy()
        flash_surface = pygame.Surface((BUTTON_SIZE, BUTTON_SIZE))
        flash_surface = flash_surface.convert_alpha()
        r, g, b = flash_color

        sound.play()  # Play the sound for the button

        for start, end, step in ((0, 255, 1), (255, 0, -1)):
            # Animate the button fading in and out
            for alpha in range(start, end, ANIMATION_SPEED * step):
                self.screen.blit(original_surface, (0, 0))
                flash_surface.fill((r, g, b, alpha))
                self.screen.blit(flash_surface, (button.x, button.y))
                pygame.display.update()
                self.clock.tick(60)  # Control frame rate
        self.screen.blit(original_surface, (0, 0))

    def game_over_animation(self):
        # Display game over animation with screen fading
        original_surface = self.screen.copy()
        flash_surface = pygame.Surface(self.screen.get_size())
        flash_surface = flash_surface.convert_alpha()
        self.steve.play()  # Play game over sound

        r, g, b = PURPLE_DEAD
        for _ in range(3):
            # Flash the entire screen with the game over color
            for start, end, step in ((0, 255, 1), (255, 0, -1)):
                for alpha in range(start, end, GAME_OVER_ANIMATION_SPEED * step):
                    self.screen.blit(original_surface, (0, 0))
                    flash_surface.fill((r, g, b, alpha))
                    self.screen.blit(flash_surface, (0, 0))
                    pygame.display.update()
                    self.clock.tick(60)

    def draw(self):
        # Draw the background, score, high score, and buttons on the screen
        self.screen.blit(self.background_image, (0, 0))

        UIElement(
            100, 100, f'Score: {str(self.score)}', 'PressStart2P-Regular.ttf', 25, WHITE
        ).draw(self.screen)
        UIElement(
            500, 100, f'High Score {str(self.high_score)}', 'PressStart2P-Regular.ttf',
            25, WHITE
        ).draw(self.screen)

        # Get the current time
        current_time = pygame.time.get_ticks()

        # Change the title text color every 0.5 seconds
        if current_time - self.last_color_change_time > self.color_change_interval:
            self.text_color_title = (self.text_color_title + 1) % len(self.flash_colors)
            self.last_color_change_time = current_time

        # Select the current color for the title
        current_color = self.flash_colors[self.text_color_title]

        # Draw the title with the current color
        UIElement(
            220, 20, 'Color Flow', 'PressStart2P-Regular.ttf', 40, current_color
        ).draw(self.screen)

        for button in self.buttons:
            # Draw each button
            button.draw(self.screen)
        pygame.display.update()

    def events(self):
        # Handle user input events, such as quitting or mouse clicks
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit(0)  # End the program

            # Check for mouse click events
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = pygame.mouse.get_pos()
                for button in self.buttons:
                    if button.click(mouse_x, mouse_y):  # Check if a button was clicked
                        self.click_button = button.color


game = Game()
while True:  # Infinite loop to keep the game running
    game.new_round()  # Start a new game round
    game.run()
