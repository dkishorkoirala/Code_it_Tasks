class FlightBooking:
    total_bookings = 0

    def __init__(self, passenger_name, flight_no, destination):
        self.passenger_name = passenger_name
        self.flight_no = flight_no
        self.destination = destination
        FlightBooking.total_bookings += 1

    def display(self):
        print(f"Passenger Name: {self.passenger_name}")
        print(f"Flight No: {self.flight_no}")
        print(f"Destination: {self.destination}")

    @classmethod
    def total_no(cls):
        print(f"Total Bookings: {cls.total_bookings}")


f1 = FlightBooking("John", 101, "New York")
f2 = FlightBooking("Jane", 102, "London")


f1.display()
f2.display()

FlightBooking.total_no()
