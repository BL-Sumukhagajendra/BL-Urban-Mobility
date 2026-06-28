import pytest
from app.models.electric_cars import ElectricCar

@pytest.fixture
def electric_car_object():
    return ElectricCar(1, "Tesla")

class TestElectrifcCar():
    def test_seating_capacity(self, electric_car_object):
        electric_car_object.seating_capacity = 5
        assert electric_car_object.seating_capacity == 5