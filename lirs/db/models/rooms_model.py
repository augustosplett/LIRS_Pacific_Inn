class Room:

    def __init__(self, room_type:str, room_price:float, avaliability:float, id: int = None):
        self.id = id
        self.room_type = room_type
        self.room_price = room_price
        self.avaliability = avaliability

    def __str__(self) -> str:
        return "ID: {}, Room Type: {}, Room Price: {}, Avaliability: {}".format(self.id, self.room_type, self.room_price, self.avaliability)