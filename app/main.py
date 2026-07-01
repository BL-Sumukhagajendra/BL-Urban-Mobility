from app.models.electric_cars import ElectricCar
from app.models.electric_scooter import ElectricScooter
from app.Services.fleet_service import FleetService


# Un-necessary.
# vehicles = [
#     ElectricCar(1, "Tesla"),
#     ElectricScooter(2, "Ather"),
#     ElectricCar(3, "BYD"),
#     ElectricScooter(4, "Ola")
# ]

# for vehicle in vehicles:
#     cost = vehicle.calculate_trip_cost(20)
#     print(f"{vehicle.model}: ${cost}")


service = FleetService()


while True:

    print("------ Fleet Management ------")
    print("1. Add Hub")
    print("2. Add Vehicle")
    print("3. Display Hubs")
    print("4. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:

        hub_name = input("Enter Hub Name: ")

        if service.add_hub(hub_name):
            print("Hub added successfully.")
        else:
            print("Hub already exists.")

    elif choice == 2:

        hub_name = input("Enter Hub Name: ")

        vehicle_id = int(input("Enter Vehicle ID: "))
        model = input("Enter Vehicle Model: ")

        print("\nVehicle Types")
        print("1. Electric Car")
        print("2. Electric Scooter")

        vehicle_type = int(input("Enter your choice: "))

        if vehicle_type == 1:
            vehicle = ElectricCar(vehicle_id, model)

        elif vehicle_type == 2:
            vehicle = ElectricScooter(vehicle_id, model)

        else:
            print("Invalid Vehicle Type.")
            continue

        if service.add_vehicle_to_hub(hub_name, vehicle):
            print("Vehicle added successfully.")
        else:
            print("Hub not found.")

    elif choice == 3:

        service.display_hubs()

    elif choice == 4:

        print("Exiting Fleet Management System...")
        break

    else:
        print("Invalid Choice.")