class Vehicle:
    def __init__(self, vehicle_number):
        self.vehicle_number = vehicle_number


class ParkingLot:
    def __init__(self, capacity=40) -> None:
        self.capacity = capacity
        self.level_a = {i:None for i in range(1,21)}
        self.level_b = {i:None for i in range(21,41)}

    def find_empty_spot(self):
        for spot, Vehicle in self.level_a.items():
            if Vehicle is None:
                return "A", spot
            
        for spot, Vehicle in self.level_b.items():
            if Vehicle is None:
                return "B", spot
        return None, None
    
    def park_vehicle(self, vehicle_number):
        level, spot = self.find_empty_spot()
        if level and spot:
            vehicle = Vehicle(vehicle_number)
            if level == "A":
                self.level_a[spot] = vehicle

            else:
                self.level_b[spot] = vehicle
            return {'level':level, 'spot':spot}
        else:
            return 'Parking lot is full'
        
    def find_parked_vehicle(self, vehicle_number):
        for spot, Vehicle in self.level_a.items():
            if Vehicle and Vehicle.vehicle_number == vehicle_number:
                return {'level':"A",'spot':spot}
            
        for spot, vehicle in self.level_b.items():
            if vehicle and vehicle.vehicle_number == vehicle_number:
                return {'level':"B", "spot": spot}
            
        return "Vehicle not found"
    


def main():
    parking_lot = ParkingLot()

    while True:
        print("\n1. Park a vehicle\n2. Find a parked vehicle\n3. Quit")
        choice = input("Enter your chioce : ")
        if choice =='1':
            vehicle_number = input("\nEnter vehicle number :")
            result = parking_lot.park_vehicle(vehicle_number)
            print(result)
        elif choice == '2':
            vehicle_number = input("\nEnter vehicle number :")
            result = parking_lot.find_parked_vehicle(vehicle_number)
            print(result)
        elif choice == "3":
            break
        else:
            print("Invalid Choice !")

if __name__ == "__main__":
    main()
        