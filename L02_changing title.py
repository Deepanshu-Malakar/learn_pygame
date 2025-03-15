import pygame
import pygame.display
pygame.init()

# creating the screen..............................
screen = pygame.display.set_mode((1960*0.5,1080*0.5))
#.................................................


# setting the title of the screen...................
pygame.display.set_caption("Game Title")
#...................................................


#setting the icon of game...........................
icon = pygame.image.load("icon_image.png")
pygame.display.set_icon(icon)
#...................................................

#main loop of game..............................
running:bool = True
while(running):
    for event in pygame.event.get():
        if(event.type == pygame.QUIT): 
            running = False