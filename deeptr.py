from translate.deep import TransLate, LangDetect, CodeLang, LanguageList

text_to_translate = "текст, який необхідно перекласти"
source_language = "auto"
target_language = "en"

translated_text = TransLate(text_to_translate, source_language, target_language)
print(f"Переклад: {translated_text}")

detected_language = LangDetect(text_to_translate, "lang")
print(f"Мова оригінального тексту: {detected_language}")

language_code = CodeLang("ukrainian")
print(f"Код Ukrainian: {language_code}")

language_name = CodeLang("en")
print(f"Назва en: {language_name}")

result = LanguageList(out="screen", text="текст, який необхідно перекласти")
print(result)
