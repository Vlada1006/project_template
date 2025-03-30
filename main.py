from app.io.input import read_text_from_console, read_text_from_file, read_text_with_pandas
from app.io.output import print_text_to_console, write_text_to_file

def main():
    text_from_console = read_text_from_console()

    text_from_file = read_text_from_file("data/input.txt")

    text_with_pandas = read_text_with_pandas("data/data.csv")

    print_text_to_console("Текст із консолі:")
    print_text_to_console(text_from_console)

    print_text_to_console("\nТекст із файлу:")
    print_text_to_console(text_from_file)

    print_text_to_console("\nТекст із файлу (через pandas):")
    print_text_to_console(text_with_pandas)

    write_text_to_file("output.txt", "Текст із консолі:\n" + text_from_console)
    write_text_to_file("output.txt", "\nТекст із файлу:\n" + text_from_file)
    write_text_to_file("output.txt", "\nТекст із файлу (через pandas):\n" + text_with_pandas)

if __name__ == "__main__":
    main()
