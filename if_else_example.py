# Parking Ticket System using Class

class ParkingTicket:
    
    def __init__(self, ticket_type, hours):
        self.ticket_type = ticket_type.lower()
        self.hours = hours

    def calculate_charge(self):
        
        if self.ticket_type == "basic":
            if self.hours <= 2:
                return self.hours * 10
            else:
                return (2 * 10) + (self.hours - 2) * 15

        elif self.ticket_type == "premium":
            if self.hours <= 3:
                return self.hours * 20
            else:
                return (3 * 20) + (self.hours - 3) * 30

        elif self.ticket_type == "vip":
            if self.hours <= 5:
                return self.hours * 50
            else:
                return (5 * 50) + (self.hours - 5) * 70

        else:
            return None


# Taking user input
ticket_type = input("Enter ticket type (basic / premium / vip): ")
hours = int(input("Enter parking hours: "))

# Create object
ticket = ParkingTicket(ticket_type, hours)

# Calculate and print result
charge = ticket.calculate_charge()

if charge is None:
    print("Invalid ticket type!")
else:
    print("Total Parking Charge: ₹", charge)
