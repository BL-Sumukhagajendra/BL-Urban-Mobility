
class FleetHub:
    def __init__(self, hub_name):
        self.hub_name = hub_name
        self.vehicles = []
    
    def add_vehicle(self, vehicle):

        duplicate_vehicle = [
            existing_vehicle
            for existing_vehicle in self.vehicles
            if existing_vehicle == vehicle
        ]

        if duplicate_vehicle:
            return False

        self.vehicles.append(vehicle)
        return True

    def __str__(self):
        output = ""

        if not self.vehicles:
            return "No vehicles are added to this hub"

        for vehicle in self.vehicles:
            output += str(f"{vehicle}\n")
        
        return output
    
