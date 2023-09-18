from googletrans import Translator, LANGUAGES


def TransLate(text: str, src: str, dest: str) -> str:
    translator = Translator()
    try:
        translated_text = translator.translate(text, src=src, dest=dest).text
        return translated_text
    except Exception as e:
        return str(e)

def LangDetect(text: str, set: str) -> str:
    translator = Translator()
    try:
        detection = translator.detect(text)
        if set == "lang":
            return detection.lang
        elif set == "confidence":
            return str(detection.confidence)
        else:
            return f"Language: {detection.lang}, Confidence: {detection.confidence}"
    except Exception as e:
        return str(e)

def CodeLang(lang: str) -> str:
    lang = lang.lower()

    for code, name in LANGUAGES.items():
        if lang == code.lower():
            return name

    for code, name in LANGUAGES.items():
        if lang == name.lower():
            return code

    return "Мову не знайдено або невірний формат"


def LanguageList(out: str = "screen", text: str = None) -> str:
    if out not in ["screen", "file"]:
        return "Невірний параметр 'out'. Використовуйте 'screen' або 'file'."

    if out == "file":
        try:
            with open("google_translate_language_list.txt", "w", encoding="utf-8") as file:
                file.write("N\tLanguage\tISO-639 code\tText\n")
                languages = LANGUAGES

                for index, (code, lang) in enumerate(languages.items(), start=1):
                    if text:
                        translator = Translator()
                        translated_text = translator.translate(text, src='auto', dest=code).text
                        file.write(f"{index}\t{lang}\t{code}\t{translated_text}\n")
                    else:
                        file.write(f"{index}\t{lang}\t{code}\n")

                return "Ok"
        except Exception as e:
            return f"Помилка: {str(e)}"

    elif out == "screen":
        try:
            languages = LANGUAGES
            print("N\tLanguage\tISO-639 code\tText")
            print("-" * 48)

            for index, (code, lang) in enumerate(languages.items(), start=1):
                if text:
                    translator = Translator()
                    translated_text = translator.translate(text, src='auto', dest=code).text
                    print(f"{index}\t{lang}\t{code}\t{translated_text}")
                else:
                    print(f"{index}\t{lang}\t{code}")

            return "Ok"
        except Exception as e:
            return f"Помилка: {str(e)}"