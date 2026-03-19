class Restaurant:
    """a simple restaurant class"""
    def __init__(self,restaurant_name,cuisine_type):
        """"store two attributes"""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.customers = 0
        self.served = 0
    def describe_restaurant(self):
        """print two pieces of info"""
        print(f"Welcome to The {self.restaurant_name}!")
        print(f"We serve {self.cuisine_type} ")
    def open_restaurant(self):
        """prints indicating the restaurant is open"""
        print(f"{self.restaurant_name} is open!\n")
    def restaurant(self):
        """read number"""
        print(f"This restaurant has recieved {self.customers}")

    def updated_restaurant(self,number_recieved):
        """print number of served customers"""
        if number_recieved >= self.customers:           
            self.customers = number_recieved
        else:
            print("Can't change the numbers")
    def set_numbers_served(self):
        """set number of coustomers"""
        print(f"We have served {self.served}")

    def updated_served(self,numbers_served):
        """change numbers""" 
        self.served += numbers_served
           

   
your_order = Restaurant('Kempinski','Bobber Tea')
your_order.describe_restaurant()
your_order.open_restaurant()
your_order.restaurant()

your_order.updated_served(200)
your_order.restaurant()
