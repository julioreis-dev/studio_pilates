from django.test import TestCase
from alunos.models.models_turmas import Turmas
from model_mommy import mommy


class TurmasModelTest(TestCase):
    def setUp(self):
        self.turmas = mommy.make('Turmas')

    def test_Turmas_exist(self):
        tur = Turmas.objects.first()
        self.assertIsNotNone(tur)

    def test_str(self):
        attrstr = f'{self.turmas.day} / {self.turmas.schedule}'
        self.assertEquals(str(self.turmas), attrstr)

    def test_total(self):
        number = self.turmas.alunos.count()
        response = f'Disponível {3-number} vaga(s)'
        self.assertEquals(response, self.turmas.total())
