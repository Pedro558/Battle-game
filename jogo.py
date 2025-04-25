class Personagem:
  def __init__(self, nome, vida, nivel):
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

  
personagem1 = Personagem("Heroi", 100, 1)
print(f"Nome: {personagem1.nome}, Vida: {personagem1.vida}, Nivel: {personagem1.nivel}")