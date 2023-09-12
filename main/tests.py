from django.test import TestCase
from .models import Product

# Create your tests here.
class mainTest(TestCase):
    def setUp(self):
        self.data= Product.objects.create(
            name = "Fifa 23",
            price = 40000,
            amount = 20,
            category = "Sport",
            platform = "PC, Nitendo Switch, Xbox X|S, Xbox One, Playstation 4",
            description = "The game offers revamped Career Mode, FIFA Ultimate Team (FUT), and the return of Volta Football for a diverse gaming experience.",

        ) 
    
    def test_product(self):
        self.assertEqual(self.data.name, "Fifa 23")
        self.assertEqual(self.data.price, 40000)
        self.assertEqual(self.data.amount, 20)
        self.assertEqual(self.data.category, "Sport")
        self.assertEqual(self.data.platform, "PC, Nitendo Switch, Xbox X|S, Xbox One, Playstation 4")
        self.assertEqual(self.data.description, "The game offers revamped Career Mode, FIFA Ultimate Team (FUT), and the return of Volta Football for a diverse gaming experience.")        