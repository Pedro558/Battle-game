from src.models.heroi import Heroi
from src.models.inimigo import Inimigo

class Jogo:
  """Classe orquestradora do jogo"""
  def __init__(self) -> None:
    self.heroi = Heroi("Hercules", 100, 5, "Força")
    self.inimigo = Inimigo("Minotauro", 80, 2, "Besta")
  
  def iniciar_batalha(self):
    print("Hello")
    """Gestão da batalha em turnos"""
    while self.heroi.vida > 0 and self.inimigo.vida > 0:
      print("\nDetalhes dos personagens:")
      print(self.heroi.exibir_detalhes())
      print(self.inimigo.exibir_detalhes())

      input("\nPressione Enter para atacar...")
      escolha = input("Escolha o ataque: 1 - Ataque normal, 2 - Ataque especial: ")

      if escolha == "1":
        self.heroi.atacar(self.inimigo)
      elif escolha == "2":
        self.heroi.ataque_especial(self.inimigo)
      else:
        print("Escolha inválida, escolha novamente")

      if self.inimigo.vida > 0:
        # inimigo ataca herói
        self.inimigo.atacar(self.heroi)
    
    if self.heroi.vida > 0:
      print(f"{self.heroi.nome} venceu a batalha!")
    else:
      print(f"{self.inimigo.nome} venceu a batalha!")

      