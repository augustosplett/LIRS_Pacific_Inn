class Room:

    def __init__(self, room_type, room_price, avaliability):
        self.first_name = room_type
        self.last_name = room_price
        self.email = avaliability

    def __init__(self, id: int, room_type, room_price, avaliability):
        self.id = id
        self.first_name = room_type
        self.last_name = room_price
        self.email = avaliability