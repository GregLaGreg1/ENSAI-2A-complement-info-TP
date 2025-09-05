import copy

from business_object.pokemon.abstract_pokemon import AbstractPokemon

from business_object.statistic import Statistic

from abc import ABC, abstractmethod

class AbstractAttack(ABC):

    def __init__(self, power, name, description=None):
        self._power = power
        self._name = name
        self._description = description

    @abstractmethod
    def compute_damage(self):
        pass