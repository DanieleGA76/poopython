# Biblioteca
import classe
# algoritmo principal
if __name__ == "__main__":
    # instancia o classe filho
    Filho = classe.Filho("", "", "", "", 0.0, 0.0)

    try:

        Filho.nome = input("Informe o nome: ").strip().title()
        Filho.email = input("Informe o e-mail: ").strip().lower()
        Filho.telefone = input("Informe o telefone: ").strip()
        Filho.genero = input("Informe o gênero: ").strip().title()
        Filho.peso = float(input("Informe o peso em kg: ").replace(",", "."))
        Filho.altura = float(input("Informe a altura em mêtros: ").replace(",", "."))

        # atributo
        Filho.exibir_info()
    except Exception as e:
        print(f"Não foi possível executar. {e}.")