import random
import string
adjectives=['uninen', 'nopea', 'hidas', 'väsynyt', 'innokas', 'pehmeä', 'äänekäs', 'pyöreä', 'sileä', 'mutkikas', 'märkä', 'pehmeä','kova',
            'kaunis', 'ruma', 'luja', 'hiljainen', 'haiseva', 'ilkeä',
            'hopeinen', 'likainen']
nouns=['auto', 'omena', 'hattara', 'lippalakki', 'sorsa', 'pallo', 'neliö', 'kello', 'paahdin',
       'karhu', 'liikennemerkki', 'ikkuna', 'laskin', 'vasara', 'vuohi', 'kamera', 'pullo',
       'kirjasto', 'karvalakki', 'huivi', 'pelikonsoli', 'puhelin', 'koira', 'kissa']
color=['musta', 'valkoinen', 'sininen', 'keltainen', 'punainen', 'vihreä', 'lila', 'purppura', 'oranssi']
print('Tällä ohjelmalla luodaan salasana')
while True:
    adjective=random.choice(adjectives)
    noun=random.choice(nouns)
    color=random.choice(color)
    number=random.randrange(0, 1000)
    special_char=random.choice(string.punctuation)

    password=adjective+color+noun+str(number)+special_char
    print("Uusi salasanasi on: %s" % password)

    response=input('Haluatko luoda uuden salasanan? Vastaa k tai e: ')
    if response=='e':
        break
