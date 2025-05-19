from Auto import Auto

class Szemelyauto(Auto):
    def __init__(self, plate, car_type, rental_fee):
        super().__init__(plate, car_type , rental_fee)
        self._car_type = car_type

        @property
        def car_type(self):
            return self._car_type

