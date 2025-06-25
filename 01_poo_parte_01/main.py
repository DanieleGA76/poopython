# Classes
class Pessoa:
    # atributos
    nome = "Alex Machado"
    idade = 40
    email = "alex@gmail.com"
    profissao = "programdor"

 # algoritmo principal
if __name__ == "__main__":
        # instancia a classe Pessoa (cria objeto da classe)
        usuario = Pessoa()

         # exibi na tela os dados do usuario
        print(f"Nome: {usuario.nome}.")
        print(f"idade: {usuario.idade}.")
        print(f"E-mail: {usuario.email}.")
        print(f"Profissâo: {usuario.profissao}.")
