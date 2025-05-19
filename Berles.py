class Berles:
    def __init__(self):
        self._rentals = []

    def rent_by_plate(self, plate, rental_date):
        self._rentals.append((plate, rental_date))

    def unrent_by_plate(self, plate, rental_date):
        self._rentals = [(p, d) for (p, d) in self._rentals if not (p == plate and d == rental_date)]

    def is_rented(self, plate, rental_date):
        return (plate, rental_date) in self._rentals

    @property
    def rentals(self):
        return self._rentals
