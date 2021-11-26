DAY_CHOICE = (
    ('segunda-feira', 'Segunda-Feira'),
    ('terça-feira', 'Terça-Feira'),
    ('quarta-feira', 'Quarta-Feira'),
    ('quinta-feira', 'Quinta-Feira'),
    ('sexta-feira', 'Sexta-Feira'),
)

SCHEDULE_CHOICE = [
    ('Manhã', (
        ('m1', 'M1 (07:00 / 08:00)'),
        ('m2', 'M2 (08:00 / 09:00)'),
        ('m3', 'M3 (09:00 / 10:00)'),
        ('m4', 'M4 (10:00 / 11:00)'),
        ('m5', 'M5 (11:00 / 12:00)'),)
     ),

    ('Tarde/Noite', (
        ('t1', 'T1 (16:00 / 17:00)'),
        ('t2', 'T2 (17:00 / 18:00)'),
        ('t3', 'T3 (18:00 / 19:00)'),
        ('t4', 'T4 (19:00 / 20:00)'),
        ('t5', 'T5 (20:00 / 21:00)'),
        ('t6', 'T6 (21:00 / 22:00)'),)
     ),
]

STATUS_CHOICE = (
    ('ativo', 'Ativo'),
    ('inativo', 'Inativo'),
)

MONTH_CHOICE = (
    ('janeiro', 'Janeiro'),
    ('fevereiro', 'Fevereiro'),
    ('março', 'Março'),
    ('abril', 'Abril'),
    ('maio', 'Maio'),
    ('junho', 'Junho'),
    ('julho', 'Julho'),
    ('agosto', 'Agosto'),
    ('setembro', 'Setembro'),
    ('outubro', 'Outubro'),
    ('novembro', 'Novembro'),
    ('dezembro', 'Dezembro'),
)



from .models_alunos import *
from .models_turmas import *
from .models_boleto import *
from .models_pagamentos import *
