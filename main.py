import datetime
from unicodedata import name
# method
# attributes
class Student:
    group = "IP-11"
    def __init__(self, first_name: str = "", last_name: str = "") -> None:
        self.first_name = first_name    # public
        self.last_name = last_name      # public
        self.__name = "hidden"          # private
        self._another = "another"       # protected
    def print_name(self):
        self.full_name = "Mr/Mrs. " + self.first_name + " " + self.last_name
        print(self.full_name)
    @staticmethod
    def pass_exam() -> None:
        print(Student.group)

class Fish:
    def __init__(
                self, name:str = "oseledets",
                price_in_uah_per_kilo:float = 11.2,
                catch_date:datetime.date = datetime.date.fromisoformat("2022-01-21"),
                origin:str = "Norway",
                body_only:bool = True,
                weight:float = 100
    ) -> None:
        self.name = name
        self.price_in_uah_per_kilo = price_in_uah_per_kilo
        self.catch_date = catch_date
        self.origin = origin
        self.body_only = body_only
        self.weight = weight

    def __repr__(self) -> str:
        return " ".join((self.name,str(self.price_in_uah_per_kilo),str(self.catch_date),
                    self.origin,"Body only?:",str(self.body_only)+" ",str(self.weight)))

class FishShop:
    available_fish = list()

    def add_fish(self, fish: Fish) -> None:
        self.available_fish.append(fish)

    def get_fish_names_sorted_by_price(self) -> [Fish]:
        return list(sorted(
            self.available_fish,
            key=lambda fish: fish.price_in_uah_per_kilo
            ))

    def sell_fish(self, fish_name: str, weight: float) -> float:
        price:float = 0.0
        for fish in self.available_fish:
            if fish.name == fish_name:
                if fish.weight <= weight:
                    weight = weight - fish.weight
                    price += fish.weight* fish.price_in_uah_per_kilo
                    self.available_fish.remove(fish)
                else:
                    fish.weight = fish.weight - weight
                    price += weight * fish.price_in_uah_per_kilo
                    break
        return price

    def cast_out_old_fish(self, is_that_after_days: int = 30) -> [Fish]:
        out = list(self.available_fish)
        min_good_date = datetime.date.today() - datetime.timedelta(days = is_that_after_days)
        self.available_fish = list(filter(lambda fish: fish.catch_date >= min_good_date, self.available_fish))
        return out.remove([fish for fish in self.available_fish])

class Seller:
    def __init__(self,full_name:str = "oleh petrovych", id: int, money:float, place_of_work:Place, place_of_residence: Place):
        pass
    def pay_taxes(self, tax_premium_percentage: int = 30) -> None:
        pass
    def available_goods(self) -> []:
        pass
    def order_goods(self, goods:[Goods]) -> None:
        pass
    def pay_employee(self, employee: str, money:int) -> None:
        pass
    def hire_employee(self, employee: Employee) -> None:
        pass
    def fire_employee(self, employee: str) -> Employee:
        pass
    def make_revision(self) -> None:
        pass
    def cast_out_old_goods(self) -> [Goods]:
        pass
class Buyer:
    def __init__(self, full_name:str = "oleh petrovych", id: int, money:float, place_of_residence: Place, preferences: [str]) ->None:
        pass
    def buy(goods:[Goods]) -> None:
        pass
    

bazar = FishShop()
bazar.add_fish(Fish(
                    "oleh", 500.3, datetime.date.fromisoformat("2006-02-05"),
                    "Somewhere near the city", False, 15.3))
bazar.add_fish(Fish(
                    "petrovych", 10.3, datetime.date.fromisoformat("2021-06-01"),
                    "Chornobyl", True, 20
                    ))
bazar.add_fish(Fish(
                    "Dog", 25.5, datetime.date.fromisoformat("2014-08-22"),
                    "Fukusima", False, 45
                    ))
bazar.add_fish(Fish(
                    "oleh", 500.3, datetime.date.fromisoformat("2016-08-05"),
                    "Somewhere near the city", False, 50))
print("\n".join([str(fish) for fish in bazar.get_fish_names_sorted_by_price()]))
print(str(bazar.sell_fish("oleh", 20)))
print("\n".join([str(fish) for fish in bazar.get_fish_names_sorted_by_price()]))

bazar.cast_out_old_fish(1000)
print("Casted ouit")
print("\n".join([str(fish) for fish in bazar.available_fish]))
oleh = Student("oleh", "petrovych")
oleh.print_name()
taras = Student()
taras.print_name()
