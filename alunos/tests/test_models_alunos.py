from django.db import IntegrityError
from django.test import TestCase
from alunos.models.models_alunos import People
from model_mommy import mommy


class PeopleModelTest(TestCase):
    def setUp(self) -> None:
        self.aluno = mommy.make('People')

    def test_people_exist(self):
        aluno = People.objects.first()
        self.assertIsNotNone(aluno)

    def test_str(self):
        attrstr = f'{self.aluno}'
        self.assertEquals(str(self.aluno), attrstr)

    def test_day_validation_default(self):
        aluno = People.objects.first()
        self.assertEqual(aluno.day, 'segunda-feira')

    def test_schedule_validation_default(self):
        aluno = People.objects.first()
        self.assertEqual(aluno.schedule, 'm1')

    def test_status_validation_default(self):
        aluno = People.objects.first()
        self.assertEqual(aluno.status, 'ativo')

    def test_day_validation_no_default(self):
        self.aluno.day = 'terça-feira'
        self.aluno.save()
        aluno = People.objects.first()
        self.assertEqual(aluno.day, 'terça-feira')

    def test_schedule_validation_no_default(self):
        self.aluno.schedule = 'm3'
        self.aluno.save()
        aluno = People.objects.first()
        self.assertEqual(aluno.schedule, 'm3')

    def test_status_validation_no_default(self):
        self.aluno.status = 'inativo'
        self.aluno.save()
        aluno = People.objects.first()
        self.assertEqual(aluno.status, 'inativo')

    def test_name_validation(self):
        with self.assertRaises(IntegrityError) as context:
            self.aluno.name = None
            self.aluno.save()
        self.assertTrue('NOT NULL constraint failed' in str(context.exception))

    def test_tel1_validation(self):
        with self.assertRaises(IntegrityError) as context:
            self.aluno.tel1 = None
            self.aluno.save()
        self.assertTrue('NOT NULL constraint failed' in str(context.exception))

    def test_email_validation(self):
        with self.assertRaises(IntegrityError) as context:
            self.aluno.email = None
            self.aluno.save()
        self.assertTrue('NOT NULL constraint failed' in str(context.exception))
