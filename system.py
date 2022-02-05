from os import POSIX_SPAWN_CLOSE
import pygame
import sys
from game_state import Game_state
from event_handler import Event_handler


class System:
    def __init__(self, size, title, clk_speed):
        self.__size = size
        self.__title = title
        self.__clk_speed = clk_speed
        self.__win = pygame.display.set_mode((self.__size, self.__size))
        self.__clk = pygame.time.Clock()
        self.__game_state = Game_state(self.__size/2, self.__size/2)
        self.__event_handler = Event_handler()

    def initialize(self):
        pygame.init()
        pygame.display.set_caption(self.__title)
        self.main_loop()

    @staticmethod 
    def __lookForCommands(output: dict, possible_commands: dict):
        for i in output.keys():
            if i in possible_commands.keys():
                possible_commands[i] = output[i]
        return possible_commands

    def main_loop(self):
        while True:
            self.__event_handler.key_checker()

            # Fecha a janela, termina o programa
            if (self.__event_handler.output['quit'] == True):
                pygame.quit()
                sys.exit()

            # executa os comandos dados pelo event handler
            for command_object in self.__game_state.command_objects:
                OUTPUT = self.__event_handler.output
                command_object.commands = self.__lookForCommands(OUTPUT, command_object.commands)
                command_object.execute_commands()

            # update os retangulos
            for i in self.__game_state.kinetic_objects:
                i.update()
            # Draw
            self.__win.fill((12, 24, 36))
            for i in self.__game_state.objects:
                i.draw(self.__win)

            pygame.display.flip()
            self.__clk.tick(self.__clk_speed)
