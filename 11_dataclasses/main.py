from classes import Pessoa

if __name__ == "__main__":
    usuario = Pessoa(
        nome= "",
        idade= 0,
        email= "",
        telefone= "",
        profissao= "",
        peso= 0.0,
        altura= 0.0
    )

    usuario.nome = "Fulano"
    usuario.idade = 18
    usuario.email = "fulano2gmail.com"
    usuario.telefone = "(61) 98765-4321"
    usuario.profissao = "programador"
    usuario.peso = 100
    usuario.altura = 1.05

    print(f"{usuario}, tenho {len(usuario)} anos. Seque meus dados: ")
    print(f"Nome: {usuario.nome}")
    print(f"Idade: {usuario.idade}")
    print(f"E-mail: {usuario.email}")
    print(f"Telefone: {usuario.telefone}")
    print(f"Profissão: {usuario.profissao}")
    print(f"Peso: {usuario.peso}")
    print(f"Altura: {usuario.altura}")