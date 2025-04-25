# Personagem: classe pai
# Heroi: classe filha
# Inimigo: adversario do usuário
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
  
class Heroi(Personagem):
  def __init__(self, nome: str, vida: int, nivel: int, habilidade: str):

    super().__init__(nome,vida,nivel)

    try:
      if not isinstance(habilidade, str):
        raise TypeError("Tipo inválido: 'habilidade' deve ser string.")
    except TypeError as e:
      print(f"Erro: {e}")
      raise
    
    self.__habilidade = habilidade

  @property
  def habilidade(self):
    return self.__habilidade
  
  def exibir_detalhes(self):
    return f"{super().exibir_detalhes()}\nHabilidade: {self.__habilidade}"

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

  
heroi = Heroi("Hercules", 100, 1, "Força")
print(heroi.exibir_detalhes())
inimigo = Inimigo("Minotauro", 80, 2, "Besta")
print(inimigo.exibir_detalhes())