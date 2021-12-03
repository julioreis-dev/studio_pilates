from django.test import TestCase
from alunos.models.models_turmas import Turmas
from model_mommy import mommy


class TurmasModelTest(TestCase):
    def setUp(self):
        self.turma = mommy.make('Turmas')

    def test_Turmas_exist(self):
        tur = Turmas.objects.first()
        self.assertIsNotNone(tur)

    def test_str(self):
        attrstr = f'{self.turma.day} / {self.turma.schedule}'
        self.assertEquals(str(self.turma), attrstr)

    def test_val_validation_default(self):
        turma = Turmas.objects.first()
        self.assertEqual(turma.day, 'segunda-feira')

    def test_schedule_validation_default(self):
        turma = Turmas.objects.first()
        self.assertEqual(turma.schedule, 'm1')

    def test_val_validation_no_default(self):
        self.turma.day = 'quarta-feira'
        self.turma.save()
        turma = Turmas.objects.first()
        self.assertEqual(turma.day, 'quarta-feira')

    def test_schedule_validation_no_default(self):
        self.turma.schedule = 'm3'
        self.turma.save()
        turma = Turmas.objects.first()
        self.assertEqual(turma.schedule, 'm3')

    def test_total(self):
        number = self.turma.alunos.count()
        response = f'Disponível {3 - number} vaga(s)'
        self.assertEquals(response, self.turma.total())
