import pytest

from src.shared.helpers.errors.domain_errors import EntityError
from src.shared.domain.entities.hamburguer import Hamburguer
from src.shared.domain.enums.flavor_enum import FLAVOR

class Test_Hamburguer():
    def test_hamburguer(self):
        hamburguer = Hamburguer(flavor=FLAVOR.BEEF)
        assert hamburguer.flavor == FLAVOR.BEEF
        
    def test_hamburguer_flavor_must_be_flavor(self):
        with pytest.raises(EntityError):
            hamburguer = Hamburguer(flavor=1)