import tweepy
import time
import random

#Twitter-Authentifizierung
C_KEY =
C_SECRET =
A_TOKEN =
A_TOKEN_SECRET =

auth = tweepy.OAuthHandler(C_KEY, C_SECRET)
auth.set_access_token(A_TOKEN, A_TOKEN_SECRET)
api = tweepy.API(auth)

#Random Nomen + Adjektiv
def Line():
#Initialisierung
    upper = 1
    line = ""
    line4 = ""
#Text wird ausgewählt
    line1 = random.choice(open('adjectives.txt').readlines())
    line2 = random.choice(open('nouns.txt').readlines())
    line3 = line1 + " " + line2
#Zeilenumbrüche werden ersetzt
    for z in line3:
        if z == "\n":
            z = ""
        line4 = line4 + z
#Erster Buchstabe wird groß geschrieben
    for u in line4:
        if upper == 1:
            upper = ord(u)
            upper = upper - 32
            u = chr(upper)
        line = line + u
    return line

#Ausgabe
while True:
#Ausgabe Python
    print(Line())
#Ausgabe Twitter
    api.update_status(Line())
#Wartezeit
    time.sleep(900)
