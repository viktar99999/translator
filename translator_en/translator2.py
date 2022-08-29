import googletrans
from googletrans import Translator
file = open('/home/user_name/contents.txt', 'r')
content = file.read()
print(content)
s = content.split(' ')
ru = ""
en = ""
for k in content:
    if k == "а-яА-Я":
        print(ru)
    else:
        k == "a-zA-Z"
        print(en)

translator = Translator()
result = translator.translate(content, dest='ru')
result = translator.translate(content, dest='en')
print(result.text)
print(result.text)
with open('/home/user_name/text.txt', 'w') as f:
    f.write(result.text)


