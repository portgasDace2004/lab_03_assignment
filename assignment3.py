class Flight:
    def __init__(self, flight_id, source, destination, price):
        self.flight_id = flight_id
        self.source = source
        self.destination = destination
        self.price = price

class FlightTable:
    def __init__(self):
        self.flights = []
    
    def add_flight(self, flight):
        self.flights.append(flight)
    
    def search_by_id(self, flight_id):
        for flight in self.flights:
            if flight.flight_id == flight_id:
                return flight
        return None
    
    def search_by_source(self, source):
        results = []
        for flight in self.flights:
            if flight.source == source:
                results.append(flight)
        return results
    
    def search_destination(self, destination):
        results = []
        for flight in self.flights:
            if flight.destination == destination:
                results.append(flight)
        return results


flight_table = FlightTable()
flight_table.add_flight(Flight("AI161E90", "BLR", "BOM", 5600))
flight_table.add_flight(Flight("BR161F91", "BOM", "BBI", 6750))
flight_table.add_flight(Flight("AI161F99", "BBI", "BLR", 8210))
flight_table.add_flight(Flight("VS171E20", "JLR", "BBI", 5500))
flight_table.add_flight(Flight("AS171G30", "HYD", "JLR", 4400))
flight_table.add_flight(Flight("AI131F49", "HYD", "BOM", 3499))

while True:
    user_input = input("\nEnter '1' to search by Flight ID,\n'2' to search by source city, or \n'3' to search by destination city:\n '4': exit ")
    if user_input == '1':
        flight_id = input("Enter Flight ID: ")
        flight = flight_table.search_by_id(flight_id)
        if flight:
            print(f"Flight ID: {flight.flight_id}, From: {flight.source}, To: {flight.destination}, Price: {flight.price}")
        else:
            print("Flight not found.")
    elif user_input == '2':
        source = input("Enter source city: ")
        flights = flight_table.search_by_source(source)
        if flights:
            # print("Flights from", source)
            for flight in flights:
                print(f"Flight ID: {flight.flight_id},From: {flight.source} ,To: {flight.destination}, Price: {flight.price}")
        else:
            print("No flights from the given source.")
    elif user_input == '3':
        destination = input("Enter destination city: ")
        flights = flight_table.search_destination(destination)
        if flights:
            # print("Flights to", destination)
            for flight in flights:
                print(f"Flight ID: {flight.flight_id}, From: {flight.source},To: {flight.destination} ,Price: {flight.price}")
        else:
            print("No flights to the given destination.")
    elif user_input == '4':
        break
    else:
        print("Invalid input.")
