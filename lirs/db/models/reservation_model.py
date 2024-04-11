class Reservation:

    def __init__(self, room_type, customer_id, accommodation_days, cost, checkout):
        self.room_type = room_type
        self.customer_id = customer_id
        self.accommodation_days = accommodation_days
        self.cost = cost
        self.checkout = checkout

    def __init__(self, id: int, room_type, customer_id, accommodation_days, cost, checkout):
        self.id = id  
        self.room_type = room_type
        self.customer_id = customer_id
        self.accommodation_days = accommodation_days
        self.cost = cost
        self.checkout = checkout