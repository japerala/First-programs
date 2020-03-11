def check_guess(guess, answer):
    global score
    still_guessing=True
    attemp=0
    while still_guessing and attemp < 3:
        if guess.lower()==answer.lower():
            print('Oikea vastaus!')
            score=score+3-attemp
            still_guessing=False
        else:
            if attemp < 2:
                guess=input('Ikävä kyllä väärä vastaus. Yritä uudelleen')
    if attemp==3:
        print('Oikea vastaus on ' + answer)
score=0
print('Arvaa mikä eläin')
guess1=input('Mikä eläin asuu Pohjoisnavalla?')
check_guess(guess1, 'jääkarhu')
guess1=input('Mikä eläin ei aina riehu vaan syö välillä puolukoita?')
check_guess(guess1, 'karhu')
guess1=input('Mikä eläin nukkuu päivät pitkät?')
check_guess(guess1, 'laiskiainen')
guess1=input('Mikä on maailman nopein eläin?')
check_guess(guess1, 'gepardi')
guess1=input('Mikä on maailman suurin eläin?')
check_guess(guess1,'sinivalas')
guess=input('Mikä näistä on suurin? \n \
a) henkilöauto\n b) mikroauto\n c) linja-auto\n d) pakettiauto\n \
Kirjoita vastaus a, b, c tai d: ')
check_guess(guess, 'c')
guess1=input('Saimaa on Suomen suurin järvi. Tosi vai epätosi?')
check_guess(guess, 'tosi')
print('Pistemääräsi on '+str(score))
