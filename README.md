# Projekt - Scraping výsledků voleb

## Instalace

1. Vytvořte virtuální prostředí:
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

## Použití

Spusťte skript s následujícími argumenty:

```bash
python projekt_3.py "<url>" "<výstupní_soubor.csv>"