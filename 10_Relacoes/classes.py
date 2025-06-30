class Aluno:
    def __init__(self, nome, matricula, cpf):
        self.__nome = nome
        self.__matricula = matricula
        self.__cpf = cpf
        self.cursos_inscritos = []
    
    # método de acesso
    @property
    def nome(self):
        return self.__nome
    @nome.setter
    def nome(self,nome):
        self.__nome = nome 
    
    # método de acesso
    @property
    def matricula(self):
        return self.__matricula
    @matricula.setter
    def matricula(self,matricula):
        self.__matricula = matricula
    
    # método de acesso
    @property
    def cpf(self):
        return self.__cpf
    @cpf.setter
    def cpf(self,cpf):
        self.__cpf = cpf
    
    def inscrever_curso(self, curso):
        if curso not in self.cursos_inscritos:
            self.cursos_inscritos.append(curso)
            curso.adicionar_aluno(self)
    
    def lista_cursos(self):
        lista = []
        for curso in self.cursos_inscritos:
            lista.append(curso.nome_curso)
            return lista

    def __del__(self):
        print(f"Objeto {self.nome} destruido com sucesso.")

class Curso:
    def __init__(self, nome_curso):
        self.__nome_curso = nome_curso
        self.alunos_inscritos = []
    
    # método de acesso
    @property
    def nome_curso(self):
        return self.__nome_curso
    
    @nome_curso.setter
    def nome_curso(self, nome_curso):
        self.__nome_curso = nome_curso
    
    # método de ação
    def adicionar_aluno(self, aluno):
        if aluno not in self.alunos_inscritos:
            self.alunos_inscritos.append(aluno)
        aluno.inscrever_curso(self)
    
    def listar_alunos(self):
        lista = []
        for aluno in self.alunos_inscritos:
            lista.append(aluno.nome)
        return lista
    
    # método especial
    def __del__(self):
        print(f"Objeto {self.nome_curso}")