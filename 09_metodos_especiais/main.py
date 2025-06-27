from classes import Pessoa
import os

def limpar():
    os.system("cls" if os.name == "nt" else "clear")

if __name__ == "__main__":
    usuario = Pessoa(nome="", profissao="", idade="")

    while True:

        print("1 - Inserir dados e exibir")
        print("2 - sair do programa")
        opcao = input("Informe a opção desejada: ").strip()
        limpar()
        match opcao:
            case "1":
                try:
                    usuario.nome = input("Informe o nome: ").strip().title()
                    usuario.profissao = input("Informe a profissão: ").strip()
                    usuario.idade = int(input("Informe sua idade: "))

                    """
                    print(f"Nome: {usuario.nome}")
                    print(f"Profissão: {usuario.profissao}")
                    """
                    
                    limpar()
                    print(usuario)
                    print(f"Idade de {usuario.nome}: {len(usuario)} anos")

                    
                except Exception as e:
                    print(f"Não foi possível executar o programa. {e}.")
                """
                    del(usuario)
                """
                continue
            case "2":
                break
            case _:
                print("Opção inválida.")
                continue