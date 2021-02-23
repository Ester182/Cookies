from usuário import*
from time import sleep

cabecalho('LOGIN')

usuario = Usuario()
usuario.confirmarLogin()

cabecalho('INFORMAÇÕES PESSOAIS')

cliente = Cliente()
cliente.Pedido(PedidoCliente)
endereço = Endereco()
print( )

cliente.AtualizarPerfil()
endereço.ConsultarLocal()

print( )
print('--- Perfil Atualizado com sucesso')
print( )
cabecalho('LOCALIZAÇÃO')

pedidoCliente = PedidoCliente()
pedidoCliente.VerLocal()

cabecalho('Cardápio')
menu([c.saborMassa, c2.saborMassa, c3.saborMassa, c4.saborMassa])
print('Preço único: R$ 10,00')
print(linha())
print('Preço fixo de entrega: R$ 5,00')
print(linha())
print()

opc = int(input('Qual sabor deseja? '))
print()
sleep(0.5)
if opc ==1:

  c.Exibir1()
  envio = Envio()
  envio.en()
if opc ==2:

  c2.Exibir1()
  envio = Envio()
  envio.en()
if opc ==3:

  c3.Exibir1()
  envio = Envio()
  envio.en()
if opc ==4:

  c4.Exibir1()
  envio = Envio()
  envio.en()      