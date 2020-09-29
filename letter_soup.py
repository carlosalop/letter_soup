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
        self.words = [Word(word.replace('\n',''))  for word in lines]
        for word in self.words:
            word.letter_soup = self

    def write_word (self, word):
        row = word.current_pos[0]
        column = word.current_pos[1]
        for letter in word.value:
            self.board[row][column] = letter
            if word.direction == 'up':
                row -= 1
            elif word.direction == 'down':
                row += 1
            elif word.direction == 'left':
                column -= 1
            elif word.direction == 'right':
                column += 1
    
    def val_word(self, word):
        row = word.current_pos[0]
        column = word.current_pos[1]
        for letter in word.value:
            board_value = self.board[row][column]
            if board_value == '' or board_value == letter:
                if word.direction == 'up':
                    row -= 1
                elif word.direction == 'down':
                    row += 1
                elif word.direction == 'left':
                    column -= 1
                elif word.direction == 'right':
                    column += 1
            else:
                return False
        return True
    
    def fill_words(self):
        for word in self.words:
            word.get_new_pos_dir()
            if self.val_word(word):
                self.write_word(word)
            else:
                print(f"Can't add word: {word.value} {word.direction} {word.current_pos}")
    
    def fill_empty (self):
        for i, row in enumerate(self.board):
            for j, letter in enumerate(row):
                if letter == '':
                    random_letter = random.choice([chr(i) for i in range(65,91)])
                    self.board[i][j] = random_letter

class Word():
    direction = ('up','down','left', 'right')

    def get_new_pos_dir(self):
        new_direction = random.choice(Word.direction)
        if not self.valid_pos:
            self.gen_possible_pos(new_direction)
        self.direction = new_direction
        self.current_pos = random.choice(self.valid_pos)

    def gen_possible_pos(self, new_direction):
        if new_direction == 'up':
            self.valid_pos = [(i,j) for i in range(len(self) - 1, self.letter_soup.rows) for j in range(0, self.letter_soup.columns)]
        elif new_direction == 'down':
            self.valid_pos = [(i,j) for i in range(0, self.letter_soup.rows - len(self) + 1) for j in range(0, self.letter_soup.columns)]
        elif new_direction == 'left':
            self.valid_pos = [(i,j) for i in range(0, self.letter_soup.rows) for j in range(len(self) - 1, self.letter_soup.columns)]
        elif new_direction == 'right':
            self.valid_pos = [(i,j) for i in range(0, self.letter_soup.rows) for j in range(0, self.letter_soup.columns - len(self) + 1)]

    def __init__(self, value):
        self.value = value.upper()
        self.letter_soup = None
        self.clear_pos()
    
    def __repr__(self) -> str:
        return self.value

    def clear_pos(self):
        self.direction = ''
        self.current_pos = None
        self.valid_pos = []
        self.unusable_pos = []
    
    def __len__(self):
        return len(self.value)

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
