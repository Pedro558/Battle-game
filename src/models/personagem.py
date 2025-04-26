class Personagem:
  def __init__(self, nome: str, vida: int, nivel: int):
    try:
      if not isinstance(nome, str) or not isinstance(vida, int) or not isinstance(nivel, int):
        raise TypeError("Tipos inválidos: 'nome' deve ser string, 'vida' e 'nivel' devem ser inteiros.")
    except TypeError as e:
      print(f"Erro: {e}")
      raise

    self.__nome = nome
    self.__vida = vida
    self.__nivel = nivel

  @property
  def nome(self):
    return self.__nome
  
  @property
  def vida(self):
    return self.__vida
  
  @property
  def nivel(self):
    return self.__nivel
  
  def exibir_detalhes(self):
    return f"\nNome: {self.__nome}\nVida: {self.__vida}\nNível: {self.__nivel}"