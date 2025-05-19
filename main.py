from Berles import Berles
from Szemelyauto import Szemelyauto
from Teherauto import Teherauto
from Autokolcsonzo import Autokolcsonzo
from datetime import date, datetime


class CarRentalSystem:
    def __init__(self):
        self._rental_service = Autokolcsonzo(name="")
        self.rents = Berles()
        self._init_data()

    def _init_data(self):
        initial_cars = [
            Szemelyauto("ABC-123", "Szemelyautó", 10000),
            Szemelyauto("ABC-456", "Szemelyautó", 12000),
            Szemelyauto("ABC-789", "Szemelyautó", 14000),
            Teherauto("DEF-123", "Teherautó", 20000),
            Teherauto("DEF-456", "Teherautó", 22000),
        ]
        for car in initial_cars:
            self._rental_service.add_car(car)

        self._rental_service.rent_by_plate("ABC-123", date(2025, 6, 5))
        self._rental_service.rent_by_plate("ABC-456", date(2025, 6, 4))
        self._rental_service.rent_by_plate("DEF-123", date(2025, 6, 5))
        self._rental_service.rent_by_plate("DEF-456", date(2025, 6, 5))
        self._rental_service.rent_by_plate("DEF-123", date(2025, 6, 6))

    def user_interact(self):
        while True:
            print(f"Üdvözöljük az {self._rental_service.name} regisztrációs felületén!")
            print("1. Autók listázása")
            print("2. Foglalások listázása")
            print("3. Autó foglalás")
            print("4. Foglalás lemondása")
            print("5. Kilépés")

            try:
                choice = int(input("Válasszon a menüpontok közül: "))
            except ValueError:
                print("Kérem csak számot adjon meg!")
                continue

            if choice == 1:
                print("Elérhető autók:")
                for car in self._rental_service.cars:
                    print(f"{car.plate} – {car.car_type}, {car.rental_fee} Ft")

            elif choice == 2:
                print("Aktuális foglalások:")
                for plate, d in self._rental_service.rentals:
                    print(f"{plate} – {d}")

            elif choice == 3:
                rental_date = self._prompt_for_date("Adja meg a foglalás dátumát (YYYY-MM-DD): ")
                available = self._rental_service.get_available_cars(rental_date)

                if not available:
                    print(f"Nincsenek szabad autók erre a napra: {rental_date}")
                    continue

                print("Szabad autók ezen a napon:")
                for car in available:
                    print(f"  {car.plate} – {car.car_type}, {car.rental_fee} Ft")

                plate = self._prompt_for_plate(available, rental_date, for_booking=True)
                self._rental_service.rent_by_plate(plate, rental_date)
                print(f"Sikeres foglalás: {plate} – {rental_date} - {car.rental_fee} Ft")

            elif choice == 4:
                rental_date = self._prompt_for_date("Adja meg a foglalás dátumát (YYYY-MM-DD): ")
                busy = self._rental_service.get_busy_cars(rental_date)

                if not busy:
                    print(f"Nincsenek foglalt autók erre a napra: {rental_date}")
                    continue

                print("Foglalt autók ezen a napon:")
                for car in busy:
                    print(f"  {car.plate} – {car.car_type}, {car.rental_fee} Ft")

                plate = self._prompt_for_plate(busy, rental_date, for_booking=False)
                self._rental_service.unrent_by_plate(plate, rental_date)
                print(f"Foglalás lemondva: {plate} – {rental_date}")

            elif choice == 5:
                print("Viszontlátásra!")
                break

            else:
                print("Hibás menüpont, próbálja újra!")

    def _prompt_for_date(self, prompt):
        while True:
            user_input = input(prompt)
            try:
                d = datetime.strptime(user_input, "%Y-%m-%d").date()
            except ValueError:
                print("Hibás formátum! Kérem YYYY-MM-DD formátumot adjon meg!")
                continue

            if d < date.today():
                print("A dátum nem lehet múltbéli!")
                continue
            return d

    def _prompt_for_plate(self, cars_list, rental_date, for_booking=True):
        action = "foglalni" if for_booking else "lemondani"
        while True:
            plate_input = input(f"Adja meg annak az autónak a rendszámát, amit {action} szeretne: ").upper()
            if any(car.plate == plate_input for car in cars_list):
                return plate_input

            in_fleet = any(car.plate == plate_input for car in self._rental_service.cars)
            if in_fleet:
                status = "foglalható" if not for_booking else "ezt a napot már" if for_booking else "már szabad"
                print(f"A {plate_input} rendszámú autó erre a napra {rental_date} {status}.")
            else:
                print(f"Nincs ilyen rendszámú autónk: {plate_input}")


CarRentalSystem().user_interact()