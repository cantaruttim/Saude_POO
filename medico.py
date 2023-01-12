from paciente import Pessoa
from medicamento import Medicamento

class Medico:

    """
    Representa a Entidade Médico, responsável por atender um paciente

    nome (str) : nome do médico
    idade (int) : idade do médico
    especialidade (str) : representa a especialidade médica,
                          também restringe os tipos de medicamentos que o médico pode prescrever

    """


    def __init__(self, nome, idade, especialidade):
        self.nome = nome
        self.idade = idade
        self.especialidade = especialidade

