import pygame
import pygame.display
pygame.init()
screen = pygame.display.set_mode((1960*0.5,1080*0.5))
pygame.display.set_caption("Game Title")
icon = pygame.image.load("icon_image.png")
pygame.display.set_icon(icon)


#defineing colors...............................
background_color:tuple = (119,133,255)
#here 
# tuple[0] = red value
# tuple[1] = green value
# tuple[2] = blue value
#each color is represented in terms of rgb values
#you can even add tuple[3]
#tuple[3] denotes alpha value (means transparency)

#...............................................

#main loop of game..............................
running:bool = True
while(running):
    for event in pygame.event.get():
        if(event.type == pygame.QUIT): 
            running = False

    
    # changing the background color of the game.....

    screen.fill(background_color)   #you have changed the screen color but you now have to update the display
    #remember whenever you change anything on display you need to update display
    

    #updating the display
    pygame.display.update()
    #...............................................