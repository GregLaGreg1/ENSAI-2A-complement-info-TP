import copy

from business_object.pokemon.abstract_pokemon import AbstractPokemon

from business_object.pokemon.abstract_attack import AbstractAttack

from business_object.statistic import Statistic

from abc import ABC, abstractmethod

class FixedDamageAttack(AbstractAttack):

    def __init__(self, power, name, description=None):
        super().__init__(power, name, description)
    
    def compute_damage(self):
        return self._power
    

