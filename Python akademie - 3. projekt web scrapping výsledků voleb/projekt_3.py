"""
projekt_3.py: Third project for Engeto Online Python Academy
author: Anna Johanová
email: a.johanova@seznam.cz
discord: annajohanova_75116
"""

from bs4 import BeautifulSoup
import requests
import argparse
import csv


def validate_url(url: str) -> bool:
    """
    Ověření platnosti URL adresy pomocí knihovny requests.

    :param url: URL adresa, kterou chceme ověřit.
    :return: True, pokud je URL platná a server vrátí status kód 200, jinak False.
    """
    try:
        response = requests.get(url)
        return response.status_code == 200
    except requests.exceptions.RequestException:
        return False


def validate_command_line_arguments() -> tuple:
    """
    Funkce pro ověření argumentů příkazové řádky.

    :return: Tupl (url, file_name) pokud jsou argumenty platné.
    :raises ValueError: Pokud argumenty nejsou platné.
    """
    parser = argparse.ArgumentParser(description="Scraper výsledků voleb.")
    parser.add_argument("url", type=str, help="URL pro scrapování výsledků voleb.")
    parser.add_argument("file_name", type=str, help="Název výstupního CSV souboru.")
    args = parser.parse_args()
    url, file_name = args.url, args.file_name

    # Ověření URL
    if not url.startswith("https://volby.cz/pls/ps2017nss/"):
        raise ValueError("URL musí začínat s 'https://volby.cz/pls/ps2017nss/'.")

    # Ověření přípony souboru
    if not file_name.endswith(".csv"):
        raise ValueError("Soubor musí mít příponu '.csv'.")

    # Ověření, zda je URL platná
    if not validate_url(url):
        raise ValueError("Neplatná URL: " + url)

    return url, file_name


def get_city_urls(url: str) -> list[str]:
    """
    Funkce pro získání individuálních URL pro jednotlivá města.

    :param url: URL stránky, kde hledáme odkazy na města.
    :return: Seznam URL jednotlivých měst.
    """
    response = requests.get(url)
    doc = BeautifulSoup(response.text, "html.parser")
    city_urls = []

    # Získání všech odkazů, které obsahují 'xobec='
    for a in doc.find_all("a", href=True):
        if "xobec=" in a["href"]:
            full_url = "https://volby.cz/pls/ps2017nss/" + a["href"]
            if full_url not in city_urls:
                city_urls.append(full_url)

    return city_urls


def city_names_scraper(url: str) -> tuple[list[str], list[str]]:
    """
    Funkce pro získání názvů měst a jejich kódů z URL.

    :param url: URL stránky obsahující seznam měst a jejich kódů.
    :return: Tupl obsahující dva seznamy: první seznam obsahuje kódy měst a druhý seznam obsahuje názvy měst.
    """
    response = requests.get(url)
    response.raise_for_status()  # Zajistí, že HTTP požadavek proběhl úspěšně
    doc = BeautifulSoup(response.text, "html.parser")

    # Získání kódů měst
    city_codes = [code.text.strip() for code in doc.find_all("td", class_="cislo")]

    # Získání názvů měst
    city_names = [name.text.strip() for name in doc.find_all("td", class_="overflow_name")]

    return city_codes, city_names


def voter_turnout_data(city_urls: list[str]) -> list[list[str]]:
    """
    Funkce pro získání údajů o volební účasti z adres URL měst.

    :param city_urls: Seznam URL adres městských stránek s údaji o volební účasti.
    :return: Seznam obsahující tři seznamy: registrovaní voliči, hlasovací lístky a platné hlasy.
    """
    registered_voters = []
    ballot_papers = []
    valid_votes = []

    for url in city_urls:
        response = requests.get(url)
        response.raise_for_status()  # Zajistí, že HTTP požadavek proběhl úspěšně
        doc = BeautifulSoup(response.text, "html.parser")

        # Získání údajů o registrovaných voličích
        registered_voters.extend(
            item.text.replace("\xa0", "").strip() for item in doc.find_all("td", class_="cislo", headers="sa2")
        )

        # Získání údajů o hlasovacích lístcích
        ballot_papers.extend(
            item.text.replace("\xa0", "").strip() for item in doc.find_all("td", class_="cislo", headers="sa3")
        )

        # Získání údajů o platných hlasech
        valid_votes.extend(
            item.text.replace("\xa0", "").strip() for item in doc.find_all("td", class_="cislo", headers="sa6")
        )

    return [registered_voters, ballot_papers, valid_votes]


