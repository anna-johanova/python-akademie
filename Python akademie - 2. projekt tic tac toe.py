"""
projekt_2.py: Druhý projekt do Engeto Online Python Akademie
Autor: Anna Johanová
Email: a.johanova@seznam.cz
Discord: annajohanova_75116
"""

# Definice funkcí

def zobraz_desku(deska):
    """Vytiskne aktuální stav hrací desky."""
    print("\n+---+---+---+")
    for i in range(3):
        print(f"| {deska[i * 3]} | {deska[i * 3 + 1]} | {deska[i * 3 + 2]} |")
        print("+---+---+---+")

def zkontroluj_vitezstvi(deska, znak):
    """Zkontroluje, zda hráč s daným znakem vyhrál."""
    vyherni_kombinace = [
        # Horizontální
        (0, 1, 2),
        (3, 4, 5),
        (6, 7, 8),
        # Vertikální
        (0, 3, 6),
        (1, 4, 7),
        (2, 5, 8),
        # Diagonální
        (0, 4, 8),
        (2, 4, 6)
    ]
    # Zkontrolujeme, zda některá z vítězných kombinací není plně obsazena jedním znakem
    for kombinace in vyherni_kombinace:
        if all(deska[i] == znak for i in kombinace):
            return True
    return False

def zkontroluj_remizu(deska):
    """Zkontroluje, zda došlo k remíze (všechna pole jsou obsazená)."""
    return all(pole in ['X', 'O'] for pole in deska)

def hlavni():
    # Úvodní přivítání a pravidla hry
    print("Welcome to Tic Tac Toe")
    print("=" * 40)
    print("GAME RULES:")
    print("Each player can place one mark (or stone)")
    print("per turn on the 3x3 grid. The WINNER is")
    print("who succeeds in placing three of their")
    print("marks in a:")
    print("* horizontal,")
    print("* vertical or")
    print("* diagonal row")
    print("=" * 40)
    print("Let's start the game")

    # Inicializace prázdné hrací desky
    deska = [' ' for _ in range(9)]
    aktualni_hrac = 'O'
    zbyvajici_tahy = 9

    while True:
        # Zobrazíme aktuální stav desky
        zobraz_desku(deska)
        print(f"Player {aktualni_hrac} | Please enter your move number:", end=" ")

        # Zpracování tahu
        try:
            tah = int(input().strip())
            if tah < 1 or tah > 9:
                print("Invalid move. | Please enter your move number between 1 and 9.")
                continue
        except ValueError:
            print("Invalid enter. Please enter your move number between 1 and 9.")
            continue

        # Kontrola, zda je pole volné
        index = tah - 1
        if deska[index] != ' ':
            print("The selected field is already occupied. Select another field.")
            continue

        # Provést tah
        deska[index] = aktualni_hrac
        zbyvajici_tahy -= 1

        # Kontrola vítězství
        if zkontroluj_vitezstvi(deska, aktualni_hrac):
            zobraz_desku(deska)
            print(f"Congratulations, the player {aktualni_hrac} WON!")
            break

        # Kontrola remízy
        if zbyvajici_tahy == 0:
            zobraz_desku(deska)
            print("It's a tie!")
            break

        # Přepnutí hráčů
        aktualni_hrac = 'X' if aktualni_hrac == 'O' else 'O'

if __name__ == "__main__":
    hlavni()