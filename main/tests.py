from django.test import TestCase
from .models import Contact

class ContactTest(TestCase):
	def testing_contact(self):
		saved = Contact.objects.create(name = "Abdul Muis", phone = "08812577839")
		self.assertEqual(saved.name, "Abdul Muis")
		self.assertEqual(saved.phone, "08812577839")