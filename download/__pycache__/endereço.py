class Endereco:
  def __init__(self):
    self._estado = input('Diga o nome do seu estado: ')
    self._cidade = input('Diga o nome da sua cidade: ')

  def ConsultarLocal(self):
    print(self._cidade, '-', self._estado)