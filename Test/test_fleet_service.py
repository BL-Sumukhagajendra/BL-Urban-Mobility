from app.models.electric_cars import ElectricCar
from app.models.electric_scooter import ElectricScooter
from app.Services.fleet_service import FleetService
import pytest

@pytest.fixture
def fleet_service():
    return FleetService()


class TestFleetService:
    def test_add_new_hub(self, fleet_service):
        hub_name = "Down Town"

        res = fleet_service.add_hub(hub_name)

        assert res is True
        assert hub_name in fleet_service.fleet_hub

    def test_add_duplicate_hub(self, fleet_service):
        hub_name = "Down Town"
        fleet_service.add_hub(hub_name)
        res = fleet_service.add_hub(hub_name)
        print(fleet_service.fleet_hub)
        assert res is False

    def test_add_vehicle_to_hub(self, fleet_service):
        fleet_service.add_hub("Down Town")
        vehicle = ElectricCar(101, "Tesla")

        result = fleet_service.add_vehicle_to_hub("Down Town", vehicle)
        assert result is True
        assert vehicle in fleet_service.fleet_hub["Down Town"].vehicles

    def test_vehicle_equality(self):
        vehicle1= ElectricCar(101, "Tesla")
        vehicle2 = ElectricCar(101, "BYD")

        assert vehicle1 == vehicle2

    def test_vehicle_in_equality(self):
        vehicle1= ElectricCar(101, "Tesla")
        vehicle2 = ElectricCar(102, "BYD")

        assert vehicle1 != vehicle2

    def test_add_duplicate_vehicle(self, fleet_service):
        fleet_service.add_hub("Airport")

        vehicle1 = ElectricCar(101, "Tesla")
        vehicle2 = ElectricCar(101, "BYD")

        fleet_service.add_vehicle_to_hub("Airport", vehicle1)
        result = fleet_service.add_vehicle_to_hub("Airport", vehicle2)

        assert result is False