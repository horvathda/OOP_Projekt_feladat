from Auto import Auto

class Teherauto(Auto):
    def __init__(self, plate, car_type, rental_fee):
        super().__init__(plate, car_type, rental_fee)
        self._car_type = "Teherautó"

        @property
        def car_type(self):
            return self._car_type
