import googletrans
from googletrans import Translator
file = open('/home/user_name/contents.txt', 'r', encoding='utf-8')
content = file.read()
print(content)
line_count = sum(1 for line in open('/home/user_name/contents.txt', 'r', encoding='utf-8'))
print(line_count)
translator = Translator()
result = translator.translate(content, dest='ru')
print(result.text)
with open('/home/user_name/text.txt', 'w', encoding='utf-8') as f:
    f.write(result.text)


