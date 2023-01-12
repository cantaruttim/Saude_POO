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



class Pessoa:

    """
    Representa a entidade Pessoa/Paciente.

    nome (str) : nome do paciente
    idade (int) : idade do paciente. Representa também uma variável de risco. Quanto maior ou menor
                  maior o risco (considerando pessoas que tomam muitos medicamentos)
    queixa (str) : Queixa ou motivo pelo qual o paciente procurou o médico
    medicamentos (lst) : Representa os medicamentos que o paciente na hora da consulta, informa
                        fazer uso para que o médico possa avaliar.

    """

    # a ideia é fazer com que a IA indique a possível causa (diagnóstico) e um tratamento
    def __init__(self, nome, idade, queixa):
        self.nome = nome
        self.idade = idade
        self.queixa = queixa
        self.medicamentos = []




class Medicamento:

    def __init__(self, nome, dose, ADR, posologia, indicacao):
        self.nome = nome
        self.dose = dose
        self.ADR = ADR
        self.posologia = posologia
        self.indicacao = indicacao