def get_political_parties(city_urls: list[str]) -> list[str]:
    """
    Funkce pro získání názvů politických stran z URL stránek měst.

    :param city_urls: Seznam URL adres městských stránek obsahujících názvy politických stran.
    :return: Seznam názvů politických stran.
    """
    if not city_urls:
        raise ValueError("Seznam URL je prázdný.")

    political_parties = []

    for url in city_urls:
        response = requests.get(url)
        response.raise_for_status()  # Zajistí, že HTTP požadavek proběhl úspěšně
        doc = BeautifulSoup(response.text, "html.parser")

        # Získání názvů politických stran z prvního a druhého stolu
        table1 = [
            item.text.replace("\xa0", "").strip() for item in
            doc.find_all("td", class_="overflow_name", headers="t1sa1 t1sb2")
        ]
        table2 = [
            item.text.replace("\xa0", "").strip() for item in
            doc.find_all("td", class_="overflow_name", headers="t2sa1 t2sb2")
        ]

        political_parties.extend(table1 + table2)

    return political_parties


def get_votes(city_urls: list) -> list:
    """Funkce pro získání volebních dat z jednotlivých stránek měst."""
    total_votes = []
    for url in city_urls:
        response = requests.get(url)
        doc = BeautifulSoup(response.text, "html.parser")
        table1 = [
            j.text.replace("\xa0", "").strip() for j in doc.find_all("td", class_="cislo", headers="t1sa2 t1sb3")
        ]
        table2 = [
            j.text.replace("\xa0", "").strip() for j in doc.find_all("td", class_="cislo", headers="t2sa2 t2sb3")
        ]
        total_votes.append(table1 + table2)
    return total_votes


def write_csv(file_name, city_codes, city_names, data_collection, political_parties, total_votes) -> None:
    """Funkce pro zapsání dat do CSV souboru."""
    print(f"Zápis do souboru {file_name}...")  # Ladící výstup
    head = [
        "Kód obce",
        "Název obce",
        "Voliči v seznamu",
        "Vydané obálky",
        "Platné hlasy",
    ]
    with open(file_name, "w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(head + political_parties)
        for i in range(len(city_codes)):
            writer.writerow(
                [city_codes[i], city_names[i]]
                + [data_collection[0][i]]
                + [data_collection[1][i]]
                + [data_collection[2][i]]
                + total_votes[i]
            )
    print(f"Soubor {file_name} byl úspěšně vytvořen.")


def main() -> None:
    """Hlavní skript programu pro sběr a zápis volebních dat."""
    try:
        # Ověření a načtení argumentů příkazového řádku
        url, file_name = validate_command_line_arguments()
        print(f'Inicializace programu skrz URL "{url}" a jméno souboru "{file_name}"\nZískávám data...')

        # Získání názvů měst a jejich kódů
        city_codes, city_names = city_names_scraper(url)

        # Získání URL adres pro jednotlivá města
        city_urls = get_city_urls(url)
        if not city_urls:
            raise ValueError("Seznam URL městských stránek je prázdný.")

        # Získání údajů o volební účasti, politických stranách a volebních datech
        data_collection = voter_turnout_data(city_urls)
        political_parties = get_political_parties(city_urls)
        total_votes = get_votes(city_urls)

        # Zápis dat do CSV souboru
        write_csv(
            file_name, city_codes, city_names, data_collection, political_parties, total_votes
        )
        print(f"Soubor {file_name} byl úspěšně vytvořen.")

    except ValueError as error:
        print(f"Chyba: {error}")
    except requests.exceptions.RequestException as e:
        print(f"Chyba při HTTP požadavku: {e}")
    except Exception as e:
        print(f"Neočekávaná chyba: {e}")


if __name__ == "__main__":
    main()