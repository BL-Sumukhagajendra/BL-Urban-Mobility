from app.models.fleet_hub import FleetHub
from app.models.electric_scooter import ElectricScooter
from app.models.electric_cars import ElectricCar

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
    
    
    def search_by_hub(self, hub_name: str):

        if hub_name not in self.fleet_hub:
            return []
        return self.fleet_hub[hub_name].vehicles
    
    def search_high_battery_vehicles(self):

        vehicles = []

        for hub in self.fleet_hub.values():
            vehicles.extend(hub.vehicles)

        return list(
            filter(
                lambda vehicle: vehicle.battery_percentage > 80,
                vehicles
            )
        )

    def categorize_vehicles(self):

        categorized = {
            "ElectricCar": [],
            "ElectricScooter": []
        }

        for hub in self.fleet_hub.values():

            for vehicle in hub.vehicles:

                if isinstance(vehicle, ElectricCar):
                    categorized["ElectricCar"].append(vehicle)

                elif isinstance(vehicle, ElectricScooter):
                    categorized["ElectricScooter"].append(vehicle)

        return categorized
    
    def fleet_analytics(self):

        analytics = {
            "Available": 0,
            "On Trip": 0,
            "Under Maintenance": 0
        }

        for hub in self.fleet_hub.values():

            for vehicle in hub.vehicles:

                analytics[vehicle.status] += 1

        return analytics
