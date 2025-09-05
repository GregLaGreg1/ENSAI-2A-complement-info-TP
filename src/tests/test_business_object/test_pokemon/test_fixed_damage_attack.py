from business_object.pokemon.fixed_damage_attack import FixedDamageAttack
from business_object.statistic import Statistic

class TestFixedDamageAttack:
    def test_get_coef_damage_type(self):
        # GIVEN
        Degat_fixe = FixedDamageAttack(30, "Dracaufeu")

        # WHEN
        res = Degat_fixe.compute_damage()

        # THEN
        assert res == 30


if __name__ == "__main__":
    import pytest

    pytest.main([__file__])