from django.test import TestCase
from alunos.models.models_boleto import Bills
from model_mommy import mommy
import datetime


class BillsModelTest(TestCase):
    def setUp(self):
        self.bill = mommy.make('Bills')

    def test_bills_exist(self):
        bill = Bills.objects.first()
        self.assertIsNotNone(bill)

    def test_str(self):
        attrstr = f'{self.bill}'
        self.assertEquals(str(self.bill), attrstr)

    def test_ano_validation_default(self):
        bill = Bills.objects.first()
        self.assertEqual(bill.ano, datetime.date.today().year)

    def test_ano_validation_no_default(self):
        self.bill.ano = 2019
        self.bill.save()
        bill = Bills.objects.first()
        self.assertEqual(bill.ano, 2019)
