# Python Akademie - 3. projekt: Web Scraping

## Popis
Tento projekt je třetím úkolem v rámci Python Akademie od Engeto Online Python Academy. Cílem projektu je vytvořit web scraper, který shromažďuje výsledky voleb z veřejně dostupné webové stránky a ukládá je do CSV souboru.

## Pro spuštění skriptu

1. Vytvořte virtuální prostředí v příkazovém řádku:
    ```bash
    python -m venv venv
    ```

2. Aktivujte virtuální prostředí:
    - Na Windows:
        ```bash
        venv\Scripts\activate
        ```
    - Na macOS/Linux:
        ```bash
        source venv/bin/activate
        ```

3. Nainstalujte knihovny:
    ```bash
    pip install -r requirements.txt
    ```

## Funkcionalita
Skript provádí následující úkoly:
1. Ověření platnosti zadané URL adresy.
2. Získání URL jednotlivých měst ze zadané stránky.
3. Scraping názvů měst a jejich kódů.
4. Shromáždění údajů o volební účasti, počtu hlasovacích lístků a platných hlasech.
5. Získání názvů politických stran a jejich hlasů z jednotlivých městských stránek.
6. Uložení všech shromážděných dat do CSV souboru.

## Použití
Chcete-li spustit skript, použijte následující příkaz v příkazovém řádku:
```bash
python projekt_3.py <URL> <název_souboru.csv>
```
Kde:

<URL> je URL adresa stránky obsahující výsledky voleb.
<název_souboru.csv> je název CSV souboru, do kterého budou uložena data.

## Příklad:
```bash
python projekt_3.py https://volby.cz/pls/ps2017nss/ps32?xjazyk=CZ&xkraj=2&xnumnuts=2109" "výsledky_volby_PHA-vychod.csv"
```
# Požadavky
Skript vyžaduje následující Python knihovny:

1. <b>requests
2. beautifulsoup4
3. argparse (ve verzi Python 3 a vyšší automaticky k dispozici)
4. csv (ve verzi Python 3 a vyšší automaticky k dispozici)</b>

Tyto knihovny (requests a beautifulsoup4) můžete nainstalovat pomocí pip:

```bash
pip install requests beautifulsoup4
```

## Další informace
Pokud máte jakékoliv dotazy nebo potřebujete pomoc, neváhejte mě kontaktovat na uvedeném e-mailu nebo Discordu.