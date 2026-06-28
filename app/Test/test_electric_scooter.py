import pytest
from app.models.electric_scooter import ElectricScooter

@pytest.fixture
def electric_scooter_object():
    return ElectricScooter(1, "Tesla")

class TestElectricScooter():
    def test_max_speed_limit(self, electric_scooter_object):
        electric_scooter_object.max_speed_limit = 10
        assert electric_scooter_object.max_speed_limit == 10

    
