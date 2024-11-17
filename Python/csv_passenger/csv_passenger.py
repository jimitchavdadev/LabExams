import csv

class Train:
    def __init__(self, train_id, train_name, source_station, destination_station, total_seats, available_seats, fare):
        self.train_id = train_id
        self.train_name = train_name
        self.source_station = source_station
        self.destination_station = destination_station
        self.total_seats = total_seats
        self.available_seats = available_seats
        self.fare = fare

    def book_tickets(self, num_tickets):
        if num_tickets <= self.available_seats:
            self.available_seats -= num_tickets
            return self.fare * num_tickets
        else:
            return None

    def __str__(self):
        return f"{self.train_name} ({self.train_id}): {self.available_seats} seats available"


class Passenger:
    def __init__(self, train_id, name, num_tickets):
        self.train_id = train_id
        self.name = name
        self.num_tickets = num_tickets


def load_trains(filename):
    trains = {}
    try:
        with open(filename, 'r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                try:
                    train = Train(
                        row['Train ID'], row['Train Name'], row['Source Station'], row['Destination Station'],
                        int(row['Total Seats']), int(row['Available Seats']), int(row['Total fare'])
                    )
                    trains[train.train_id] = train
                except (ValueError, KeyError) as e:
                    print(f"Error processing train data: {e}")
    except FileNotFoundError:
        print(f"Error: File {filename} not found.")
    return trains


def load_passengers(filename):
    passengers = []
    try:
        with open(filename, 'r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                try:
                    passenger = Passenger(row['Train ID'], row['Name'], int(row['Number of Tickets']))
                    passengers.append(passenger)
                except (ValueError, KeyError) as e:
                    print(f"Error processing passenger data: {e}")
    except FileNotFoundError:
        print(f"Error: File {filename} not found.")
    return passengers


def generate_report(trains, filename="train_report.txt"):
    try:
        with open(filename, 'w') as file:
            file.write("Report 1: Train Details\n")
            file.write("Train ID | Train Name | Source | Destination | Total Seats | Available Seats\n")
            for train in trains.values():
                file.write(
                    f"{train.train_id} | {train.train_name} | {train.source_station} | {train.destination_station} | {train.total_seats} | {train.available_seats}\n"
                )

            file.write("\nReport 2: Revenue Earned from Each Train\n")
            for train in trains.values():
                revenue = (train.total_seats - train.available_seats) * train.fare
                file.write(f"{train.train_name} ({train.train_id}): Total Revenue = {revenue}\n")
        print(f"Report generated and saved to {filename}.")
    except IOError as e:
        print(f"Error writing to report file: {e}")


def main():
    trains = load_trains("trains.csv")
    passengers = load_passengers("passengers.csv")

    for passenger in passengers:
        if passenger.train_id in trains:
            train = trains[passenger.train_id]
            total_fare = train.book_tickets(passenger.num_tickets)
            if total_fare is not None:
                print(f"Booking confirmed for {passenger.name} on {train.train_name}. Total fare: {total_fare}")
            else:
                print(f"Error: Not enough seats available for {passenger.name} on {train.train_name}.")
        else:
            print(f"Error: Invalid Train ID {passenger.train_id} for passenger {passenger.name}.")

    generate_report(trains)


if __name__ == "__main__":
    main()
