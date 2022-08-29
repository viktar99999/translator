import googletrans
from googletrans import Translator
file = open('/home/vik/contents.txt', 'r')
content = file.read()
print(content)
if content == 'en':
    print('en')
else:
    print('ru')
translator = Translator()
result = translator.translate(content, dest='en')
print(result.text)
with open('/home/vik/text.txt', 'w') as f:
    f.write(result.text)


