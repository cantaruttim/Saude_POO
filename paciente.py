from medico import Medico
from medicamento import Medicamento

class Pessoa:

    # a ideia é fazer com que a IA indique a possível causa (diagnóstico) e um tratamento
    def __init__(self, nome, idade, queixa, medicamentos):
        self.nome = nome
        self.idade = idade
        self.queixa = queixa
        self.medicamentos = medicamentos