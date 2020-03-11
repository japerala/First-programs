import random
lives = 9
words = ['pizza', 'keiju', 'kieli', 'kieli', 'paita', 'sorsa', 'kirje', 'piano',
         'lehmä', 'kalja', 'viina', 'koodi', 'aitio', 'lätkä', 'kärsä', 'harja',
         'kampa', 'pyörä', 'kahvi', 'lauta', 'laulu', 'auto', 'käsi', 'talo',
         'puhe', 'tila', 'sika', 'kana', 'kuva', 'ilma', 'lasi', 'väri', 'aita', 'äiti']
secret_word = random.choice(words)
clue = []
index=0
while index < len(secret_word):
    clue.append('?')
    index=index+1
heart_symbol = u'\u2764'
guessed_word_correctly = True
unknown_letters=len(secret_word)

def update_clue(guessed_letter, secret_word, clue, unknown_letters):
    index=0
    while index < len(secret_word):
        if guessed_letter==secret_word[index]:
            clue[index]=guessed_letter
            unknown_letters=unknown_letters - 1
        index=index+1
    return unknown_letters

difficulty=input('Valitse vaikeustaso (taso 1, 2 tai 3):\n1. Nössö\n2. Normaalimies\n3. Absoluuttinen hullumies\nValitse: ')
difficulty=int(difficulty)

if difficulty==1:
    lives=12
elif difficulty==2:
    lives=9
else:
    lives=6
     
while lives > 0:
    print(clue)
    print('Henkiä jäljellä: '+heart_symbol * lives)
    guess=input('Arvaa kirjain tai koko sana: ')

    if guess==secret_word:
        guessed_word_correctly=True
        break

    if guess in secret_word:
        unknown_letters=update_clue(guess, secret_word, clue, unknown_letters)
    else:
        print('Väärin. Menetit yhden hengen')
        lives=lives-1
    if unknown_letters==0:
        guessed_word_correctly=True
        break

if guessed_word_correctly==True:
    print('Voitit! Salainen sana oli ' + secret_word)
else:
    print('Hävisit! Salainen sana oli ' + secret_word)
