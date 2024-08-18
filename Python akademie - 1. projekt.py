
# Na úvod si svůj soubor 
# popiš hlavičkou, ať se s tebou můžeme snadněji spojit:

"""
projekt_1.py: první projekt do Engeto Online Python Akademie
author: Anna Johanová
email: a.johanova@seznam.cz
discord: annajohanova_75116
"""

import string

TEXTS = ['''
Situated about 10 miles west of Kemmerer,
Fossil Butte is a ruggedly impressive
topographic feature that rises sharply
some 1000 feet above Twin Creek Valley
to an elevation of more than 7500 feet
above sea level. The butte is located just
north of US 30N and the Union Pacific Railroad,
which traverse the valley. ''',
'''At the base of Fossil Butte are the bright
red, purple, yellow and gray beds of the Wasatch
Formation. Eroded portions of these horizontal
beds slope gradually upward from the valley floor
and steepen abruptly. Overlying them and extending
to the top of the butte are the much steeper
buff-to-white beds of the Green River Formation,
which are about 300 feet thick.''',
'''The monument contains 8198 acres and protects
a portion of the largest deposit of freshwater fish
fossils in the world. The richest fossil fish deposits
are found in multiple limestone layers, which lie some
100 feet below the top of the butte. The fossils
represent several varieties of perch, as well as
other freshwater genera and herring similar to those
in modern oceans. Other fish such as paddlefish,
garpike and stingray are also present.'''
]

# Vyžádá si od uživatele přihlašovací jméno a heslo

# databáze registrovaných uživatelů
uzivatele = {"bob": "pass", "ann": "pass123", "mike": "password123", "liz": "pass123"}

jmeno = input("user: ")
heslo = input("password: ")
cara = ("-" * 40)

# Podmínka pro umožnění vstupu uživatele, nebo ukončení programu
if jmeno in uzivatele and uzivatele[jmeno] == heslo:
    print(cara)
    print("Welcome to the app,", jmeno, ".")
else:
    print("unregistered user, terminating the program...")
    exit()
print("We have 3 texts to be analyzed.")
print(cara)

# Program nechá uživatele vybrat mezi třemi texty, uloženými v proměnné TEXTS

# Úprava textů pro další zpracování
text_1 = str(TEXTS[0])
text_2 = str(TEXTS[1])
text_3 = str(TEXTS[2])

# Input od uživatele, porovnání hodnot a přiřazení textu do vypsana_slova
while True:
    zadane_cislo = input("Enter a number btw. 1 and 3 to select: ")
    
    if zadane_cislo == "1":
        vypsana_slova = TEXTS[0].translate(str.maketrans('', '', string.punctuation)).split()
        print(cara)
        break
    elif zadane_cislo == "2":
        vypsana_slova = TEXTS[1].translate(str.maketrans('', '', string.punctuation)).split()
        print(cara)
        break
    elif zadane_cislo == "3":
        vypsana_slova = TEXTS[2].translate(str.maketrans('', '', string.punctuation)).split()
        print(cara)
        break
    elif zadane_cislo.isalpha():
        print("You did not enter a number. Terminating the program...")
        exit()
    else:
        print("Wrong number entered. Terminating the program...")
        exit()
         
# Pro vybraný text spočítá následující statistiky:

# Počet slov
print("There are ", len(vypsana_slova), " words in the selected text.")

# Výpočet počtu slov s velkým počatečním písmenem
titlecase_words = {}
for slovo in vypsana_slova:
    if slovo[0].isupper() and not any(char.isdigit() for char in slovo):
        titlecase_words[slovo] = titlecase_words.get(slovo, 0) + 1
print("There are ", len(titlecase_words), "titlecase words.")

# Počet slov psaných pouze velkými písmeny
uppercase_words = {}
for slovo in vypsana_slova:
    if slovo.isupper() and not any(char.isdigit() for char in slovo):
        uppercase_words[slovo] = uppercase_words.get(slovo, 0) + 1
print("There are ", len(uppercase_words), "uppercase words.")

# Počet slov psaných pouze malými písmeny
lowercase_words = {}
for slovo in vypsana_slova:
    if slovo.islower() and not any(char.isdigit() for char in slovo):
        lowercase_words[slovo] = lowercase_words.get(slovo, 0) + 1
print("There are ", len(lowercase_words), "lowercase words.")

# Počet slov, která obsahují číslo (bez '30N')
numeric_strings = {}
for slovo in vypsana_slova:
    if slovo.isdigit():  # Čistě číselné řetězce
        numeric_strings[slovo] = numeric_strings.get(slovo, 0) + 1
print("There are ", len(numeric_strings), " numeric strings.")

# Součet všech čísel
suma = 0
for slovo in vypsana_slova:
    if slovo.isdigit():  # Čistě číselné řetězce
        suma += int(slovo)
print("The sum of all the numbers: ", suma)

# Četnost různých délek slov v textu
pocet_vyskytu = {}
for slovo in vypsana_slova:
    delka = len(slovo)
    if delka not in pocet_vyskytu:
        pocet_vyskytu[delka] = 1
    else:
        pocet_vyskytu[delka] += 1

pocet_vyskytu_sorted = dict(sorted(pocet_vyskytu.items()))

# Vypíše tabulku
hlavicka_delka = "LEN"
hlavicka_hvezdicky = "OCCURENCES"
hlavicka_pocet = "NR."
print()
print(f"{hlavicka_delka:>6} | {hlavicka_hvezdicky:>15} | {hlavicka_pocet:>5}")

for delka_slova, pocet_slov in pocet_vyskytu_sorted.items():
    print(f"{delka_slova:>6} | {'*' * pocet_slov:>15} | {pocet_slov:>5}")