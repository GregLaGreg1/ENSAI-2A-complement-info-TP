from business_object.pokemon.speedster_pokemon import SpeedsterPokemon
from business_object.statistic import Statistic


class TestSpeedsterpokemon:
    def test_get_coef_damage_type(self):
        # GIVEN
        ratata = SpeedsterPokemon(stat_current=Statistic(speed=100, sp_atk=100))

        # WHEN
        multiplier = ratata.get_pokemon_attack_coef()

        # THEN
        assert multiplier == 2


if __name__ == "__main__":
    import pytest

    pytest.main([__file__])
