from gtts import gTTS
my_file = open('text.txt', 'r', encoding='utf-8')
my_str = my_file.read()
my_file.close()
print(my_str)
converter = gTTS(text=my_str, lang='ru')
converter.save('love.mp3')