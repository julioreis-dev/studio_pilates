from django.test import TestCase
from alunos.models.models_boleto import Bills
from model_mommy import mommy


class BillsModelTest(TestCase):
    def setUp(self):
        self.people = mommy.make('Bills')

    def test_bills_exist(self):
        bill = Bills.objects.first()
        self.assertIsNotNone(bill)

    def test_str(self):
        attrstr = f'{self.people}'
        self.assertEquals(str(self.people), attrstr)
