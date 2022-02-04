import pygame, sys
import math
class Player:
    def __init__(self, initial_x: int, initial_y: int, size: int, speed: int):
        self.__x = initial_x
        self.__y = initial_y
        self.__size = size
        self.__rect = pygame.Rect(self.__x, self.__y, size, size)
        #depois vai ser um sprite
        self.__color = (250, 160, 60)
        self.__speed = speed
        self.__velX = 0
        self.__velY = 0
        self.__commands = {'up': False, 'down': False, 'right': False, 'left': False}

    @property
    def commands(self):
        return self.__commands
    
    # usar para normalizar os vetores de velocidade, caso contrario, anda mais rápido nas diagonais
    def normalize(self):
        if self.__velX != 0 and self.__velY != 0:
            self.__velX *=  1/math.sqrt(2)
            self.__velY *= 1/math.sqrt(2)

    def draw(self, win):
        pygame.draw.rect(win, self.__color, self.__rect)

    def execute_commands(self):
        self.__velX = 0
        self.__velY = 0
        if self.__commands['left'] and not self.__commands['right']:
            self.__velX = -self.__speed
        if self.__commands['right'] and not self.__commands['left']:
            self.__velX = self.__speed
        if self.__commands['up'] and not self.__commands['down']:
            self.__velY = -self.__speed
        if self.__commands['down'] and not self.__commands['up']:
            self.__velY = self.__speed
        
        self.__x += self.__velX
        self.__y += self.__velY 

    def update(self):
        self.__rect = pygame.Rect(int(self.__x), int(self.__y), self.__size, self.__size)

    


