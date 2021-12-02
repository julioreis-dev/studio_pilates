from django.test import TestCase
from alunos.models.models_pagamentos import Payments
from model_mommy import mommy


class PaymentsModelTest(TestCase):
    def setUp(self):
        self.payment = mommy.make('Payments')

    def test_payments_exist(self):
        payment = Payments.objects.first()
        self.assertIsNotNone(payment)

    def test_str(self):
        attrstr = f'{self.payment}'
        self.assertEquals(str(self.payment), attrstr)
