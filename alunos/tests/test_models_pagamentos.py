from decimal import Decimal
from django.test import TestCase
from pagamentos.models.models_pagamentos import Payments, default_month
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

    def test_val_validation_default(self):
        aluno = Payments.objects.first()
        self.assertEqual(aluno.val, 0.00)

    def test_month_validation_default(self):
        aluno = Payments.objects.first()
        self.assertEqual(aluno.month, default_month())

    def test_pay_validation_default(self):
        aluno = Payments.objects.first()
        self.assertEqual(aluno.pay, False)

    def test_val_validation_no_default(self):
        self.payment.val = 163.34
        self.payment.save()
        payment = Payments.objects.first()
        self.assertEqual(payment.val, Decimal('163.34'))

    def test_pay_validation_no_default(self):
        self.payment.pay = True
        self.payment.save()
        payment = Payments.objects.first()
        self.assertEqual(payment.pay, True)
