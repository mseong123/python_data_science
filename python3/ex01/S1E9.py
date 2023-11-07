from abc import ABC, abstractmethod


class Character(ABC):
    """Base character class"""
    @abstractmethod
    def __init__(self, first_name, is_alive=True):
        """constructor Character class (Abstract)"""
        self.first_name = first_name
        self.is_alive = is_alive

    def die(self):
        """Kills the character"""
        self.is_alive = False


class Stark(Character):
    """Stark Class inherited from Character Base class"""
    def __init__(self, first_name, is_alive=True):
        """constructor Stark class"""
        super().__init__(first_name, is_alive)
