import pygame
from pygame import mixer

pygame.init() #START PYGAME

screen = pygame.display.set_mode((800, 600)) #DISPLAY THE SCREEN

#TITLE AND ICON
pygame.display.set_caption('Color Flow')
icon = pygame.image.load('/Users/alvarogonzalez/Documents/PROGRAMMING/Color-Flow/simon_logo.png') #APP ICON
pygame.display.set_icon(icon)
background = pygame.image.load('') #GAME BACKGROUND

# ADD BACKGROUND MUSIC
mixer.music.load('')
mixer.music.play(-1)  # -1 means it repeats every time it ends

#GAME LOOP
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: #QUIT GAME
            running = False