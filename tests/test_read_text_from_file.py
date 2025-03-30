import unittest
import os
from app.io.input import read_text_from_file

class TestReadTextFromFile(unittest.TestCase):

    def setUp(self):
        """Створюємо тестовий файл перед тестами."""
        with open("test_input.txt", "w", encoding="utf-8") as f:
            f.write("Це тестовий файл для перевірки.")

    def tearDown(self):
        """Видаляємо тестовий файл після тестів."""
        os.remove("test_input.txt")

    def test_read_text_from_file_existing(self):
        """Тест зчитування існуючого файлу."""
        self.assertEqual(read_text_from_file("test_input.txt"), "Це тестовий файл для перевірки.")

    def test_read_text_from_file_missing(self):
        """Тест зчитування неіснуючого файлу."""
        self.assertEqual(read_text_from_file("missing.txt"), "Файл missing.txt не знайдено.")

    def test_read_text_from_file_empty(self):
        """Тест зчитування порожнього файлу."""
        with open("empty.txt", "w", encoding="utf-8") as f:
            f.write("")
        self.assertEqual(read_text_from_file("empty.txt"), "")
        os.remove("empty.txt")

if __name__ == "__main__":
    unittest.main()
