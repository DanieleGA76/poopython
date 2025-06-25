# biblioteca
import classes
import os

if __name__ == "__main__":
    usuario = classes.PessoaFisica("", "", "", "", "", "", "")
    empresa = classes.PessoaJuridica("", "", "", "", "","")

    # limpeza de tela
    os.system("cls" if os.name == "nt" else "clear")

    # atribui valores do objeto do tipo pessoa física
    print(f"{'-'*20} DADOS DO USUÁRIO {'-'*20}")

    usuario.nome = input("Informe seu nome: ").title().strip()
    usuario.cpf = input("Infomre o CPF: ").strip()
    usuario.profissao = input("Informe sua profissão: ").strip()
    usuario.genero = input("Informe seu gênero: ").strip()
    usuario.email = input("Informe o seu e-mail: ").strip().lower()
    usuario.endereco = input("Informe seu endereço: ").strip().title()
    usuario.telefone = input("Informe seu telefone: ").strip()

    # limpa a tela
    os.system("cls" if os.name == "nt" else "clear")

    # atribui valores do objeto do tipo Pessoa Juridica
    empresa.razao_social = input("Informe a razão social da empresa: ").title().strip()
    empresa.nome_fantasia = input("Informe o nome fantansia: ").title().strip()
    empresa.cnpj = input("Informe o CNPJ: ").strip()
    empresa.email = input("Informe o e-mail: ").strip().lower()
    empresa.endereco = input("Informe o endereço da empresa: ").strip().title()
    empresa.telefone = input("Informe o telefone da empresa: ").strip()

    # limpar a tela
    os.system("cls" if os.name == "nt" else "clear")

    # exibir os dados do usuário:
    print("Dados dos usuario: \n")
    usuario.exibir_dados()
    print(f"-"*60)
    print("Dados da empresa: \n")
    empresa.exibir_dados()