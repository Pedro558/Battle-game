from src.models.personagem import Personagem
import random
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
  
  def ataque_especial(self, alvo):
    dano = random.randint(self.nivel * 5, self.nivel * 8)
    alvo.receber_ataque(dano)
    print(f"{self.nome} atacou {alvo.nome} e causou {dano} de dano!")