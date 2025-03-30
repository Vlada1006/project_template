import pandas as pd

def read_text_from_console():
    """Функція для вводу тексту з консолі."""
    return input("Введіть текст: ")

def read_text_from_file(filepath):
    """Функція для зчитування тексту з файлу."""
    try:
        with open(filepath, "r", encoding="utf-8") as file:
            return file.read()
    except FileNotFoundError:
        return f"Файл {filepath} не знайдено."

def read_text_with_pandas(filepath):
    """Функція для зчитування текстових даних з файлу за допомогою pandas."""
    try:
        df = pd.read_csv(filepath, encoding="utf-8")
        return df.to_string()  # Перетворюємо DataFrame у текст
    except FileNotFoundError:
        return f"Файл {filepath} не знайдено."
    except pd.errors.EmptyDataError:
        return f"Файл {filepath} порожній або має неправильний формат."
