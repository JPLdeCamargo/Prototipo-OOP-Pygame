from player import Player
class Game_state:
    def __init__(self, playerX, playerY):
        self.__player =  Player(playerX, playerY, 50, 3)
        self.__objects = [self.__player]
        self.__kinetic_objects = [self.__player]
        self.__command_objects = [self.__player]

    @property
    def player(self):
        return self.__player
    @property
    def objects(self):
        return self.__objects
    @property
    def kinetic_objects(self):
        return self.__kinetic_objects
    @property
    def command_objects(self):
        return self.__command_objects