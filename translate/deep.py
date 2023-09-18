from deep_translator import GoogleTranslator
from langdetect import detect
from googletrans import LANGUAGES
import pycountry
def TransLate(text: str, src: str, dest: str) -> str:
    try:
        translated_text = GoogleTranslator(source=src, target=dest).translate(text)
        return translated_text
    except Exception as e:
        return str(e)

def LangDetect(text: str, set: str) -> str:
    try:
        detected_language = detect(text)
        if set == "lang":
            return detected_language
        elif set == "confidence":
            return "N/A"
        else:
            return f"Language: {detected_language}, Confidence: N/A"
    except Exception as e:
        return str(e)


def CodeLang(lang: str) -> str:
    try:
        if len(lang) == 2:
            language = pycountry.languages.get(alpha_2=lang)
            return language.name
        elif len(lang) == 3:
            language = pycountry.languages.get(alpha_3=lang)
            return language.name
        else:
            code = "".join([c.lower() for c in lang if c.isalpha()])[:2]
            return code if code else "Мову не знайдено або невірний формат"
    except Exception as e:
        return "Невідома мова"



def LanguageList(out: str = "screen", text: str = None) -> str:
    if out not in ["screen", "file"]:
        return "Невірний параметр 'out'. Використовуйте 'screen' або 'file'."

    if out == "file":
        try:
            with open("deep_translate_language_list.txt", "w", encoding="utf-8") as file:
                file.write("N\tLanguage\tISO-639 code\tText\n")

                for index, (code, lang) in enumerate(LANGUAGES.items(), start=1):
                    if text:
                        try:
                            translated_text = GoogleTranslator(source='auto', target=code).translate(text)
                            file.write(f"{index}\t{lang}\t{code}\t{translated_text}\n")
                        except Exception as e:
                            file.write(f"{index}\t{lang}\t{code}\tError: {str(e)}\n")
                    else:
                        file.write(f"{index}\t{lang}\t{code}\n")

                return "Ok"
        except Exception as e:
            return f"Помилка: {str(e)}"

    elif out == "screen":
        try:
            print("N\tLanguage\tISO-639 code\tText")
            print("-" * 48)

            for index, (code, lang) in enumerate(LANGUAGES.items(), start=1):
                if text:
                    try:
                        translated_text = GoogleTranslator(source='auto', target=code).translate(text)
                        print(f"{index}\t{lang}\t{code}\t{translated_text}")
                    except Exception as e:
                        print(f"{index}\t{lang}\t{code}\tError: {str(e)}")
                else:
                    print(f"{index}\t{lang}\t{code}")

            return "Ok"
        except Exception as e:
            return f"Помилка: {str(e)}"
