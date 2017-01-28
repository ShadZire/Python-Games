import pygame

pygame.init()

white = (255,255,255)
red = (255,0,0)
black = (0,0,0)
blue = (0,0,255)

gameDisplay = pygame.display.set_mode((800,600))
pygame.display.set_caption('Snakie')

#pygame.display.flip()


gameExit = False

lead_x = 300
lead_y = 300
lead_x_change = 0
while not gameExit:
    for event in pygame.event.get():
        print(event)
        if event.type == pygame.QUIT:
            gameExit = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                lead_x_change -= 10
            if event.key == pygame.K_RIGHT:
                lead_x_change += 10
                
    lead_x += lead_x_change
     
    gameDisplay.fill(white)
    pygame.draw.rect(gameDisplay, red, [lead_x,lead_y,10,10])

    #gameDisplay.fill(red, rect=[200,200,50,10])

    pygame.display.update()


pygame.quit()
quit()
