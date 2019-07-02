import random


class Flight:                                       # flight class
    def __init__(self, flight_name, flight_no):                    # constructor
        self.flight_name = flight_name
        self.flight_no = flight_no

    def display(self):                       # display flight details
        print('airlines: ', self.flight_name)
        print('flight number: ', self.flight_no)


class Employee:                                     # employee class
    def __init__(self, e_id, e_name, e_age, e_gender):          # constructor
        self.e_name = e_name
        self.e_age = e_age
        self.__e_id = e_id                      # private data member
        self.e_gender = e_gender

    def emp_display(self):                          # display employee details
        print("name of employee: ", self.e_name)
        print('employee id: ', self.__e_id)       # retrieving private data member
        print('employee age: ', self.e_age)
        print('employee gender: ', self.e_gender)


class Passenger:                                    # Passenger class
    def __init__(self):                             # constructor
        Passenger.__passport_number = input("enter the passport number : ")     # private data member
        Passenger.name = input('enter the name : ')
        Passenger.age = input('enter the  age ')
        Passenger.gender = input('enter the gender: ')
        Passenger.class_type = input('select type of class: ')


class Baggage():                                    # baggage class
    cabin_bag = 1
    bag_fare = 0

    def __init__(self, checked_bags):               # calculate cost if passenger has more than 2 checked bags
        self.checked_bags = checked_bags
        if checked_bags > 2:
            for item in checked_bags:
                self.bag_fare += 100
        print("number of checked bags allowed:", checked_bags, "bag fare:", self.bag_fare)


class Fare(Baggage):                                # fare class which is the sub class of baggage class
    counter = 150                                   # fixed cost if ticket is purchased at counter
    online = random.randint(100, 200)               # if purchased through online, cost is generated from a random function
    total_fare = 0

    def __init__(self):                             # constructor
        super().__init__(2)                         # super call to baggage (parent class)
        x = input('buy ticket through online or counter:')
        if x == 'online':
            Fare.total_fare = self.online + self.bag_fare
        elif x == 'counter':
            Fare.total_fare = self.counter + self.bag_fare
        else:
            x = input('enter correct transaction type:')
        print("Total Fare before class type:", Fare.total_fare)


class Ticket(Passenger, Fare):                                      # multiple inheritance
    def __init__(self):                                             # constructor
        print("Passenger name:", Passenger.name)                     # accessing the passenger (parent) class variable
        if Passenger.class_type == "business":                      # cost varies with business and economy class
            Fare.total_fare += 100
        else:
            pass
        print("Passenger class type:", Passenger.class_type)
        print("Total fare:", Fare.total_fare)                        # total fare is displayed


f1 = Flight('Etihad', 1000)                                            # Instance of Flight class
f1.display()

e1 = Employee('E1', 'dhruv', 29, 'M')                          # instance of Employee class
e1.emp_display()

p1 = Passenger()                                                    # instance of passenger class

fare1 = Fare()                                                        # instance of fare class

t = Ticket()                                                         # instance of ticket class