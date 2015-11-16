from python import Professor
class Disciplina:
    nome = None
    professor = None
    turmas = None
    duracao = None
    
    def __init__(self, nome,professor,turmas):
        self.nome = nome
        self.professor = professor
        self.turmas = turmas
    