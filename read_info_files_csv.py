import pandas as pd


if __name__ == "__main__":
    # Ścieżka do pliku CSV
    file_path = 'data/sprawdzone-nadcisnienie-wywiad/001_004/001_004/001_004_online.csv'

    # Wczytanie danych z pliku CSV do DataFrame
    df = pd.read_csv(file_path, sep=';', encoding='utf-8')

    # Wyświetlenie wczytanych danych
    print(df.info())
    print(df.to_markdown())

