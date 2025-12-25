words=input('请输入若干单词，用空格分隔：').split(' ')
unique_words=set(words)
sorted_words=sorted(unique_words)
for word in sorted_words:
    print(word)