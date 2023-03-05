import unittest
from main import Object, ForRent, ForSale, Client, Seller, Landlord, Agency, RealEstate, CommercialRealEstate, Office, DataBase, CommissionCalculator


def setUpModule():
    global obj, for_rent, for_sale, client, seller, landlord, agent, real_estate1, real_estate2, \
        commercial_estate, office, data_base, calculator

    obj = Object()
    for_rent = ForRent()
    for_sale = ForSale()
    client = Client()
    seller = Seller()
    landlord = Landlord()
    agent = Agency()
    real_estate1 = RealEstate("Офис", 100, 100)
    real_estate2 = RealEstate("Здание", 1000, 3000)
    commercial_estate = CommercialRealEstate("Офис", 500, 300)
    office = Office("Офис", 100, 100)
    data_base = DataBase()
    calculator = CommissionCalculator()


class TestObject(unittest.TestCase):
    def test_atr(self):
        self.assertIsInstance(obj, Object)
        self.assertEqual(obj.status, 'Предложение')
        self.assertEqual(obj.agent_commission, 1)


class TestForRent(unittest.TestCase):
    def test_atr(self):
        self.assertIsInstance(for_rent, ForRent)
        self.assertEqual(for_rent.status, 'Аренда')
        self.assertEqual(for_rent.agent_commission, 0.05)
        self.assertTrue(issubclass(ForRent, Object))


class TestForSale(unittest.TestCase):
    def test_atr(self):
        self.assertIsInstance(for_sale, ForSale)
        self.assertEqual(for_sale.status, 'Продажа')
        self.assertEqual(for_sale.agent_commission, 0.1)
        self.assertTrue(issubclass(ForSale, Object))


class TestClient(unittest.TestCase):
    def test_atr(self):
        self.assertIsInstance(client, Client)
        self.assertEqual(client.type, 'Клиент')
        self.assertIsNone(client.name)
        self.assertIsNone(client.e_mail)
        self.assertIsNone(client.phone_number)


class TestSeller(unittest.TestCase):
    def test_atr(self):
        self.assertIsInstance(seller, Seller)
        self.assertEqual(seller.type, 'Продавец')
        self.assertIsNone(seller.name)
        self.assertIsNone(seller.e_mail)
        self.assertIsNone(seller.phone_number)
        self.assertTrue(issubclass(Seller, Client))


class TestLandLord(unittest.TestCase):
    def test_atr(self):
        self.assertIsInstance(landlord, Landlord)
        self.assertEqual(landlord.type, 'Арендодатель')
        self.assertIsNone(landlord.name)
        self.assertIsNone(landlord.e_mail)
        self.assertIsNone(landlord.phone_number)
        self.assertTrue(issubclass(Landlord, Client))


class TestAgency(unittest.TestCase):
    def test_atr(self):
        self.assertIsInstance(agent, Agency)
        self.assertEqual(agent.type, 'Агентство')
        self.assertIsNone(agent.name)
        self.assertIsNone(agent.e_mail)
        self.assertIsNone(agent.phone_number)
        self.assertTrue(issubclass(Agency, Client))


class TestRealEstate(unittest.TestCase):
    def test_init(self):
        self.assertIsInstance(real_estate1, RealEstate)
        self.assertEqual(real_estate1.classification, "Недвижимость")
        self.assertIsNone(real_estate1.description)
        self.assertIsNone(real_estate1.address)
        self.assertEqual(real_estate1.type_object, "Офис")
        self.assertEqual(real_estate1.square, 100)
        self.assertEqual(real_estate1.price, 100.0)
        self.assertEqual(real_estate1.id_, 1)

    def test_type_object(self):
        with self.assertRaises(ValueError):
            real_estate1.type_object = "Земля"

    def test_id_number(self):
        self.assertEqual(real_estate2.id_, 2)

    def test_price(self):
        with self.assertRaises(TypeError):
            real_estate1.price = "500"
        with self.assertRaises(ValueError):
            real_estate1.price = -500

    def test_square(self):
        with self.assertRaises(TypeError):
            real_estate1.square = "1000"
        with self.assertRaises(ValueError):
            real_estate1.square = -1000

    def test_set_description(self):
        with self.assertRaises(TypeError):
            real_estate1.set_description(48758943759734895)
        with self.assertRaises(TypeError):
            real_estate1.set_description("Паькаль кьаплкалкаь улаьлукалткуьать ьтаькутаькутаьткуьа уатьутаьутаь/"
                                         "ьутаьутьатуьатьутаьтуьатутиаьиуьатиьутиаьутиьатьуцтуаьутаутаьуьатьуаьта/"
                                         "ьутаьтуаьтуьтаьбутаьбтуьбатьбутаьбтуьбатьбутаьбтуьбатьбутаьбтуцьбатьбут/"
                                         "оутаотуцьатуьбцтаьтуоатуьцтаьуцталтуцлатьуцтаьтуцолаолуцтаолтуцолатуолца")


class TestCommercialRealEstate(unittest.TestCase):
    def test_init(self):
        self.assertIsInstance(commercial_estate, CommercialRealEstate)
        self.assertEqual(commercial_estate.classification, "Недвижимость")
        self.assertIsNone(commercial_estate.address)
        self.assertEqual(commercial_estate.type_object, "Офис")
        self.assertEqual(commercial_estate.square, 500)
        self.assertEqual(commercial_estate.price, 300.0)
        self.assertEqual(commercial_estate.id_, 3)
        self.assertEqual(commercial_estate.sub_classification, "Коммерческая недвижимость")
        self.assertTrue(issubclass(CommercialRealEstate, RealEstate))


class TestOffice(unittest.TestCase):
    def test_init(self):
        self.assertIsInstance(office, Office)
        self.assertEqual(office.classification, "Недвижимость")
        self.assertIsNone(office.address)
        self.assertEqual(office.type_object, "Офис")
        self.assertEqual(office.square, 100)
        self.assertEqual(office.price, 100.0)
        self.assertEqual(office.id_, 4)
        self.assertEqual(office.sub_classification, "Коммерческая недвижимость")
        self.assertTrue(issubclass(Office, CommercialRealEstate))
        self.assertEqual(office.sub_sub_classification, 'Офисы')


class TestDataBase(unittest.TestCase):

    def tearDown(self) -> None:
        data_base.data_rows.clear()

    def test_init(self):
        self.assertIsInstance(data_base.data_rows, list)
        for num in data_base.data_rows:
            self.assertIsNone(num)

    def test_add_to_data_base(self):
        with self.assertRaises(TypeError):
            data_base.add_to_data_base(0, real_estate1, client)
        with self.assertRaises(TypeError):
            data_base.add_to_data_base(obj, 0, client)
        with self.assertRaises(TypeError):
            data_base.add_to_data_base(obj, real_estate1, 0)
        data_base.add_to_data_base(obj, real_estate1, client)
        self.assertEqual(data_base.data_rows[0], f"Предложение\n--------------------\nОбъект: {real_estate1.id_}.\n\nОписание: {real_estate1._description}.\nТип: {real_estate1.type_object}.\nАдрес: {real_estate1.address}.\nПлощадь: {real_estate1.square} м2.\nЦена: {real_estate1.price} руб.\n--------------------\nКлиент, None, None, None")


class TestCommissionCalculator(unittest.TestCase):
    def test_commission(self):
        with self.assertRaises(TypeError):
            calculator.commission(0, 0)
        self.assertEqual(calculator.commission(real_estate2, obj), 3000)


# if __name__ == '__main__':
#     unittest.main()
