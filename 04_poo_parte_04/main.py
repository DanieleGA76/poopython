# biblioteca
import random
# classe
class Pessoa:
    # construtor
    def __init__(self, nome, email, profissao, humor):
        self.nome = nome
        self.email = email
        self.profissao = profissao
        self.humor = humor

    # métodos
    def dar_boas_vindas(self):
        return "Boa tarde!"
    
    def cumprimentar(self):
        return f"Olá, eu me chamo {self.nome}. É um prazer!"
    
    def perguntar(self):
        return f"Qual o seu nome?"
    
    def cartao_de_visitas(self):
        print(f"Nome: {self.nome}")
        print(f"E-mail {self.email}")
        print(f"Profissão: {self.profissao}")
    
    def ofernder(self):
        return f"Que liga? Me erra! vai ver se eu tò na esquina!"
    
# algoritmo principal
if __name__ == "__main__":
    #instancia de dois objetos
    usuario_masculino = Pessoa("", "", "", bool(random.getrandbits(1)))
    usuario_feminina = Pessoa("", "", "", bool(random.getrandbits(1)))

   
    # setas os valores dos atributos do objeto masculino
    usuario_masculino.nome = input("Informe seu nome: ").title().strip()
    usuario_masculino.email = input("Informe seu e-mail: ").lower().strip()
    usuario_masculino.profissao = input("Informe sua profissão: ").strip()
    
    # setas os valores dos atributos do objeto masculino
    usuario_feminina.nome = input("Informe seu nome: ").title().strip()
    usuario_feminina.email = input("Informe seu e-mail: ").lower().strip()
    usuario_feminina.profissao = input("Informe sua profissão: ").strip()

    # conversar
    print(f"Homem: - {usuario_masculino.dar_boas_vindas()}")
    print(f"Mulher: - {usuario_feminina.dar_boas_vindas()}")
    print(f"Homem: - {usuario_masculino.perguntar()}")
    if usuario_feminina.humor is True:
        print(f"Mulher: - {usuario_feminina.cumprimentar()}")
        print(f"Mulher: - {usuario_feminina.perguntar()}")
        usuario_masculino.humor = usuario_feminina.humor
        print(f"Homem: - {usuario_masculino.cumprimentar()}")
        print("Segue meu cartão de visitas: ")
        print(usuario_masculino.cartao_de_visitas())
    else:
        print(f"Mulher: - {usuario_feminina.ofernder()}")
        usuario_masculino.humor = usuario_feminina.humor
        print(f"Homem: bom humor = {usuario_masculino.humor}")