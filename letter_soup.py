#%%
import random
#%%
class LetterSoup():
    def __init__(self, rows, columns):
        self.rows = rows
        self.columns = columns
        self.board = [['' for i in range(rows)] for j in range(columns)]
    
    def __repr__(self):
        return f'{self.board!r}'

    def read_words(self, file_name):
        with open(file_name) as file:
            lines = file.readlines()
        self.words = [word.replace('\n','')  for word in lines]

# %%
file_name = 'word_input.txt'
rows = 10
columns = 10
# %%
# %%
letter_soup = LetterSoup(rows, columns)
letter_soup.read_words(file_name)
print(letter_soup)
# %%
