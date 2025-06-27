from classes import PessoaFisica, PessoaJuridica
import os

def limpar():
    os.system("cls" if os.name == "nt" else "clear")

if __name__ == "__main__":
    usuario = PessoaFisica(nome= "", Cpf= "", profissao= "", email="", telefone="")
    empresa = PessoaJuridica(razao_social="", nome_fantasia="", cnpj="", email="", telefone="")

print(f"{'-'*20} Dados do Usuário {'-'*20}")
usuario.name = input("Informe o nome: ").title().strip()
usuario.cpf = input("Informe o CPF: ").strip()
usuario.profissao = input("Informe a profissão: ").strip()
usuario.email = input("Informe o e-mail: ").lower().strip()
usuario.telefone = input("Informe o telefone: ").strip()

limpar()

print(f"{'-'*20} Dados da empresa {'-'*20}")
empresa.razao_social = input("informe a razão social: ").title().strip()
empresa.nome_fantasia = input("informe o nome fantasia: ").title().strip()
empresa.cnpj = input("informe o cnpj: ").strip()
empresa.email = input("informe o email: ").lower().strip()
empresa.telefone = input("informe telefone: ").strip()

limpar()

print(f"{'-'*20} Dados do usuario {'-'*20}")
print(f"Nome: {usuario.nome}")
print(f"CPF: {usuario.cpf}")
print(f"profissão: {usuario.profissao}")
print(f"E-mail: {usuario.email}")
print(f"Telefone: {usuario.telefone}")

print(f"{'-'*20} Dados da Empresa {'-'*20}")
print(f"Razão Social: {empresa.razao_social}")
print(f"Nome Fantasia: {empresa.nome_fantasia}")
print(f"CNPJ: {empresa.cnpj}")
print(f"E-mail: {empresa.email}")
print(f"Telefone: {empresa.telefone}")
