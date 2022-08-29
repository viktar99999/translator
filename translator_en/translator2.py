import googletrans
from googletrans import Translator
file = open('/home/user_name/contents.txt', 'r')
content = file.read()
print(content)
s = content.split(' ')
content_ru = ""
content_en = ""
for k in content:
    if k == "а-яА-Я":
        print(content_ru)
    else:
        k == "a-zA-Z"
        print(content_en)

translator = Translator()
result = translator.translate(content_ru, dest='en')
result = translator.translate(content_en, dest='ru')
print(result.text)
print(result.text)
with open('/home/user_name/text.txt', 'w') as f:
    f.write(result.text)


