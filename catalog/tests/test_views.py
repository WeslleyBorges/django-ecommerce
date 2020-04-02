from catalog.models import *
from django.urls import reverse
from model_mommy import mommy
from django.test import TestCase

class CategoryTestCase(TestCase):
    def setUp(self):
        self.category = mommy.make(Category)

    def test_get_absolute_url(self):
        self.assertEquals(
            self.category.get_absolute_url(),
            reverse('catalog:category', kwargs={'slug': self.category.slug})
        )

class ProductTestCase(TestCase):
    def setUp(self):
        self.product = mommy.make(Product, slug='produto')

    def test_get_absolute_url(self):
        self.assertEquals(
            self.product.get_absolute_url(),
            reverse('catalog:product', kwargs={'slug': 'produto'})
        )

