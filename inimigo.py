from personagem import Personagem

class Inimigo(Personagem):
  def __init__(self, nome: str, vida: int, nivel: int, tipo: str):
    super().__init__(nome,vida,nivel)

    try:
      if not isinstance(tipo,str):
        raise TypeError("Tipo inválido: 'tipo' do inimigo deve ser uma string")
    except TypeError as e:
      print(f"Erro: {e}")
      raise
      
    self.__tipo = tipo

  def exibir_detalhes(self):
    return f"{super().exibir_detalhes()}\nTipo: {self.__tipo}"
