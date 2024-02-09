from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User

from Clients.models import Cliente
from product.models import ProductCategory

class TestRegister(TestCase):
    def test_register_cliente(self):
        client_instance = User.objects.create(name="Jose", password1 = "holacomotas", password2 = "holacomotas")
        self.url = reverse('register', args=[client_instance])

class TestRegister_ProductsCategory(TestCase):
    def test_register_product_category(self):
        product_instance = ProductCategory.objects.create(name="Shirts")
        self.url = reverse('productcategory_create', args=[product_instance])

    def test_eliminar_categoria(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'productcategory_delete')
        self.assertQuerySetEqual(ProductCategory.objects.all(), [])