from app.models.fleet_hub import FleetHub
from app.models.vehicle import Vehicle

class FleetService:
    def __init__(self):
        self.fleet_hub = {
            # "Airport": []
        }

    def add_hub(self, hub_name: str):
        if hub_name in self.fleet_hub:
            return False
        
        self.fleet_hub[hub_name] = FleetHub(hub_name)
        return True
    
    def add_vehicle_to_hub(self, hub_name, vehicle):

        if hub_name not in self.fleet_hub:
            return False

        hub = self.fleet_hub[hub_name]
        return hub.add_vehicle(vehicle)
    
    def display_hubs(self):
        if not len(self.fleet_hub):
            print("empty fleet. Do you want to add fleet?")
            return False
        
        for fleet, vehicles in self.fleet_hub.items():
            print(f"Fleet name: {fleet}")
            for vehicle in vehicles.vehicles:
                print(f"Vehicle id: {vehicle.vehicle_id} ")
                print(f"Vehicle Name: {vehicle.model}")
        return True
    
    