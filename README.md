# Battle Game

This is a Python-based turn-based battle game where a hero battles against an enemy. The game is designed with an object-oriented approach, featuring classes for characters, enemies, and the game controller. It was used modularization too.

## Features


- **Hero and Enemy Classes**: The game includes a `Heroi` class and an `Inimigo` class, both inheriting from a base `Personagem` class.
- **Turn-Based Combat**: Players can choose between normal and special attacks during their turn.
- **Dynamic Damage Calculation**: Damage is calculated based on the character's level and attack type.
- **Battle Outcome**: The game determines the winner based on the remaining health of the characters.

### Key Components

#### `Personagem` (Base Class)
- **Attributes**: `nome`, `vida`, `nivel`
- **Methods**:
  - `atacar(alvo)`: Performs a normal attack on the target.
  - `receber_ataque(dano)`: Reduces health based on the damage received.
  - `exibir_detalhes()`: Displays character details.

#### `Heroi` (Hero Class)
- Inherits from `Personagem`.
- **Additional Attribute**: `habilidade` (special skill).
- **Methods**:
  - `ataque_especial(alvo)`: Performs a special attack with higher damage.

#### `Inimigo` (Enemy Class)
- Inherits from `Personagem`.
- **Additional Attribute**: `tipo` (enemy type).
- **Methods**:
  - `exibir_detalhes()`: Displays enemy details, including type.

#### `Jogo` (Game Controller)
- Manages the game flow, including turn-based combat and battle outcomes.

## How to Run

1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd <repository-folder>

2. Run the game:
    ```bash
    python main.py

## Example Gameplay
- The game displays the hero and enemy details.
- The player chooses between a normal or special attack.
- The battle continues in turns until one character's health reaches zero.
- The winner is announced at the end.