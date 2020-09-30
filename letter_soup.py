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
            if word.current_direction == 'up':
                row -= 1
            elif word.current_direction == 'down':
                row += 1
            elif word.current_direction == 'left':
                column -= 1
            elif word.current_direction == 'right':
                column += 1
            elif word.current_direction == 'right_up':
                row -= 1
                column += 1
            elif word.current_direction == 'right_down':
                row += 1
                column += 1
            elif word.current_direction == 'left_up':
                row -= 1
                column -= 1
            elif word.current_direction == 'left_down':
                row += 1
                column -= 1

    
    def val_word(self, word):
        if word.current_pos!=None:
            row = word.current_pos[0]
            column = word.current_pos[1]
            for letter in word.value:
                board_value = self.board[row][column]
                if board_value == '' or board_value == letter:
                    if word.current_direction == 'up':
                        row -= 1
                    elif word.current_direction == 'down':
                        row += 1
                    elif word.current_direction == 'left':
                        column -= 1
                    elif word.current_direction == 'right':
                        column += 1
                    elif word.current_direction == 'right_up':
                        row -= 1
                        column += 1
                    elif word.current_direction == 'right_down':
                        row += 1
                        column += 1
                    elif word.current_direction == 'left_up':
                        row -= 1
                        column -= 1
                    elif word.current_direction == 'left_down':
                        row += 1
                        column -= 1
                else:
                    return False
        else:
            return False
        return True
    
    def fill_words(self):
        for word in self.words:
            word.gen_new_pos_dir()
            valid_word = self.val_word(word)
            if valid_word:
                self.write_word(word)
            else:
                while len(word.valid_pos) > 0 and not valid_word:
                    # print(f'word.valid_pos = {len(word.valid_pos)}')
                    word.get_valid_pos()
                    valid_word = self.val_word(word)
                    if valid_word:
                        self.write_word(word)
                    else:
                        print(f"Can't add word: {word.value} {word.current_direction} {word.current_pos}")
    
    def fill_empty (self):
        for i, row in enumerate(self.board):
            for j, letter in enumerate(row):
                if letter == '':
                    random_letter = random.choice([chr(i) for i in range(65,91)])
                    self.board[i][j] = random_letter

class Word():
    def __init__(self, value):
        self.value = value.upper()
        self.letter_soup = None
        self.clear_pos()
    
    def __repr__(self) -> str:
        return self.value

    def __len__(self):
        return len(self.value)

    def clear_pos(self):
        self.available_direction = ['up','down','left', 'right','right_up', 
                                    'right_down', 'left_up', 'left_down']
        self.current_direction = ''
        self.current_pos = None
        self.valid_pos = []
        self.unusable_pos = []
    
    def gen_new_pos_dir(self):
        new_direction = random.choice(self.available_direction)
        self.available_direction.remove(new_direction)
        self.gen_possible_pos(new_direction)
        self.current_direction = new_direction
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
        elif new_direction == 'right_up':
            self.valid_pos = [(i,j) for i in range(len(self) - 1, self.letter_soup.rows) for j in range(0, self.letter_soup.columns - len(self) + 1)]
        elif new_direction == 'right_down':
            self.valid_pos = [(i,j) for i in range(0, self.letter_soup.rows - len(self) + 1) for j in range(0, self.letter_soup.columns - len(self) + 1)]
        elif new_direction == 'left_up':
            self.valid_pos = [(i,j) for i in range(len(self) - 1, self.letter_soup.rows) for j in range(len(self) - 1, self.letter_soup.columns)]
        elif new_direction == 'left_down':
            self.valid_pos = [(i,j) for i in range(0, self.letter_soup.rows - len(self) + 1) for j in range(len(self) - 1, self.letter_soup.columns)]

    def get_valid_pos(self):
        self.valid_pos.remove(self.current_pos)
        self.unusable_pos.append(self.current_pos)
        if self.valid_pos:
            self.current_pos = random.choice(self.valid_pos)
        else:
            self.current_pos = None

# %%
file_name = 'word_input.txt'
rows = 10
columns = 10
# %%
# %%
letter_soup = LetterSoup(rows, columns)
letter_soup.read_words(file_name)
letter_soup.fill_words()
letter_soup.fill_empty()
print(letter_soup.board)
# %%
