import googletrans
from googletrans import Translator
file = open('/home/vik/contents.txt', 'r')
content = file.read()
print(content)
translator = Translator()
result = translator.translate(content, dest='en')
print(result.text)
with open('/home/vik/text.txt', 'w') as f:
    f.write(result.text)


