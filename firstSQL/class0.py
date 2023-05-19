
class Flight:

    counter = 1  

    def __init__(self, origin, destination, duration) -> None:
        self.id = Flight.counter
        Flight.counter += 1

        self.passengers = []
        self.origin = origin
        self.destination = destination
        self.duration = duration

    def print_info(self):
        print(f"No.{self.id} flight travel from {self.origin} to {self.destination} during {self.duration}")
        print("Having passengers:")
        for passenger in self.passengers:
            print(passenger.name, end = ' ')
    def delay(self, amount):
        self.duration += amount

    def add_passenger(self, p):
        self.passengers.append(p)
        p.flight_id = self.id


class Passenger:
    def __init__(self, name, flight_id=None) -> None:
        self.name = name
        self.flight_id = flight_id


def main():

    f1 = Flight("New York", "Paris", 540)
    f2 = Flight("Tokyo", "Seul", 480)

    Alice = Passenger("Alice")
    Bob = Passenger("Bob")

    f1.add_passenger(Alice)
    f1.add_passenger(Bob)
    f1.print_info()

if __name__ == "__main__": main()