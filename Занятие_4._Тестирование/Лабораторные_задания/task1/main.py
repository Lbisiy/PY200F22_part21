from abc import abstractmethod
import unittest

class Object:
    @abstractmethod
    def __init__(self):
        self.status = 'Предложение'
        self.agent_commission = 1

    def __repr__(self) -> str:
        return f"{self.status}"


class ForRent(Object):
    def __init__(self):
        super().__init__()
        self.status = 'Аренда'
        self.agent_commission = 0.05


class ForSale(Object):

    def __init__(self):
        super().__init__()
        self.status = 'Продажа'
        self.agent_commission = 0.1


class Client:
    @abstractmethod
    def __init__(self, type_="Клиент"):
        self.type = type_
        self.name = None
        self.e_mail = None
        self.phone_number = None

    def __repr__(self) -> str:
        return f"{self.type}, {self.name}, {self.e_mail}, {self.phone_number}"


class Seller(Client):
    def __init__(self, type_="Продавец"):
        super().__init__(type_)


class Landlord(Client):
    def __init__(self, type_="Арендодатель"):
        super().__init__(type_)


class Agency(Client):
    def __init__(self, type_="Агентство"):
        super().__init__(type_)


class RealEstate:
    Type_of_real_estate = [
        ["Офис", "Здание", "Магазин", "Склад"],
        ["Дом", "Квартира", "Гараж", "Комната", "Участок"]
    ]

    id_ = 0

    @abstractmethod
    def __init__(self, type_object, square, price, text=None):
        self._classification = "Недвижимость"
        self._description = None
        self.address = None

        self.type_object = type_object
        self.square = square
        self.price = price

        self.id_ = 0
        self.id_ = self._id_number()
        self.set_description(text)

    @property
    def classification(self):
        return self._classification

    @property
    def type_object(self) -> str:
        return self._type_object

    @type_object.setter
    def type_object(self, type_object) -> None:
        if type_object not in self.Type_of_real_estate[0] and type_object not in self.Type_of_real_estate[1]:
            raise ValueError("Неверно указан тип объекта")
        self._type_object = type_object

    @classmethod
    def _id_number(cls) -> int:
        cls.id_ += 1
        return cls.id_

    @property
    def price(self) -> float:
        return self._price

    @price.setter
    def price(self, price: (int, float)) -> None:
        if not isinstance(price, (int, float)):
            raise TypeError("Значение цены должно быть [int, float]")
        if price <= 0:
            raise ValueError("Значение цены должно быть больше нуля")
        self._price = float(price)

    @property
    def square(self) -> int:
        return self._square

    @square.setter
    def square(self, square: (int, float)) -> None:
        if not isinstance(square, (int, float)):
            raise TypeError("Значение площади должно быть [int, float]")
        if square <= 0:
            raise ValueError("Значение площади должно быть больше нуля")
        self._square = int(square)

    @property
    def description(self) -> str:
        return self._description

    def set_description(self, text: str) -> None:
        if not isinstance(text, (str, type(None))):
            raise TypeError("Описание должно быть текстом")
        if isinstance(text, str) and len(text) > 100:
            raise TypeError("Описание должно быть длиной не более 100 символов")
        self._description = text

    def __str__(self) -> str:
        return f"\n--------------------\nОбъект: {self.id_}.\n\nОписание: {self._description}.\nТип: {self.type_object}."\
               f"\nАдрес: {self.address}.\nПлощадь: {self.square} м2.\nЦена: {self.price} руб.\n--------------------\n"

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({self.type_object!r}, {self.square}, {self.price})"


class CommercialRealEstate(RealEstate):

    def __init__(self, type_object, square, price, text=None):
        super().__init__(type_object, square, price, text)
        self._sub_classification = 'Коммерческая недвижимость'

    @property
    def sub_classification(self):
        return self._sub_classification


class Office(CommercialRealEstate):
    def __init__(self, type_object, square, price, text=None):
        super().__init__(type_object, square, price, text)
        self._sub_sub_classification = 'Офисы'

    @property
    def sub_sub_classification(self):
        return self._sub_sub_classification


# class PrivateRealEstate(RealEstate):
#     ...
#
#
# class Apartment(PrivateRealEstate):
#     ...


class DataBase:
    def __init__(self):
        self.data_rows = []

    def add_to_data_base(self, obj: Object, type_of_obj: RealEstate, client: Client):
        if not isinstance(obj, Object):
            raise TypeError("Передан неверный тип")
        if not isinstance(type_of_obj, RealEstate):
            raise TypeError("Передан неверный тип")
        if not isinstance(client, Client):
            raise TypeError("Передан неверный тип")
        line = f"{obj}{type_of_obj}{client}"
        self.data_rows.append(line)

    def print_data_base(self):
        for data in self.data_rows:
            print(data)

    def __repr__(self):
        return f"{list(self.data_rows)}"


class CommissionCalculator:
    @staticmethod
    def commission(estate: RealEstate, obj: Object):
        if not isinstance(estate, RealEstate) and not isinstance(obj, Object):
            raise TypeError("Неверный интерфейс")
        agent_commission = estate.price * obj.agent_commission
        return agent_commission


if __name__ == '__main__':
    unittest.main()
