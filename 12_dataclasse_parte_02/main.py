from classes import PessoaFisica, PessoaJuridica
import os

def limpar():
    os.system("cls" if os.name == "nt" else "clear")

if __name__ == "__main__":
    usuario = PessoaFisica(
        nome="", 
        cpf="", 
        profissao ="",
        email="",
        telefone="",
        endereco=""
        )
    
    empresa = PessoaJuridica(
        razao_social="",
        nome_fantasia="",
        cnpj="",
        email="",
        telefone="",
        endereco=""
    )
    
    print("Informe os dados do usuário: \n")
    usuario.nome = input("Informe o nome do usuário: ").strip().title()
    usuario.cpf = input("Informe o CPF do usuário: ").strip()
    usuario.profissao = input("Informe a profissão do usuário: ").strip()
    usuario.email = input("Informe o e-mail do usuário: ").strip().lower()
    usuario.telefone = input("Informe o telefone do usuário: ").strip()
    usuario.endereco = input("Informe o endereço do usuário: ").strip().title()

    print("Informe os dados da empresa: \n")
    empresa.razao_social = input("Informe razão social da empresa: ").strip().title()
    empresa.nome_fantasia = input("Informe o nome fantasia da empresa: ").strip()
    empresa.cnpj = input("Informe o CNPJ da empresa: ").strip()
    empresa.email = input("Informe o e-mail da empresa: ").strip().lower()
    empresa.telefone = input("Informe o telefone da empresa: ").strip()
    empresa.endereco = input("Informe o endereço da empresa: ").strip().title()

    # limpar a tela
    limpar()

    # saida de dados
    print(f"{'-'*20} DADOS DO USUÁRIO {'-'*20}")
    print(usuario)
    print(f"{'-'*60}")
    print(f"{'-'*20} DADOS DA EMPRESA {'-'*20}")
    print(empresa)