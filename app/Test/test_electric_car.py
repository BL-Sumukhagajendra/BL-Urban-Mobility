import pytest
from app.models.electric_cars import ElectricCar

@pytest.fixture
def electric_car_object():
    return ElectricCar(1, "Tesla")

class TestElectrifcCar():
    def test_seating_capacity(self, electric_car_object):
        electric_car_object.seating_capacity = 5
        assert electric_car_object.seating_capacity == 5

    def test_calculate_trip_cost(self, electric_car_object):
        trip_cost = electric_car_object.calculate_trip_cost(20)
        assert trip_cost == 700

    def test_negetive_trip_cost(self, electric_car_object):
        with pytest.raises(ValueError):
            electric_car_object.calculate_trip_cost(-10)