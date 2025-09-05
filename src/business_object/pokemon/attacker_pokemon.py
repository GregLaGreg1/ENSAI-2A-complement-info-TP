import copy
from business_object.pokemon.abstract_pokemon import AbstractPokemon

from business_object.statistic import Statistic
from abc import ABC, abstractmethod

class AttackerPokemon(AbstractPokemon):

    def __innit__(self):
        super().__init__(self, stat_max=None, stat_current=None, level=0, name=None, type_pk=None)

    def get_pokemon_attack_coef(self):
        multiplier = 1 + (self.speed_current + self.attack_current) / 200
        return multiplier