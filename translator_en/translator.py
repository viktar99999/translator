import googletrans
from googletrans import Translator
file = open('/home/user_name/contents.txt', 'r')
content = file.read()
print(content)
translator = Translator()
result = translator.translate(content, dest='ru')
print(result.text)
with open('/home/user_name/text.txt', 'w') as f:
    f.write(result.text)


