import os 
def nome_app():
    print("EATFY\n")

def opcoes():
    print('1. Cadastrar restaurante')
    print('2. Listar restaurante')
    print('3. Ativar restaurante')
    print('4 Sair\n')

def Finalizar_App():
    os.system('cls')
    print('Aplicativo Encerrado!\n')

def opcao_invalida():
    print('Opção Invalida!\n')
    input('Aperte qualquer tecla para voltar ao inicio do programa: ')
    main()


#print(f'Você escolheu a opção {opcao_escolhida}')

def opcao_escolhida():
    try:
        opcao_escolhida = int(input('Digite a opcao escolhida '))
        if opcao_escolhida == 1:
            print('Cadastro de Restaurantes: ')

        elif opcao_escolhida == 2:
            print('Lista de Restaurantes: ')
        elif opcao_escolhida == 3:
            print('Restaurantes ativados')
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
