from business_object.pokemon.supporter_pokemon import SupporterPokemon
from business_object.statistic import Statistic


class TestSupporterPokemon:
    def test_get_coef_damage_type(self):
        # GIVEN
        dracaufeu= SupporterPokemon(stat_current=Statistic(sp_atk=100, defense=100))

        # WHEN
        multiplier = dracaufeu.get_pokemon_attack_coef()

        # THEN
        assert multiplier == 2

class TestLevelup :
    def test_level_up(self):
        dracaufeu= SupporterPokemon(stat_current=Statistic(sp_atk=100, defense=100),level=54)
        level = dracaufeu.level_up()
        assert dracaufeu.level == 55

if __name__ == "__main__":
    import pytest

    pytest.main([__file__])
