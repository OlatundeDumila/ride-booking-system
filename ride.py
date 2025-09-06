class User:
    def __init__(self, name, user_type):
        self.name = name
        self.user_type = user_type

class Vehicle:
    def __init__(self, model, plate_number):
        self.model = model
        self.plate_number = plate_number

class Ride:
    def __init__(self, ride_id, rider, driver, vehicle, distance_km):
        self.ride_id = ride_id
        self.rider = rider
        self.driver = driver
        self.vehicle = vehicle
        self.distance_km = distance_km

    def calculate_fare(self):
        base_fare = 500  # Base fare in Naira
        per_km_rate = 100  # Rate per kilometer
        return base_fare + (self.distance_km * per_km_rate)

    def start_ride(self):
        self.status = "in progress"
        print(f"🚗 Ride started for {self.rider.name} with driver {self.driver.name} in {self.vehicle.model} ({self.vehicle.plate_number})")

    def end_ride(self):
        self.status = "completed"
        fare = self.calculate_fare()
        print(f"✅ Ride completed for {self.rider.name}. Total fare: ₦{fare}")

# --- Test the system ---
if __name__ == "__main__":
    rider = User("Olatunde", "rider")
    driver = User("Chinedu", "driver")
    vehicle = Vehicle("Toyota Corolla", "LAG123XY")
    ride = Ride(rider, driver, vehicle, distance_km=12)

    ride.start_ride()
    ride.end_ride()