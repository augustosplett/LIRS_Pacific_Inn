class Reservation:

    def __init__(self, room_id: int, customer_id: int, accommodation_days: int, cost:float, checkout:int, id: int = None):
        self.id = id  
        self.room_id = room_id
        self.customer_id = customer_id
        self.accommodation_days = accommodation_days
        self.cost = cost
        self.checkout = checkout

