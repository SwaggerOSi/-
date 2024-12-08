class WordsFinder:
    def __init__(self, *file_names):
        self.file_names = file_names  # Сохраняем названия файлов как кортеж

    def get_all_words(self):
        all_words = {}
        for file_name in self.file_names:
            try:
                with open(file_name, 'r', encoding='utf-8') as file:
                    content = file.read().lower()
                    # Убираем пунктуацию
                    for char in [',', '.', '=', '!', '?', ';', ':', ' - ']:
                        content = content.replace(char, '')
                    words = content.split()
                    all_words[file_name] = words
            except FileNotFoundError:
                all_words[file_name] = []
        return all_words

    def find(self, word):
        word = word.lower()
        result = {}
        all_words = self.get_all_words()
        for name, words in all_words.items():
            try:
                result[name] = words.index(word) + 1  # Позиция слова (начиная с 1)
            except ValueError:
                result[name] = None  # Слово не найдено
        return result

    def count(self, word):
        word = word.lower()
        result = {}
        all_words = self.get_all_words()
        for name, words in all_words.items():
            result[name] = words.count(word)
        return result


# Пример использования
if __name__ == "__main__":
    finder = WordsFinder('test_file.txt')
    print(finder.get_all_words())  # Список слов из файла
    print(finder.find('TEXT'))  # Поиск слова "TEXT"
    print(finder.count('teXT'))  # Подсчёт количества "TEXT"