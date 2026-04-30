from pathlib import Path

def count_words(path):
    """Подсчитывет приблизительное количество слов в файле."""
    try:
        contents = path.read_text(encoding='utf-8')
    except FileNotFoundError:
        print(f"Sorry, the file {path} does not exist.")
    else:
        #Подсчет приблизительного количества слов в файле
        words = contents.split()
        num_words = len(words)
        print(f"The file {path} has about {num_words} words.")

filenames = ['alice.txt', 'programming.txt', 'bob.txt']
for filename in filenames:
    path = Path(filename)
    count_words(path)
