import unittest
import os
from app.io.input import read_text_with_pandas

class TestReadTextWithPandas(unittest.TestCase):

    def setUp(self):
        """Створюємо тестові CSV файли перед тестами."""
        with open("empty.csv", "w", encoding="utf-8") as f:
            f.write("")

        with open("test_data.csv", "w", encoding="utf-8") as f:
            f.write("name,age\nJohn,25\nAlice,30")

    def tearDown(self):
        """Видаляємо тестові файли після тестів."""
        os.remove("empty.csv")
        os.remove("test_data.csv")

    def test_read_text_with_pandas_existing(self):
        """Тест зчитування CSV-файлу через pandas."""
        expected_output = "    name  age\n0   John   25\n1  Alice   30"
        self.assertEqual(read_text_with_pandas("test_data.csv"), expected_output)

    def test_read_text_with_pandas_missing(self):
        """Тест зчитування неіснуючого CSV-файлу."""
        self.assertEqual(read_text_with_pandas("missing.csv"), "Файл missing.csv не знайдено.")

    def test_read_text_with_pandas_empty(self):
        """Тест зчитування порожнього CSV-файлу."""
        self.assertEqual(read_text_with_pandas("empty.csv"), "Файл empty.csv порожній або має неправильний формат.")


if __name__ == "__main__":
    unittest.main()
