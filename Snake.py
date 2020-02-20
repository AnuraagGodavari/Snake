import pygame, random, json
import SnakeObjects

pygame.init()

with open("GameData/Settings.json") as f:
    settings = json.load(f)

try: #Try and get the values from settings
    scrWidth = int(settings["Screen Width"])*10 #Screen Width
    scrHeight = int(settings["Screen Height"])*10 #Screen Height
    tickSpeed = settings["Starting Speed"] #Starting speed of the game
    tickIncrease = 2 #How much the tick speed increases by initially, is afterwards multiplied by tickIncreaseMultiplier
    tickIncreaseMultiplier = settings["Speed Increase Amount (1-100)"]*0.01 #Multiplies tickIncrease, slowing down the difficulty rise
    
    if (scrWidth < 50) or (scrHeight < 50):
        raise Exception("ERROR: A value is out of the required bounds")
        
    nextLevelRequirement = 50
    increasingFood = settings["Increasing Food"]
    
except:
    print("ERROR: Settings.json not readable")
    scrWidth = 1000 
    scrHeight = 750 
    tickSpeed = 15
    tickIncrease = 2
    tickIncreaseMultiplier = 0.85
    nextLevelRequirement = 50
    increasingFood = True

win = pygame.display.set_mode((scrWidth, scrHeight)) #Generates the window

backdrop = pygame.image.load('GameData/backdrop.png') #Plain black background

clock = pygame.time.Clock() #Gets a clock

score = 0

lost = False #Has the game been lost?

captionBase = "Snake! Score: " #The window caption, displaying the game name and score

canEat = False
snake = SnakeObjects.Snake(scrWidth, scrHeight)
foods = [SnakeObjects.Food(scrWidth, scrHeight)]

def redrawWindow():
    pygame.display.set_caption(captionBase + str(score)) #Sets the window caption
    win.blit(backdrop, (0,0))
    for food in foods:
        food.draw(win)
    snake.draw(win)
    pygame.display.update()

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
    
    for food in foods: #Cycles through each food in foods list
        canEat = snake.canEat(food)
        
        if (canEat):
            snake.move(canEat)
            score += 10
            tickSpeed += tickIncrease
            tickIncrease *= tickIncreaseMultiplier
            if(score == nextLevelRequirement & increasingFood):
                foods.append(SnakeObjects.Food(scrWidth, scrHeight))
                nextLevelRequirement*=1.5
            canEat = False
    
    if not (snake.newFrame(canEat)):
        redrawWindow()
    else:
        running = False

pygame.quit()