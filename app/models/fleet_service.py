from app.models.fleet_hub import FleetHub
from app.models.vehicle import Vehicle

class FleetService:
    def __init__(self):
        self.fleet_hub = {
            # "Airport": []
        }

    def add_hub(self, hub_name: set):
        if hub_name in self.fleet_hub:
            return False
        
        self.fleet_hub[hub_name] = FleetHub(hub_name)
        return True
    
    def add_vehicle(self, hub_name: str, vehicle: Vehicle):
        if hub_name not in self.fleet_hub:
            return False
        hub = self.fleet_hub[hub_name]
        hub.vehicles.append(vehicle)

        return True
        


