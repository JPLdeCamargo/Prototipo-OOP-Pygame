import pygame, sys
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
        # player---> inicializado no gamestate em init
        self.main_loop()

    def main_loop(self):
        while True:
            self.__event_handler.key_checker()
            
            # Fecha a janela, termina o programa
            if (self.__event_handler.output['quit'] == True):
                pygame.quit()
                sys.exit()
            

            # Executar Comandos
            # fazer isso ser mais legivel dps
            for output, value in self.__event_handler.output.items():
                for command_object in self.__game_state.command_objects:
                    for possible_command in command_object.commands.keys():
                        if output == possible_command:
                            command_object.commands[output] = value
                command_object.execute_commands()

            # update
            for i in self.__game_state.kinetic_objects:
                i.update
            # Draw
            self.__win.fill((12, 24, 255))
            for i in self.__game_state.objects:
                i.draw(self.__win)

            self.__clk.tick(self.__clk_speed)


