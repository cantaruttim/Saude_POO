from medico import Medico
from paciente import Pessoa

class Medicamento:

    def __init__(self, nome, dose, ADR, posologia, indicacao):
        self.nome = nome
        self.dose = dose
        self.ADR = ADR
        self.posologia = posologia
        self.indicacao = indicacao
