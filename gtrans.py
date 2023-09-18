from translate.google import TransLate, LangDetect, CodeLang, LanguageList

text_to_translate = "текст, який необхідно перекласти"
source_language = "auto"
target_language = "en"

translated_text = TransLate(text_to_translate, source_language, target_language)
print(f"Переклад: {translated_text}")

detected_language = LangDetect(text_to_translate, "lang")
print(f"Мова оригінального тексту: {detected_language}")

language_code="en"
language_name="ukrainian"

print(f"Код {language_name}: {CodeLang(language_name)}")
print(f"Назва {language_code}: {CodeLang(language_code)}")

result = LanguageList(out="screen", text="текст, який необхідно перекласти")
print(result)
