class Address:

    def __init__(self, index, city, street, house, flat):
        self.index = index
        self.city = city
        self.street = street
        self.house = house
        self.flat = flat


    def __str__(self):
            return f"Индекс: {self.index}, город: {self.city}, улица: {self.street}, дом: {self.house}, квартира: {self.flat}"
