# Requisito 12
def switch_options(option):
    if option == 1:
        input("Digite o título:")
    elif option == 2:
        input("Digite a data no formato aaaa-mm-dd:")
    elif option == 3:
        print("Digite a tag:")
    elif option == 4:
        print("Digite a categoria:")
    else:
        print("Opção inválida")


def analyzer_menu():
    option = input("""
    Selecione uma das opções a seguir:
    0 - Popular o banco com notícias;
    1 - Buscar notícias por título;
    2 - Buscar notícias por data;
    3 - Buscar notícias por tag;
    4 - Buscar notícias por categoria;
    5 - Listar top 5 notícias;
    6 - Listar top 5 categorias;
    7 - Sair.
    """)

    if option == 0:
        input("Digite quantas notícias serão buscadas:")
    switch_options(option)
