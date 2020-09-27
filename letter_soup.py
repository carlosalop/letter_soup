#%%
import random
#%%
class LetterSoup():
    direction = ('up','down','left', 'right')
        # 'up_right',' up_left', 'down_right', 'down_left')

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
    
    def get_new_pos_dir(self, word):
        new_direction = random.choice(LetterSoup.direction)
        word_len = len(word)
        possible_pos = self.gen_possible_pos(word_len, new_direction)
        return (random.choice(possible_pos), new_direction)

    def gen_possible_pos(self, word_len, new_direction):
        if new_direction == 'up':
            return [(i,j) for i in range(word_len - 1, self.rows) for j in range(0, self.columns)]
        elif new_direction == 'down':
            return [(i,j) for i in range(0, self.rows - word_len + 1) for j in range(0, self.columns)]
        elif new_direction == 'left':
            return [(i,j) for i in range(0, self.rows) for j in range(word_len - 1, self.columns)]
        elif new_direction == 'right':
            return [(i,j) for i in range(0, self.rows) for j in range(0, self.columns - word_len + 1)]

    def write_word (self, word, position, direction):
        row = position[0]
        column = position[1]
        for letter in word:
            self.board[row][column] = letter
            if direction == 'up':
                row -= 1
            elif direction == 'down':
                row += 1
            elif direction == 'left':
                column -= 1
            elif direction == 'right':
                column += 1
    
    def fill_empty (self):
        for i, row in enumerate(self.board):
            print(row)
            for j, letter in enumerate(row):
                if letter == '':
                    random_letter = random.choice([chr(i) for i in range(65,91)])
                    self.board[i][j] = random_letter
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
