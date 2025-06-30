from classes import Aluno, Curso
import os

def limpar():
    os.system("cls" if os.name == "nt" else "clear")

if __name__ == "__main__":
    alunos = []
    cursos = []
    matricula = 0

    limpar()
    while True:
        aluno = Aluno(nome="", matricula=0, cpf="")
        curso = Curso(nome_curso="")

        print(f"{'-'*20} SISTEMA ESCOLAR {'-'*20}")
        print("1 - Cadastra aluno.")
        print("2 - Cadastra cursos")
        print("3 - Matricular aluno no curso.")
        print("4 - Listar cursos.")
        print("5 - Listar alunos.")
        print("6 - Sair do programa.")
        opcao = input("Informe a ação desejada: ").strip()

        limpar()
        match opcao:
            case "1":
                try:
                    matricula += 1
                    aluno.nome = input("Informe o nome do aluno: ").strip().title()
                    aluno.cpf = input("Informe o CPF do aluno: ").strip()
                    aluno.matricula = matricula

                    alunos.append(aluno)
                    limpar()

                    print(f"{aluno.nome} matriculado com sucesso.")
                except Exception as e:
                    print(f"não foi possível cadastrar aluno. {e}.")
                finally:
                    continue
            case "2":
                try:
                   curso.nome_curso = input("Informe o curso: ").strip().title()
                   cursos.append(curso)
                   limpar()

                   print(f"Curso {curso.nome_curso} cadastrado com sucesso.")
                except Exception as e:
                   print(f"Não foi possível cadastrar curso. {e}.")
                finally:
                   continue
            case "3":
                print(f"{'-'*20} Lista de Alunos {'-'*20}\n")
                for aluno in alunos:
                    print(f"Nome: {aluno.nome}")
                    print(f"Matricula: {aluno.matricula}")
                    print(f"CPF: {aluno.cpf}")
                    print('-'*40)
                inscricao = int(input("Informe a matrícula: "))
                for aluno in alunos:
                    aluno = {
                            'nome': aluno.nome,
                            'matricula': aluno.matricula,
                            'cpf': aluno.cpf
                    }
                    if inscricao in aluno['matricula']:
                        break

                limpar()

                print(f"{'-'*20} Lista de Cursos {'-'*20}")
                for curso in cursos:
                    print(f"Curso: {curso.nome_curso}")
                curso_inscricao = input("Informe o curso desejado: ").strip().title()
                aluno.inscrever_curso(curso_inscricao)
                limpar()

                print(f"Aluno {aluno.nome} inscrito no curso {curso.nome_curso} com sucesso.")
                # else:
                #     print("Não foi possível encontrar a matrícula.")
            case "4":
                cursos.nome_curso.sort()
                for curso in cursos:
                    print(f"Curso: {curso.nome_curso}")
                    print(f"alunos:")
                    curso.listar_alunos().sort()
                    for aluno in curso.listar_alunos():
                        print(aluno)
                    print({'-'*60})    
            case "5":
                alunos.nome.sort()
                for aluno in alunos:
                    print(f"Nome: {aluno.nome}")
                    print(f"Matricula : {aluno.matricula}")
                    print(f"CPF: {aluno.cpf}")
                    print("Cursos Matriculados: ")
                    aluno.listar_cursos().sort()
                    for curso in aluno.listar_cursos():
                        print(curso)
                    print({'-'*60})
            case "6":
                print("Programa encerrado.")
                break
            case _:
                print("Opção Inválida.")
                continue

    # #Alunos
    # aluno01 = Aluno("Fulano", 101, "111.111.111-11")
    # aluno02 = Aluno("Cicrano", 102, "222.222.222-22")
    # aluno03 = Aluno("Betrano", 103, "333.333.333-33")
    # aluno04 = Aluno("João", 104, "444.444.444-44")
    # aluno05 = Aluno("Maria", 105, "555.555.555-55")
    # aluno06 = Aluno("José", 106, "666.666.666-66")

    # #Cursos
    # curso01 = Curso("Python Developer")
    # curso02 = Curso("IA com Python")
    # curso03 = Curso("Desenvolvedor Java")

    # #Incremento os alunos nos  cursos
    # aluno01.inscrever_curso(curso01)
    # aluno02.inscrever_curso(curso01)
    # aluno03.inscrever_curso(curso01)

    # aluno04.inscrever_curso(curso02)
    # aluno05.inscrever_curso(curso02)

    # aluno06.inscrever_curso(curso03)

    # #mostrar alunos nos cursos
    # print(f"Curso {curso01.nome_curso} tem os alunos: {curso01.listar_alunos}")