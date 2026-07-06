import pytest

from app.Services.fleet_service import FleetService
from app.models.electric_cars import ElectricCar
from app.models.electric_scooter import ElectricScooter


@pytest.fixture
def fleet_service():
    return FleetService()


class TestFleetAnalytics:

    def test_available_vehicle_count(self, fleet_service):
        fleet_service.add_hub("Airport")
        car = ElectricCar(101, "Tesla")
        car.status = "Available"

        fleet_service.add_vehicle_to_hub("Airport", car)
        analytics = fleet_service.fleet_analytics()

        assert analytics["Available"] == 1
        assert analytics["On Trip"] == 0
        assert analytics["Under Maintenance"] == 0


    def test_on_trip_vehicle_count(self, fleet_service):
        fleet_service.add_hub("Airport")
        scooter = ElectricScooter(201, "Ola")
        scooter.status = "On Trip"

        fleet_service.add_vehicle_to_hub("Airport", scooter)
        analytics = fleet_service.fleet_analytics()
        assert analytics["Available"] == 0
        assert analytics["On Trip"] == 1
        assert analytics["Under Maintenance"] == 0


    def test_under_maintenance_vehicle_count(self, fleet_service):
        fleet_service.add_hub("Airport")

        car = ElectricCar(301, "BYD")
        car.status = "Under Maintenance"

        fleet_service.add_vehicle_to_hub("Airport", car)
        analytics = fleet_service.fleet_analytics()
        assert analytics["Available"] == 0
        assert analytics["On Trip"] == 0
        assert analytics["Under Maintenance"] == 1


    def test_multiple_vehicle_status_count(self, fleet_service):
        fleet_service.add_hub("Airport")
        fleet_service.add_hub("Downtown")

        car1 = ElectricCar(101, "Tesla")
        car2 = ElectricCar(102, "BYD")
        scooter1 = ElectricScooter(201, "Ola")
        scooter2 = ElectricScooter(202, "Ather")

        car1.status = "Available"
        car2.status = "Available"
        scooter1.status = "On Trip"
        scooter2.status = "Under Maintenance"

        fleet_service.add_vehicle_to_hub("Airport", car1)
        fleet_service.add_vehicle_to_hub("Airport", scooter1)
        fleet_service.add_vehicle_to_hub("Downtown", car2)
        fleet_service.add_vehicle_to_hub("Downtown", scooter2)
        analytics = fleet_service.fleet_analytics()

        assert analytics["Available"] == 2
        assert analytics["On Trip"] == 1
        assert analytics["Under Maintenance"] == 1


    def test_empty_fleet_analytics(self, fleet_service):
        analytics = fleet_service.fleet_analytics()
        assert analytics["Available"] == 0
        assert analytics["On Trip"] == 0
        assert analytics["Under Maintenance"] == 0