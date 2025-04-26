from Game.models.heroi import Heroi
from Game.models.inimigo import Inimigo
  
heroi = Heroi("Hercules", 100, 1, "Força")
print(heroi.exibir_detalhes())
inimigo = Inimigo("Minotauro", 80, 2, "Besta")
print(inimigo.exibir_detalhes())