
# codigo para utilizar de referencia, não é meu

"""Smooth Movement in pygame"""

#Imports
import pygame, sys
import random

#Constants
WIDTH, HEIGHT = 400, 400
TITLE = "Smooth Movement"


#Player Class
class Player:
    def __init__(self, x, y):
        self.x = int(x)
        self.y = int(y)
        self.size = 32
        self.rect = pygame.Rect(self.x, self.y, self.size, self.size)
        self.color = (250, 120, 60)
        self.velX = 0
        self.velY = 0
        self.left_pressed = False
        self.right_pressed = False
        self.up_pressed = False
        self.down_pressed = False
        self.speed = 2
    
    def draw(self, win):
        pygame.draw.rect(win, self.color, self.rect)
    
    def updateRect(self):
        self.rect = pygame.Rect(int(self.x), int(self.y), self.size, self.size)

    def update(self):
        self.velX = 0
        self.velY = 0
        # Comandos dados por uma classe que conversa com event_handler
        if self.left_pressed and not self.right_pressed:
            self.velX = -self.speed
        if self.right_pressed and not self.left_pressed:
            self.velX = self.speed
        if self.up_pressed and not self.down_pressed:
            self.velY = -self.speed
        if self.down_pressed and not self.up_pressed:
            self.velY = self.speed
        
        self.x += self.velX
        self.y += self.velY 

        self.updateRect() 
         


#pygame initialization
pygame.init()
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption(TITLE)
clock = pygame.time.Clock()


#Player Initialization
player = Player(WIDTH/2, HEIGHT/2)

#Main Loop
while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player.left_pressed = True
            if event.key == pygame.K_RIGHT:
                player.right_pressed = True
            if event.key == pygame.K_UP:
                player.up_pressed = True
            if event.key == pygame.K_DOWN:
                player.down_pressed = True
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                player.left_pressed = False
            if event.key == pygame.K_RIGHT:
                player.right_pressed = False
            if event.key == pygame.K_UP:
                player.up_pressed = False
            if event.key == pygame.K_DOWN:
                player.down_pressed = False
        
    #Draw
    win.fill((12, 24, 36))  
    player.draw(win)

    #update
    player.update()
    pygame.display.flip()

    clock.tick(120)