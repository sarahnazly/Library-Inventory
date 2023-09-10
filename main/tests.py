from django.test import TestCase
from .models import Item

# Create your tests here.
class ItemModelTest(TestCase) :
    def setUp(self):
        self.item = Item.objects.create(
            name = 'Test Book',
            amount = 5,
            description = 'This was a test book',
            category = 'Fiction',
            tanggal_peminjaman = None,
        )
    
    def test_attributes_item(self) :
        self.assertEqual(self.item.name, 'Test Book')
        self.assertEqual(self.item.amount, 5)
        self.assertEqual(self.item.description, 'This was a test book')
        self.assertEqual(self.item.category, 'Fiction')
        self.assertEqual(self.item.tanggal_peminjaman, None)