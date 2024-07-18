guesses = []
guesses1 = []
guesses2 = []
word = ""
word1 = ""
word2 = ""
word1Done = False
word2Done = False
word_pos = 0
word_pos_1 = 0
word_pos_2 = 0
import random
over = False
from os import system

letters = ["q","w","e","r","t","y","u","i","o","p","a","s","d","f","g","h","j","k","l","z","x","c","v","b","n","m"]

wordList = "english.txt"
DOUBLE = False

from collections import defaultdict
keyboard = defaultdict(list)
for letter in letters:
  keyboard[letter] = letter
def find(s, ch):
  return [i for i, ltr in enumerate(s) if ltr == ch]

def clear():
  system('cls')

class col:
  cyan = '\033[96m'
  green = '\033[92m' #green
  yellow = '\033[93m' #yellow
  white = '\033[37m' #white
  gray = '\u001b[30;1m' #gray

print("Input 1 for single wordle and 2 for double wordle.")
cho = input("> ")
if cho == "1":
  DOUBLE = False
  over = False
  clear()
elif cho == "2":
  DOUBLE = True
  over = False
  clear()
else:
  DOUBLE = True
  over = False
  clear()

while True:
  if not DOUBLE:
    with open(wordList, "r") as file:
      data = file.read()
      words = data.split()
      word_pos = random.randint(0, len(words)-1)
      word = words[word_pos]
    
    while not over:
      print(col.cyan+"                            Wordle v1\n"+col.white)
      for guess in guesses:
        print("                              "+guess)
      for i in range(6 - len(guesses)):
        print("                              _____")
      daw = "\n                        "
      for i,letter in enumerate(letters):
        if i == 9:
          daw += keyboard[letter] + "\n                         "
        elif i == 18:
          daw += keyboard[letter] + "\n                           "
        else:
          daw += keyboard[letter] + " "
      print(f"{daw}")
      #print("\n                        q w e r t y u i o p \n                         a s d f g h j k l \n                           z x c v b n m")
      #word = "amman"
      #print(word)
      prompt = input("> ")
      
      if len(prompt) == 5:
        clear()
        with open(wordList, 'r') as f:
          if prompt in f.read():
            newg = ""
            wcount = defaultdict(list)
            for index, char in enumerate(prompt):
              if not wcount[char]:
                wcount[char] = 0
              newc = char
              if char in word:
                if wcount[char] < len(find(word, char)):
                  if index == word.index(char):
                    newc = col.green+char+col.white
                    keyboard[char] = col.green+char+col.white
                  else:
                    f = False
                    for pos in find(word, char):
                      if index == pos:
                        newc = col.green+char+col.white
                        keyboard[char] = col.green+char+col.white
                        f = True
                    if not f:
                      newc = col.yellow+char+col.white
                      if not keyboard[char].startswith(col.green):
                        keyboard[char] = col.yellow+char+col.white
                  wcount[char] = wcount[char] + 1
              else:
                keyboard[char] = col.gray+char+col.white
              newg += newc
            guesses.append(newg)
          else:
            clear()
            print("                         Word not found.")
      else:
        clear()
        print("                    Invalid character amount.")
      if prompt == word:
        over = True
      if len(guesses) == 6:
        over = True
    clear()
    print(col.cyan+"                            Wordle v1\n"+col.white)
    for guess in guesses:
      print("                              "+guess)
    for i in range(6 - len(guesses)):
      print("                              _____")
    print("Correct word: "+word)
    over = False
    guesses = []
    print("\nInput 1 for single wordle and 2 for double wordle.")
    for letter in letters:
      keyboard[letter] = letter
    cho = input("> ")
    if cho == "1":
      DOUBLE = False
      over = False
      clear()
    elif cho == "2":
      DOUBLE = True
      over = False
      clear()
    else:
      DOUBLE = False
      over = False
      clear()
  else:
    with open(wordList, "r") as file:
      data = file.read()
      words = data.split()
      word_pos_1 = 0
      word_pos_2 = 0
      while word_pos_1 == word_pos_2:
        word_pos_1 = random.randint(0, len(words)-1)
        word_pos_2 = random.randint(0, len(words)-1)
      word1 = words[word_pos_1]
      word2 = words[word_pos_2]
    
    while not over:
      print(col.cyan+"                            Wordle v2\n"+col.white)
      for i in range(len(guesses1) if len(guesses1) > len(guesses2) else len(guesses2)):
        x = ("                    "+guesses1[i]+"               "+guesses2[i] if i + 1 <= len(guesses1) and i + 1 <= len(guesses2) else "                    "+guesses1[i] if not i + 1 <= len(guesses2) else "                                        "+guesses2[i])
        print(x)
      for i in range(7 - (len(guesses1) if len(guesses1) > len(guesses2) else len(guesses2))):
        x = ("                    _____               _____" if not word1Done and not word2Done else "                    _____" if word2Done else "                                        _____")
        print(x)
      daw = "\n                       "
      for i,letter in enumerate(letters):
        if i == 9:
          daw += keyboard[letter] + "\n                        "
        elif i == 18:
          daw += keyboard[letter] + "\n                          "
        else:
          daw += keyboard[letter] + " "
      print(f"{daw}")
      prompt = input("> ")
      
      if len(prompt) == 5:
        clear()
        with open(wordList, 'r') as f:
          if prompt in f.read():
            wordFilter = defaultdict(list)
            if not word1Done:
              if prompt == word1:
                word1Done = True
              newg = ""
              wcount = defaultdict(list)
              for index, char in enumerate(prompt):
                if not wcount[char]:
                  wcount[char] = 0
                newc = char
                if char in word1:
                  if wcount[char] < len(find(word1, char)):
                    if index == word1.index(char):
                      newc = col.green+char+col.white
                      wordFilter[char] = 3
                    else:
                      f = False
                      for pos in find(word1, char):
                        if index == pos:
                          newc = col.green+char+col.white
                          wordFilter[char] = 3
                          f = True
                      if not f:
                        newc = col.yellow+char+col.white
                    wcount[char] = wcount[char] + 1
                else:
                  wordFilter[char] = 1
                newg += newc
              guesses1.append(newg)
            if not word2Done:
              if prompt == word2:
                word2Done = True
              newg = ""
              wcount = defaultdict(list)
              for index, char in enumerate(prompt):
                if not wcount[char]:
                  wcount[char] = 0
                newc = char
                if char in word2:
                  if wcount[char] < len(find(word2, char)):
                    if index == word2.index(char):
                      newc = col.green+char+col.white
                      if wordFilter[char] == 3:
                        keyboard[char] = col.green+char+col.white
                    else:
                      f = False
                      for pos in find(word2, char):
                        if index == pos:
                          newc = col.green+char+col.white
                          if wordFilter[char] == 3:
                            keyboard[char] = col.green+char+col.white
                          f = True
                      if not f:
                        newc = col.yellow+char+col.white
                    wcount[char] = wcount[char] + 1
                else:
                  if wordFilter[char] == 1:
                    keyboard[char] = col.gray+char+col.white
                newg += newc
              guesses2.append(newg)
          else:
            clear()
            print("                         Word not found.")
      else:
        clear()
        print("                    Invalid character amount.")
      if len(guesses1) == 7 or len(guesses2) == 7:
        over = True
      if word1Done and word2Done:
        over = True
    #clear()
    print(col.cyan+"                            Wordle v2\n"+col.white)
    for i in range(len(guesses1) if len(guesses1) > len(guesses2) else len(guesses2)):
        x = ("                    "+guesses1[i]+"               "+guesses2[i] if i + 1 <= len(guesses1) and i + 1 <= len(guesses2) else "                    "+guesses1[i] if not i + 1 <= len(guesses2) else "                                        "+guesses2[i])
        print(x)
    
    print("Word 1: "+word1)
    print("Word 2: "+word2)
    guesses1 = []
    guesses2 = []
    word1Done = False
    word2Done = False
    print("\nInput 1 for single wordle and 2 for double wordle.")
    for letter in letters:
      keyboard[letter] = letter
    cho = input("> ")
    if cho == "1":
      DOUBLE = False
      over = False
      clear()
    elif cho == "2":
      DOUBLE = True
      over = False
      clear()
    else:
      DOUBLE = True
      over = False
      clear()