from Berles import Berles
from datetime import date

class Autokolcsonzo:
    def __init__(self, name):
        self._name ="Hova Mész Autókölcsönző"
        self._cars = []
        self._berles = Berles()

    @property
    def name(self):
        return self._name

    @property
    def cars(self):
        return self._cars

    def add_car(self, car):
        self._cars.append(car)

    def get_available_cars(self, rental_date):
        available = []
        for car in self._cars:
            if not self._berles.is_rented(car.plate, rental_date):
                available.append(car)
        return available

    def get_busy_cars(self, rental_date):
        busy = []
        for car in self._cars:
            if self._berles.is_rented(car.plate, rental_date):
                busy.append(car)
        return busy

    def rent_by_plate(self, plate, rental_date):
        self._berles.rent_by_plate(plate, rental_date)

    def unrent_by_plate(self, plate, rental_date):
        self._berles.unrent_by_plate(plate, rental_date)

    @property
    def rentals(self):
        return self._berles.rentals
