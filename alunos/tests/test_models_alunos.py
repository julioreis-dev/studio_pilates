from django.test import TestCase, Client
from alunos.models.models_alunos import People
from model_mommy import mommy


class PeopleModelTest(TestCase):
    def setUp(self):
        self.aluno = mommy.make('People')

    def test_people_exist(self):
        aluno = People.objects.first()
        self.assertIsNotNone(aluno)

    def test_str(self):
        attrstr = f'{self.aluno}'
        self.assertEquals(str(self.aluno), attrstr)

class PeopleModelTes2(TestCase):
    def setUp(self):
        self.aluno = mommy.make('People')
        self.aluno.email = None

    def test_email_validation(self):
        aluno = People.objects.all()
        self.assertIsNone(aluno)

