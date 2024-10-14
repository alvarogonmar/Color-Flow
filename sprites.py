import pygame
import math
import numpy
from settings import *

# Button class to represent interactive elements in the game
class Button:
    def __init__(self, x, y, color):
        # Initialize button position and color
        self.x = x
        self.y = y
        self.color = color

    def draw(self, surface):
        # Draw the button on the screen
        pygame.draw.rect(surface, self.color, (self.x, self.y, BUTTON_SIZE, BUTTON_SIZE))

    def click(self, mouse_x, mouse_y):
        # Check if the button was clicked based on mouse coordinates
        return (
            self.x <= mouse_x <= self.x + BUTTON_SIZE and
            self.y <= mouse_y <= self.y + BUTTON_SIZE
        )

# Audio class to manage sound effects in the game
class Audio:
    def __init__(self, frequency):
        # Duration of the sound and other parameters
        duration = 0.4  # Duration of the sound in seconds
        bits = 13  # Bit depth
        sample_rate = 40000  # Sample rate in Hz
        total_samples = int(round(duration * sample_rate))  # Total samples required by the samples rates in the duration of the audio in seconds 
        data = numpy.zeros((total_samples, 2), dtype=numpy.int16)  # Create an array with zeros
        max_sample = 2**(bits - 1) - 1  # Maximum sample value

        for sample in range(total_samples):
            sample_time = float(sample) / sample_rate
            for channel in range(2):
                data[sample][channel] = int(round(max_sample * math.sin(2 * math.pi * frequency * sample_time)))
        
        self.sound = pygame.sndarray.make_sound(data)  # Create the sound from the generated data
        self.current_channel = None  # Initialize the current audio channel

    def play(self):
        # Play the sound on an available audio channel
        self.current_channel = pygame.mixer.find_channel(True)
        self.current_channel.play(self.sound)

# Texts class to create text elements on the screen
class Texts:
    def __init__(self, x, y, text, font_path='PressStart2P-Regular.ttf', font_size='', color=''):
        # Initialize text position, content, font path, size, and color
        self.x = x
        self.y = y
        self.text = text
        self.font_path = font_path
        self.font_size = font_size
        self.color = color

    def draw(self, surface):
        # Draw the text on the provided surface
        font = pygame.font.Font(self.font_path, self.font_size)  # Load the font
        text_surface = font.render(self.text, True, self.color)  # Render the text
        surface.blit(text_surface, (self.x, self.y))  # Draw the text on the surface
