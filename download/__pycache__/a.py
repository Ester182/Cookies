#Curso:Técnico em Informática
#Disciplina:Programação Orientada a Objetos
#Turma:2°ano Informática Matutino
#Docente:Camila Serrão
#Discente:Ester Silva e Clauan Santos

from usuário import*
from time import sleep

email = []
senha = []
while 1:
    cabecalho('Tela inicial')
    menu(['Cadastrar', 'Fazer login'])
    opi = int(input('Digite a opção que deseja.: '))
    print(linha())
    if opi == 1:
        em = str(input('Digite seu email.: '))
        sh = str(input('Agora, digite sua senha.: '))
        email.append(em)
        senha.append(sh)
        print('Cadastro realizado com sucesso. Aguarde.')
        sleep(1.5)
    if opi == 2:
        em1 = str(input('Digite seu email.: '))
        sh1 = str(input('Agora digite sua senha.: '))
        em = email[0]
        sh = senha[0]

        if em1 == em and sh1 == sh:
            print(linha())
            print('Login realizado com sucesso. Aguarde.')
            sleep(2)
            from time import sleep

            cabecalho('MENU')
            print('Seja bem vindo ao programa, que opção deseja?')
            opcao = 0
            while opcao != 2:
                print('''  [1] Fazer meu pedido
              [2] Sair do programa''')
                try:
                    opcao = input('Insira um número inteiro: ')
                    opcao = int(opcao)
                except ValueError:  # nome da exceçao
                    print('Inteiro não valido! Tente novamente.')
                    print('=-=' * 15)
                    raise Exception('Este não é um número inteiro.')
                if opcao == 1:
                    print('Vamos lá!')
                    from c_sistema import *

                    print('Fim da compra, seu pedido esta á caminho!')
                    break
                elif opcao == 2:
                    print('Finalizando...')
                    sleep(1)
                else:
                    print()
                print('Fim do programa, volte sempre!')
            print('=-=' * 15)
            break
        elif em1 != em:
            print('Email incorreto')
            sleep(3)

        elif sh1 != sh:
            print('Senha incorreta')
            sleep(3)
        break
