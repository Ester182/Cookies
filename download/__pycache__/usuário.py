class Usuario:
  def __init__(self):
    self.emailUsuario = input('Email de Usuário: ')
    self.senha = input('Senha: ')

  def confirmarLogin(self):
      print( )
      print(self.emailUsuario, 'confirmou login')

from endereço import*

class Cliente(Usuario):
  def __init__(self):
    self._nomeCliente = input('Nome do Cliente: ')
    self._formaPagamento = input('Forma de Pagamento: ')
    self._PedidoCliente = None

  def Pedido(self, PedidoCliente):
     self._PedidoCliente = PedidoCliente

  def AtualizarPerfil(self):
    print(self._nomeCliente,'efetuará o pagamento no', self._formaPagamento)


class Administrador(Usuario):
  pass


class PedidoCliente:
  def __init__(self):
    self._numPedido = str('Número do pedido: 01')
    self._dataEnvio = input('Data da realização do pedido: ')
    self._Localizacaologradouro = input('Rua: ')
    self._Localizacaobairro = input('Bairro: ')
    self._LocalizacaonumReside = input('Número da Residência: ')
    self._Localizacaocomplemento = input("Complemento: ")
    self._numCliente = input('Insira um telefone para contato: ')

  def VerLocal(self):
    print( )
    print(self._numPedido)
    print('Rua: ',self._Localizacaologradouro,' - ',self._LocalizacaonumReside,' - ',self._Localizacaocomplemento)
    print('Bairro: ',self._Localizacaobairro)
    print( )

class Cookies:
  def __init__(self, sabor, valor):
    self.saborMassa = sabor
    self.valorMassa = valor

  def Exibir1(self):
    print('Entrega de um cookie de:',self.saborMassa,'no valor de R$',self.valorMassa,'mais R$ 5 de taxa de entrega.')
   
class Envio:
  def __init__(self):
    self.custoenvio = str('Custo do pedido: 15 reais')
    self.numenvio = str('Número de envio: 01')

  def en(self):
    print( )
    print(self.custoenvio)
    print(self.numenvio)

#estrutura do menu
def linha(tam=44):
    return '-' * tam

def cabecalho(txt):
    print(linha())
    print(txt.center(44))
    print(linha())


def menu(lista):
    c = 1
    for item in lista:
        print(f'{c}-{item}')
        c += 1
    print(linha())
#fim estrutura menu

c = Cookies('Chocolate com gotas de chocolate brancas','10')
c2= Cookies('Chocolate com gotas de chocolate pretas','10')
c3= Cookies('Baunilha com gotas de chocolate brancas','10')
c4= Cookies('Baunilha com gotas de chocolate pretas','10')

pedido= ['c','c2','c3','c4'] #coleção