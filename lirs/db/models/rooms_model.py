class Room:

    def __init__(self, room_type:str, room_price:float, avaliability:int, id: int = None):
        self.id = id
        self.room_type = room_type
        self.room_price = room_price
        self.avaliability = avaliability

    def __str__(self) -> str:
        return f"ID: {self.id}\tType: {self.get_room_type()}\tPrice per night: {self.room_price} $\tAvaliability: {self.avaliability}"   
    
    def get_room_type(self)->str:
        type_code = self.room_type
        if type_code == 'S': return 'Standard Room'
        if type_code == 'P': return 'Premium Room'
        if type_code == 'O': return 'Ocean View Room'
        if type_code == 'E': return 'Economy Room'