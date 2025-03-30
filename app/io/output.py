def print_text_to_console(text):
    """Функція для виводу тексту у консоль."""
    print(text)

def write_text_to_file(filepath, text):
    """Функція для запису тексту у файл."""
    with open(filepath, "a", encoding="utf-8") as file:
        file.write(text + "\n")
