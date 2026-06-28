import pytest
from app.models.electric_scooter import ElectricScooter

@pytest.fixture
def electric_scooter_object():
    return ElectricScooter(1, "Tesla")

class TestElectricScooter():
    def test_max_speed_limit(self, electric_scooter_object):
        electric_scooter_object.max_speed_limit = 10
        assert electric_scooter_object.max_speed_limit == 10

    def test_calculate_trip_cost(self, electric_scooter_object):
        trip_cost = electric_scooter_object.calculate_trip_cost(20)
        assert trip_cost == 4.0

    def test_negetive_trip_cost(self, electric_scooter_object):
        with pytest.raises(ValueError):
            electric_scooter_object.calculate_trip_cost(-10)