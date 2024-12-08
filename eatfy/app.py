import os 

Restaurantes = [{'nome':'Sushi Alvim','categoria':'Japonesa','ativo':False},
                {'nome':'FinettoS','categoria':'Italiana','ativo': True},
                {'nome':'Comenalle','categoria':'Prato Feito','ativo':False}
]

def nome_app():
    print("EATFY\n")

def opcoes():
    print('1. Cadastrar restaurante')
    print('2. Listar restaurante')
    print('3. Alternar Status do Restaurante')
    print('4. Sair\n')

def Finalizar_App():
    subtitulos('Aplicativo Encerrado! ')

def voltar_menu():
    input('Digite qualquer tecla para voltar ao menu: ')
    main()

def opcao_invalida():
    print('Opção Invalida!\n')
    voltar_menu()

def subtitulos(texto_opcões):
    os.system('cls')
    print(f'{texto_opcões}\n')


def cadastrar_restaurante():
    subtitulos('Cadastros De Novos Restaurantes: ')
    Nome_Restaurante = input("Digite o Nome do Restaurante: ")
    categoria = input(f'Digite o nome da categoria do restaurante {Nome_Restaurante}: ')
    dados_restaurante = {'nome':Nome_Restaurante,'categoria':categoria,'ativo':False}
    Restaurantes.append(dados_restaurante)
    print(f'O restaurante {Nome_Restaurante} foi cadastrado com sucesso!\n')
    voltar_menu()

    
def Lista_Restaurantes():
     subtitulos('Restaurantes Cadastrados: ')
     contador = 0 
     for restaurantes in Restaurantes:
         contador += 1
         nome_restaurantes = restaurantes['nome']
         categoria = restaurantes['categoria']
         ativo = 'Ativado' if restaurantes['ativo'] else 'Desativado'
         print(f'{contador}. {nome_restaurantes.ljust(20)} | {categoria.ljust(20)} | {ativo}\n')    

     voltar_menu()


def status_restaurante():
    subtitulos('Alterar Status Restaurante')
    Nome_Restaurante = input('Digite o nome do Restaurante que deseja alterar o status: ')
    restaurante_localizado = False

    for restaurante in Restaurantes:
        if Nome_Restaurante == restaurante['nome']:
            restaurante_localizado = True
            restaurante['ativo'] = not restaurante['ativo']
            mensagem = f'O restaurante {Nome_Restaurante} foi ativado com sucesso' if restaurante ['ativo'] else f'O restaurante {Nome_Restaurante} foi desativado com sucesso'
            print(mensagem)
    if not restaurante_localizado:
        print('Restaurante não foi localizado!')

    voltar_menu()

def opcao_escolhida():
    try:
        opcao_escolhida = int(input('Digite a opcao escolhida '))
        if opcao_escolhida == 1:
            cadastrar_restaurante()

        elif opcao_escolhida == 2:
            Lista_Restaurantes()

        elif opcao_escolhida == 3:
            status_restaurante()
        elif opcao_escolhida == 4:
            Finalizar_App()
        else:
            opcao_invalida()

    except:
        opcao_invalida()

def main():
    os.system('cls')
    nome_app()
    opcoes()
    opcao_escolhida()


if __name__ == '__main__':
    main()
