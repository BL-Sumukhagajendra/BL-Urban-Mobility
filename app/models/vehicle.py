from abc import ABC, abstractmethod

class Vehicle(ABC):
    def __init__(self, vehicle_id: int, model: str):
        self.vehicle_id = vehicle_id
        self.model = model
        self.__battery_percentage = 0
        self.__maitainence_status = "AVAILABLE"

    @property
    def battery_percentage(self):
        return self.__battery_percentage
    
    @battery_percentage.setter
    def set_battery_percentage(self, battery):
        if battery < 0 or battery > 100:
            raise ValueError("Battery shpuld be between 0 to 100 ")
        
        self.__battery_percentage = battery

    @property
    def mainatin_status(self):
        return self.__maitainence_status
    
    @mainatin_status.setter
    def set_maintain_status(self, status):
        if status not in ["AVAILABLE", "UNAVAILABLE"]:
            raise ValueError("Invalid status")

        self.__maitainence_status = status

    def __eq__(self, other):
        if not isinstance(other, Vehicle):
            raise ValueError("Object mismatch")
        
        return self.vehicle_id == other.vehicle_id
    
    def __str__(self):
        id = self.vehicle_id
        model = self.model
        return "Vehicle Id: " + id + "\nVehicle Name: " + model

    @abstractmethod
    def calculate_trip_cost(distance):
        pass