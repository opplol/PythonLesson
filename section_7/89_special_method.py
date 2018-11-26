class Word(object):

    def __init__(self, text):
        self.text = text

    def __str__(self):
        return 'World!!!!!!!'

    def __len__(self):
        return len(self.text)

    def __add__(self, word):
        return self.text.lower() + word.text.lower()

    def __eq__(self, word):
        return self.text.lower() == word.text.lower()

w = Word('test')
w2 = Word('###############')
w3 = Word('test')

print(w)
print(len(w))

print(w + w2)

print(w == w2)
print(w == w3)
