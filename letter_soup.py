#%%
import random
#%%
class LetterSoup():
    direction_increments = {
        'up': [-1, 0],
        'down': [1, 0],
        'left': [0, -1],
        'right': [0, 1],
        'right_up': [-1, 1],
        'right_down': [1, 1],
        'left_up': [-1, -1],
        'left_down': [1, -1]
    }

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
            pos_modification = LetterSoup.direction_increments.get(word.current_direction)
            row += pos_modification[0]
            column += pos_modification[1]
    
    def val_word(self, word):
        if word.current_pos!=None:
            row = word.current_pos[0]
            column = word.current_pos[1]
            for letter in word.value:
                board_value = self.board[row][column]
                if board_value == '' or board_value == letter:
                    pos_modification = LetterSoup.direction_increments.get(word.current_direction)
                    row += pos_modification[0]
                    column += pos_modification[1]
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
        # This list contains the valid ranges for each direction [row init, row final, column init, column final]
        direction_ranges = {
            'up': [len(self) - 1, self.letter_soup.rows, 0, self.letter_soup.columns],
            'down': [0, self.letter_soup.rows - len(self) + 1, 0, self.letter_soup.columns],
            'left': [0, self.letter_soup.rows, len(self) - 1, self.letter_soup.columns],
            'right': [0, self.letter_soup.rows, 0, self.letter_soup.columns - len(self) + 1],
            'right_up': [len(self) - 1, self.letter_soup.rows, 0, self.letter_soup.columns - len(self) + 1],
            'right_down': [0, self.letter_soup.rows - len(self) + 1, 0, self.letter_soup.columns - len(self) + 1],
            'left_up': [len(self) - 1, self.letter_soup.rows, len(self) - 1, self.letter_soup.columns],
            'left_down': [0, self.letter_soup.rows - len(self) + 1, len(self) - 1, self.letter_soup.columns]
        }

        current_range = direction_ranges.get(new_direction)
        self.valid_pos = [(i,j) for i in range(current_range[0], current_range[1]) for j in range(current_range[2], current_range[3])]

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
def main():
    letter_soup = LetterSoup(rows, columns)
    letter_soup.read_words(file_name)
    letter_soup.fill_words()
    letter_soup.fill_empty()
    for word in letter_soup.words:
        print(word.value, word.current_direction, word.current_pos)
    for i, line in enumerate(letter_soup.board):
        print(i, line)
# %%
if __name__ == '__main__':
    main()
# %%
