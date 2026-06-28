from app.models.vehicle import Vehicle

class ElectricScooter(Vehicle):
    def __init__(self, vehicle_id, model, max_speed_limit = 120):
        super().__init__(vehicle_id, model)
        self.max_speed_limit = max_speed_limit

