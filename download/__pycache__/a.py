#Curso:Técnico em Informática
#Disciplina:Programação Orientada a Objetos
#Turma:2°ano Informática Matutino
#Docente:Camila Serrão
#Discente:Ester Silva e Clauan Santos

from usuário import*
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
  except ValueError: #nome da exceçao
    print('Inteiro não valido! Tente novamente.')
    print('=-=' * 15)
    raise Exception('Este não é um número inteiro.')
  if opcao == 1:
    print('Vamos lá!')
    from c_sistema import*
    print('Fim da compra, seu pedido esta á caminho!')
    break
  elif opcao == 2:
    print('Finalizando...')
    sleep(1)
  else:
    print()
  print('Fim do programa, volte sempre!')
print('=-=' * 15)