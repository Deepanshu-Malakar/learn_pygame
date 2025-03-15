import pygame
pygame.init()

# creating the screen
screen = pygame.display.set_mode((1960*0.5,1080*0.5))
#if we just write this above code the screen will appear and then disappear in a fraction of second 
# so to solve this problem we keep our code in a while loop to keep the window turned on

running:bool = True
while(running):
    for event in pygame.event.get():
        if(event.type == pygame.QUIT):  #when you press the close button on right of title bar the window will close
            running = False