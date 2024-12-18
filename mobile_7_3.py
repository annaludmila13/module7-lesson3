import string

class WordsFinder:
    def __init__(self, *file_names):
        self.file_names = file_names

    def get_all_words(self):
        all_words = {}
        for file_name in self.file_names:
            with open(file_name, 'r', encoding='utf-8') as file:
                # Считываем строки файла
                text = file.read().lower()  # Приводим к нижнему регистру
                # Убираем пунктуацию
                text = text.translate(str.maketrans('', '', string.punctuation))
                # Разбиваем текст на слова
                words = text.split()
                all_words[file_name] = words
        return all_words

    def find(self, word):
        word = word.lower()  # Приводим к нижнему регистру для поиска
        all_words = self.get_all_words()
        result = {}
        for file_name, words in all_words.items():
            if word in words:
                result[file_name] = words.index(word) + 1  # Позиция слова (1-indexed)
        return result

    def count(self, word):
        word = word.lower()  # Приводим к нижнему регистру для подсчета
        all_words = self.get_all_words()
        result = {}
        for file_name, words in all_words.items():
            result[file_name] = words.count(word)  # Подсчет вхождений слова
        return result

# Пример использования
if __name__ == "__main__":
    # Создание файла с текстом, если он не существует
    with open('test_file.txt', 'w', encoding='utf-8') as f:
        f.write("It's a text for task Найти везде,\n")
        f.write("Используйте его для самопроверки.\n")
        f.write("Успехов в решении задачи!\n")
        f.write("text text text\n")

    # Создаем объект класса с файлами
    finder = WordsFinder('test_file.txt')

    # Получаем все слова
    print(finder.get_all_words())  # Все слова

    # Находим позицию слова
    print(finder.find('text'))  # Позиция слова 'text'

    # Считаем количество вхождений слова
    print(finder.count('text'))  # Количество слов 'text'



