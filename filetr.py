import os
import re
from googletrans import Translator

def count_words(text):
    words = re.findall(r'\w+', text)
    return len(words)

def count_sentences(text):
    sentences = re.split(r'[.!?]', text)
    return len(sentences)

def main():
    config_filename = "config.txt"
    if not os.path.exists(config_filename):
        print("Помилка: Конфігураційний файл не знайдено.")
        return

    with open(config_filename, "r") as config_file:
        config_lines = config_file.readlines()

    if len(config_lines) < 6:
        print("Помилка: Недостатньо інформації у конфігураційному файлі.")
        return

    text_filename = config_lines[0].strip()
    target_language = config_lines[1].strip()
    output_destination = config_lines[2].strip()
    max_chars = int(config_lines[3].split()[0].strip())
    max_words = int(config_lines[4].split()[0].strip())
    max_sentences = int(config_lines[5].split()[0].strip())

    if not os.path.exists(text_filename):
        print(f"Помилка: Файл з текстом '{text_filename}' не знайдено.")
        return

    with open(text_filename, "r", encoding="utf-8") as text_file:
        text = text_file.read()

    print(f"Назва файлу: {text_filename}")
    print(f"Кількість символів: {len(text)}")
    print(f"Кількість слів: {count_words(text)}")
    print(f"Кількість речень: {count_sentences(text)}")
    print(f"Мова тексту: Англійська")  # Ви можете додати розпізнавання мови, якщо це необхідно

    # Перевіряємо умови завершення перекладу
    if len(text) <= max_chars and count_words(text) <= max_words and count_sentences(text) <= max_sentences:
        print("Умови завершення перекладу виконано.")

        translator = Translator()
        translation = translator.translate(text, dest=target_language)

        if output_destination == "screen":
            print(f"Мова перекладу: {target_language}\n")
            print(translation.text)
        elif output_destination == "file":
            output_filename = f"translate_{text_filename.split('.')[0]}_to_{target_language}.txt"
            with open(output_filename, "w", encoding="utf-8") as output_file:
                output_file.write(translation.text)
            print(f"Переклад тексту у файлі: {output_filename}")
        else:
            print("Помилка: Невірний тип виводу у конфігураційному файлі.")
    else:
        print("текст не підходить під обмеження в файлі config.txt")
if __name__ == "__main__":
    main()
