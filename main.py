with open("README.md", "r")as file:
    content = file.read()
    words = content.split()
    word_count = len(words)
    print("Количество слов в файле:", word_count)