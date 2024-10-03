import pygame

pygame.init() #START PYGAME

screen = pygame.display.set_mode((800, 600)) #DISPLAY THE SCREEN

#TITLE AND ICON
pygame.display.set_caption('Color Flow')

#GAME LOOP
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: #QUIT GAME
            running = False