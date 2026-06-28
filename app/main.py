from app.models.electric_cars import ElectricCar
from app.models.electric_scooter import ElectricScooter

vehicles = [
    ElectricCar(1, "Tesla"),
    ElectricScooter(2, "Ather"),
    ElectricCar(3, "BYD"),
    ElectricScooter(4, "Ola")
]

for vehicle in vehicles:
    if isinstance(vehicle, ElectricCar):
        cost = vehicle.calculate_trip_cost(20)  # 20 km
    else:
        cost = vehicle.calculate_trip_cost(20)  # 20 minutes

    print(f"{vehicle.model}: {cost}")