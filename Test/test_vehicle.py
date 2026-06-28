from app.models.vehicle import Vehicle
import pytest

@pytest.fixture
def vehicle():
    return Vehicle(1, "Tesla")

class TestVehicle:
    def test_vehicle_id(self, vehicle):
        assert vehicle.vehicle_id == 1

    def test_model(self, vehicle):
        assert vehicle.model == "Tesla"

    def test_default_value_for_battery(self, vehicle):
        assert vehicle.battery_percentage == 0  

    def test_battery_percentage_setter(self, vehicle):
        vehicle.set_battery_percentage = 50
        assert vehicle.battery_percentage == 50
 
    @pytest.mark.parametrize("battery", [1, 0, 99, 100])
    def test_boundary_values_battery_percentage(self, battery,  vehicle):
        vehicle.set_battery_percentage = battery
        assert vehicle.battery_percentage == battery

    @pytest.mark.parametrize("battery", [-1, 101])
    def test_negative_boundary_values_battery_percentage(self, battery, vehicle):
        with pytest.raises(ValueError):
            vehicle.set_battery_percentage = battery

    def test_negative_battery(self, vehicle):
        with pytest.raises(ValueError):
            vehicle.set_battery_percentage = -10

    def test_default_values_for_mainatin_status(self, vehicle):
        assert vehicle.mainatin_status == "AVAILABLE"        

    def test_maintan_setter(self, vehicle):
        vehicle.set_maintain_status = "UNAVAILABLE"
        assert vehicle.mainatin_status == "UNAVAILABLE"

    def test_maintain_status_wrong_input(self, vehicle):
        with pytest.raises(ValueError):
            vehicle.set_maintain_status = "ABCD"