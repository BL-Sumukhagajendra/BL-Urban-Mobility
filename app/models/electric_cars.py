from app.models.vehicle import Vehicle

class ElectricCar(Vehicle):
    def __init__(self, vehicle_id: int, model: str, seating_capacity: int = 4):
        super().__init__(vehicle_id, model)
        self.seating_capacity = seating_capacity

    def calculate_trip_cost(self, distance: int):
        base = 5
        if distance <= 0:
            raise ValueError("Invalid Distance")
        return distance * 0.35 + base