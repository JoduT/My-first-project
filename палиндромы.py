word = str(input('Придумайте слово: '))
def check(word):
    if word == word[::-1]:
        print(True)
    else:
        print(False)
check(word)

