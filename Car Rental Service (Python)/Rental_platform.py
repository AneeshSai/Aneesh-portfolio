# Online Rental car company platform
from datetime import datetime
# Rental service's local database

class RentalService:
    rental_modes = ["hourly", "daily", "weekly"] # creating an array of rental modes
    
    # creating an object of mode wise payment to be used in the final calculation
    rental_prices = { 
        "hourly": 10,
        "daily": 100,
        "weekly": 500
    }

    def __init__(self):
        self.__available_cars_count = 30 # storing as a private variable for security concerns

    # Method to get the available cars in the database
    def get_available_cars_count(self):
        return self.__available_cars_count
    
    # Method to update the available cars in the database
    def set_available_cars_count(self, requested_cars):
        self.__available_cars_count-=requested_cars

    # Regular method to return the price associated with a rental mode
    def get_rental_prices(self, rental_mode):
        return self.rental_prices[rental_mode]
    
rental_service = RentalService()
rental_service.get_available_cars_count()

# Method to check the availability
def check_availability(requested_cars):
    return requested_cars <= rental_service.get_available_cars_count()
class Customer:
    def __init__(self):
        pass

    def initiate_car_booking(self):
            requested_rental_mode = input("Please enter the mode of time you want to rent the car for: hourly/daily/weekly:: ")
            self.requested_rental_mode = requested_rental_mode

            if requested_rental_mode.lower() in rental_service.rental_modes:
                self.get_requested_car_details()
                rental_service.set_available_cars_count(self.requested_car_count)
                self.store_customer_booking_time()
                self.print_booking_details()
            
            else:
                print('Invalid input, please enter hourly/daily/weekly')
                self.initiate_car_booking()

    def get_requested_car_details(self):
        requested_car_count = int(input('How many cars would you need?'))

        if check_availability(requested_car_count):
            print('Cars are available')
            self.requested_car_count = requested_car_count

        elif rental_service.get_available_cars_count() == 0:
            print("No cars are available at this time, please try again later")

        else:
            print('Requested number of cars are unavailable, Current available count:', rental_service.get_available_cars_count())
            self.get_requested_car_details()

    def store_customer_booking_time(self):
        self.booking_time = datetime.now()
        print('Customer booking completed at:', self.booking_time)

    def get_booking_details(self):
        if self.requested_car_count == 0:
            print('No booking details found')
        else:
            print("Booking details!!")
            print("Rental mode chosen:", self.requested_rental_mode)
            print("Number of cars booked:", self.requested_car_count)
            print("Booking date and time", self.booking_time)

    def print_booking_details(self):
        print("")
        print("----------------------")
        self.get_booking_details()

    def initiate_car_return(self):
        if self.requested_car_count > 0:
            #Resetting the rental service database
            rental_service.set_available_cars_count(self.requested_car_count * -1)
            print("Available cars count has been refreshed to", rental_service.get_available_cars_count(), "after the return of cars rented")

            time_taken = (datetime(2024, 12, 12, 12, 12, 12) - self.booking_time).total_seconds()
            #time_taken = (datetime.now() - self.booking_time).total_seconds() # calculation of total time taken by the car

            hours = int(time_taken/3600)
            days = int(hours/24)
            weeks = int(days/7)

            rem_days = days % 7 # Removing days getting covered under weeks calculation
            rem_hours = hours % 24 # Removing hours getting covered under days and weeks calculation

            # Calculation of price per car based on the rental mode chose
            if self.requested_rental_mode == "hourly":
                total_price = hours * rental_service.get_rental_prices("hourly")

            elif self.requested_rental_mode == "daily":
                if rem_hours > 0:
                    total_price = (days + 1) * rental_service.get_rental_prices("daily")
                else:
                    total_price = days * rental_service.get_rental_prices("daily")
            
            else:
                if rem_days > 0:
                    total_price = (weeks + 1) * rental_service.get_rental_prices("weekly")
                else:
                    total_price = weeks * rental_service.get_rental_prices("weekly")
            
            total_price *= self.requested_car_count # price for overall cars rented

            # resetting the customer information
            self.requested_car_count = 0
            self.requested_rental_mode = ''
            self.booking_time = ''

            print("")
            print("------------------------")
            print("Final bill!!")
            print("Cars were rented for a total period of", weeks, "weeks", rem_days, "days and", rem_hours, "hours")
            print("Total amount to be paid", total_price, "units")
        else:
            print("No cars pending to be returned by this customer")

customer1 = Customer() # creating a customer

# Initiating a car booking
customer1.initiate_car_booking()
print('--------------------------------')

# Function to fetch the car details after the booking
rental_service.get_available_cars_count()
print('--------------------------------')

# function to get the booking details
customer1.get_booking_details()
print('--------------------------------')

#Function to return the car
customer1.initiate_car_return()
print('--------------------------------')

## Details After returning the cars
#To get the refreshed number of cars
rental_service.get_available_cars_count()
print('--------------------------------')

#To cross check if booking still exists
customer1.get_booking_details()
print('--------------------------------')

#To try re-returning the car
customer1.initiate_car_return()