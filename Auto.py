#Auto.py

from abc import ABC

class Auto(ABC):
    def __init__(self, plate,car_type, rental_fee):
        self._plate = plate
        self._car_type = car_type
        self._rental_fee = rental_fee


    @property
    def plate(self):
        return self._plate

    @property
    def car_type(self):
        return self._car_type

    @property
    def rental_fee(self):
        return self._rental_fee



