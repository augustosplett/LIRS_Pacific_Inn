class Customer:

    def __init__(self, first_name: str, last_name: str, email: str, phone_number: int, id: int = None):
        self.id = id
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.phone_number = phone_number

    def __str__(self) -> str:
        return "CUSTOMER --> ID: {}, First Name: {}, Last Name: {}, Email: {}, Phone Number: {}".format(self.id, self.first_name, self.last_name, self.email, self.phone_number)