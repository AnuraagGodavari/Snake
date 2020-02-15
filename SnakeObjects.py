#Snake Objects
'''
This File contains all the objects used in the snake game.
'''

import random, pygame
pygame.init() #Gets all pygame libraries 

whiteSquare = pygame.image.load('Snake Piece.png')

class Snake(object): #The entire Snake. Basically a doubly - linked list
    
    def __init__(self, xRange, yRange):
        self.tail = self.head = SnakePiece(int(int(xRange/10)/2)*10, int(int(yRange/10)/2) * 10) #The first Snake Piece, if head has no next then tail is automatically made into the next.
        self.xRange = xRange
        self.yRange = yRange
        self.yDir = 0
        self.xDir = 0
        
    #On every new Frame, move and draw the snake, and check the lose conditions
    def newFrame(self, newPiece):
        self.move(newPiece)
        return self.hasCollided()
    
    def move(self, newPiece):
    
        if self.head.next != None: #If there is more than one piece, add a new head to simulate movement
        
            if not newPiece: #If there is not a new piece, remove the current tail and replace it with its previous
                    
                self.tail = self.tail.previous #Tail is removed, new tail is the piece just before it
                self.tail.next = None
                
            self.head = SnakePiece(self.head.x + (self.xDir * 10), self.head.y + (self.yDir * 10), self.head) #New head, represents movement in a direction
            
            if not (self.head.next.previous):
                self.head.next.previous = self.head
            
        else: #If only one piece, move the head
            if newPiece:
                self.tail = SnakePiece(self.head.x, self.head.y, None, self.head)
                self.head.next = self.tail
            self.head.x += self.xDir * 10
            self.head.y += self.yDir * 10
            
        #Keep in mind: yDir = -1 means up, xDir = 1 means down
        
        self.head.checkOutOfBounds(self.xRange, self.yRange)
    
    def canEat(self, food):
        if (self.head.x == food.x and self.head.y == food.y):
            food.reposition()
            return True
        return False
    
    def hasCollided(self):
        if self.head.next:
            if(self.head.next.hasCollided(self.head.x, self.head.y)): #If any of the pieces has collided with the head, return true
                return True
        return False
        
    def getKey(self): 
        
        keys = pygame.key.get_pressed()

        if keys[pygame.K_w] and self.yDir != 1: #If w is in the keys and its not moving down, change its direction to up
            self.xDir, self.yDir = 0, -1
        elif keys[pygame.K_s] and self.yDir != -1:
            self.xDir, self.yDir = 0, 1
        elif keys[pygame.K_a] and self.xDir != 1:
            self.xDir, self.yDir = -1, 0
        elif keys[pygame.K_d] and self.xDir != -1:
            self.xDir, self.yDir = 1, 0
            
    def draw(self, win):
        self.head.draw(win) #Draws each snake piece, starting with the head

class SnakePiece(object): #One Node in the "Linked List" that is the snake.

    def __init__ (self, x, y, next = None, previous = None):
        self.x = x
        self.y = y
        self.next = next #The next Snake Piece
        self.previous = previous #Previous Snake Piece
            
    def hasCollided (self, x, y):
        if (self.x == x and self.y == y):
            return True
        elif self.next:
            return self.next.hasCollided(x, y)
        return False
        
    def draw (self, win):
        win.blit(whiteSquare, (self.x, self.y))
        if (self.next):
            self.next.draw(win)
    
    def checkOutOfBounds(self, xRange, yRange):
        if (self.x > xRange): self.x = 0
        elif (self.x < 0): self.x = xRange
        
        if (self.y > yRange): self.y = 0
        elif (self.y < 0): self.y = yRange
    
class Food(object):
    
    def __init__ (self, xRange, yRange):
        self.xRange = xRange
        self.yRange = yRange
        self.x = None
        self.y = None
        self.reposition()        
        
    def reposition(self):
        self.x = random.randint(50, (self.xRange/10) - 5)*10 #Generates random placement on the map, x coordinate
        self.y  = random.randint(50, (self.yRange/10) - 5)*10 #Generates random placement on the map, y coordinate
        
    def draw (self, win):
        win.blit(whiteSquare, (self.x, self.y))

#Bottom 1

























#Bottom 2 Electric Boogaloo
            
