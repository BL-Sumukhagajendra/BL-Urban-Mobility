from app.Services.fleet_service import FleetService
from app.models.electric_cars import ElectricCar
from app.models.electric_scooter import ElectricScooter
import pytest

@pytest.fixture
def fleet_service():
    fleet = FleetService()
    return fleet

class TestSearchFunctionality:
        def test_search_vehicle_by_existing_hub(self, fleet_service):

            fleet_service.add_hub("Airport")

            vehicle1 = ElectricCar(101, "Tesla")
            vehicle2 = ElectricScooter(102, "Ather")

            fleet_service.add_vehicle_to_hub("Airport", vehicle1)
            fleet_service.add_vehicle_to_hub("Airport", vehicle2)

            vehicles = fleet_service.search_by_hub("Airport")

            assert len(vehicles) == 2
            assert vehicle1 in vehicles
            assert vehicle2 in vehicles

        def test_search_vehicle_by_invalid_hub(self, fleet_service):
            vehicles = fleet_service.search_by_hub("Downtown")

            assert vehicles == []

        def test_search_high_battery_vehicle(self, fleet_service):
             
            fleet_service.add_hub("Airport")

            vehicle1 = ElectricCar(101, "Tesla")
            vehicle2 = ElectricScooter(102, "Ather")

            vehicle1.set_battery_percentage = 90
            vehicle2.set_battery_percentage = 60

            fleet_service.add_vehicle_to_hub("Airport", vehicle1)
            fleet_service.add_vehicle_to_hub("Airport", vehicle2)

            vehicles = fleet_service.search_high_battery_vehicles()

            assert len(vehicles) == 1
            assert vehicle1 in vehicles
            assert vehicle2 not in vehicles

