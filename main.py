from ast import Dict
from datetime import date
from typing import List, Mapping, Tuple, TypedDict, Union
from unicodedata import name

class Volume:
    width: int
    height: int
    depth: int

    def __init__(self, width: int, height: int, depth: int) -> None:
        self.height = height
        self.width = width
        self.depth = depth

    def calculate_volume(self) -> int:
        return self.height * self.width * self.depth


class FishInfo:
    name: str
    origin: str
    catch_date: date
    due_date: date

    def __init__(self, name:str, origin: str, catch_date: date, due_date:date) -> None:
        self.name = name
        self.origin = origin
        self.catch_date = catch_date
        self.due_date = due_date

class Fish(FishInfo):
    age_in_month: int
    weight: float

    def __init__(
        self, name:str, origin: str, catch_date: date, due_date:date, 
        age_in_month: int, weight: float
    ) -> None:
        super().__init__(name, origin, catch_date, due_date)
        self.age_in_month = age_in_month
        self.weight = weight

class FishBox:
    def __init__(self, fish_type: FishInfo, package_date: date, volume: Volume) -> None:
        self.fish_info = fish_type
        self.package_date = package_date
        self.volume = volume

    fish_info: FishInfo
    package_date: date
    volume: Volume

class FishShop:
    frozen_fish: dict
    fresh_fish: dict

    def add_fish(self, fish: Fish, weight: float, price_per_kilo: float) -> None:
        elem_info = (fish, weight, price_per_kilo)
        if self.fresh_fish.get(elem_info[0].name) == None:
            self.fresh_fish[elem_info[0].name] = [elem_info]
        else:
            self.fresh_fish[elem_info[0].name].append(elem_info)

    def add_fish(self, fish: FishBox, weight: float, price_per_kilo: float) -> None:
        elem_info = (fish, weight, price_per_kilo)
        if self.frozen_fish.get(elem_info[0].fish_info.name) == None:
            self.frozen_fish[elem_info[0].fish_info.name] = [elem_info]
        else:
            self.frozen_fish[elem_info[0].fish_info.name].append(elem_info)
    
    def sell_fresh_fish(self, fish_name: str, weight: float) -> Tuple[FishInfo, float, float]:
        available_fish = sorted(self.fresh_fish.get(fish_name), key = lambda fish: fish[1])
        for fish_and_weight in available_fish:
            if fish_and_weight[1] >= weight:
                return (
                    FishInfo(fish_and_weight[0]), #Fish 
                    fish_and_weight[1], #weight
                    fish_and_weight[1] * fish_and_weight[2] #sum
                    )
        return None

    def sell_frozen_fish(self, fish_name: str, weight: float) -> Tuple[FishInfo, float, float]:
        available_fish = self.frozen_fish.get(fish_name)
        out = (None, 0.0, 0.0)
        for fish_and_weight in available_fish:
            if weight <= fish_and_weight[1]:
                fish_and_weight[1] -= weight
                if out[0] == None:
                    out[0] = fish_and_weight[0].fish_info
                out[1] += weight
                out[2] += weight * fish_and_weight[2]
                return out
            else:
                weight -= fish_and_weight[1]
                if out[0] == None:
                    out[0] = fish_and_weight[0].fish_info
                out[1] += fish_and_weight[1]
                out[2] += fish_and_weight[1] * fish_and_weight[2]
        if out[0] == None: 
            return None 
        return out
    
    def get_fish_sorted_by_price(self) -> List[Tuple[FishInfo, bool, float, float]]:
        out = []
        for fish_elem in self.fresh_fish: 
            out.append((FishInfo(fish_elem[0]), True, fish_elem[1], fish_elem[2]))
        for fish_elem in self.frozen_fish: 
            out.append((FishInfo(fish_elem[0]), False, fish_elem[1], fish_elem[2]))
        return list(sorted(out, key = lambda fish: fish[2]))

    def get_fresh_fish_sorted_by_price(self) -> List[Tuple[FishInfo, float, float]]:
        return list(sorted(list(self.fresh_fish), key = lambda fish: fish[2]))

    def get_frozen_fish_sorted_by_price(self) -> List[Tuple[FishInfo, float, float]]:
        return list(sorted(list(self.frozen_fish), key = lambda fish: fish[2]))


test = Fish("ryba", "america", date.fromisoformat("2012-12-02"), date.fromisoformat("2015-02-02"), 35, 34)

print(test.name)
#Below the code block which will be deleted
"""
class Place:
    pass

class Employee:
    pass

class Goods:
    pass

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

    def get_fish_names_sorted_by_price(self) -> List[Fish]:
        return list(sorted(
            self.available_fish,
            key=lambda fish: fish.price_in_uah_per_kilo
            ))

    def cast_out_old_fish(self, is_that_after_days: int = 30) -> List[Fish]:
        out = list(self.available_fish)
        min_good_date = datetime.date.today() - datetime.timedelta(days = is_that_after_days)
        self.available_fish = list(filter(lambda fish: fish.catch_date >= min_good_date, self.available_fish))
        return list(filter(lambda fish: fish not in self.available_fish, out ))

class Seller:
    def __init__(self,full_name:str, id:int, money:float, place_of_work:Place, place_of_residence: Place):
        pass
    def pay_taxes(self, tax_premium_percentage: int = 30) -> None:
        pass
    def available_goods(self) -> List[Goods]:
        pass
    def order_goods(self, goods:List[Goods]) -> None:
        pass
    def pay_employee(self, employee: str, money:int) -> None:
        pass
    def hire_employee(self, employee: Employee) -> None:
        pass
    def fire_employee(self, employee: str) -> Employee:
        pass
    def make_revision(self) -> None:
        pass
    def cast_out_old_goods(self) -> List[Goods]:
        pass
class Buyer:
    def __init__(self, full_name:str, id: int, money:float, place_of_residence: Place, preferences: List[str]) ->None:
        pass
    def buy(goods:List[Goods]) -> None:
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
"""