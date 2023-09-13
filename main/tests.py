from django.test import TestCase, Client
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

    def test_product_amount_not_negative(self):
        product = Product(name="Test Game", amount=10, price=100, category="Game", platform="PC", description="Test")
        
        self.assertTrue(product.amount >= 0)
    
    def setUp_web(self):
        self.client = Client()

    def test_template_elements(self):
        response = self.client.get('/main/') 

        self.assertEqual(response.status_code, 200) 

        self.assertContains(response, "<h1>Game Sthar</h1>")
        self.assertContains(response, "<h5>Name: </h5>")
        self.assertContains(response, "<h4>Game: </h4>")
        self.assertContains(response, "<h4>Amount: </h4>")
        self.assertContains(response, "<h4>Price: </h4>")
        self.assertContains(response, "<h4>Category: </h4>")
        self.assertContains(response, "<h4>Platform: </h4>")
        self.assertContains(response, "<h4>Description: </h4>")
   
        context = response.context  
        self.assertIn("name", context)
        self.assertIn("game", context)
        self.assertIn("amount", context)
        self.assertIn("price", context)
        self.assertIn("category", context)
        self.assertIn("platform", context)
        self.assertIn("description", context)
