import pygame, random
import SnakeObjects

pygame.init()

scrWidth = 1000 #Screen Width in Grid Boxes
scrHeight = 750 #Screen Height in Grid Boxes

win = pygame.display.set_mode((scrWidth, scrHeight)) #Generates the window

backdrop = pygame.image.load('backdrop.png') #Plain black background

clock = pygame.time.Clock() #Gets a clock

score = 0
lost = False #Has the game been lost?

captionBase = "Snake! Score: " #The window caption, displaying the game name and score

snake = SnakeObjects.Snake(scrWidth, scrHeight)
food = SnakeObjects.Food(scrWidth, scrHeight)

def redrawWindow():
    pygame.display.set_caption(captionBase + str(score)) #Sets the window caption
    win.blit(backdrop, (0,0))
    food.draw(win)
    snake.draw(win)
    pygame.display.update()
    
tickSpeed = 20

running = True #Is the game still going
while running:
    clock.tick(tickSpeed) #How fast the game is running

    for event in pygame.event.get():
        if event.type == pygame.QUIT: #Stops the loop if x button is pressed on window
            running = False
    
    snake.getKey()

    if lost:
        running = False
        print("You have lost.")
    
    canEat = snake.canEat(food)
    
    if (canEat):
        snake.move(canEat)
        score += 10
        tickSpeed += 2
    
    if not (snake.newFrame(canEat)):
        redrawWindow()
    else:
        running = False

pygame.quit()