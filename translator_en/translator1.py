import googletrans
from googletrans import Translator
file = open('/home/user_name/contents.txt', 'r')
content = file.read()
print(content)
if content == 'en':
    print('en')
else:
    print('ru')
translator = Translator()
result = translator.translate(content, dest='en')
print(result.text)
with open('/home/user_name/text.txt', 'w') as f:
    f.write(result.text)


