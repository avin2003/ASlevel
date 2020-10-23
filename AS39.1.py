import random
import string
word = string.ascii_letters +string.ascii_letters
playlist = []

last = ''
lastlast= ''
artists = ["Lorde","Jcole","HarryS","TaylorS","BTS","Weeknd","ArianaG","Marias","Adele","Drake"]

for artist in range(10):
    playlist.append([])
    for songs in range(10):
        playlist[artist].append(artists[artist] + " " +("".join(random.choice(word) for i in range(5))))
print(playlist)

x= 1
while x <21:
    play = random.choice(playlist)
    if play == last or play == lastlast:
        play = random.choice(playlist)
    else:
        print("Song",x,":",(play[random.randint(0,9)]))
        lastlast= last
        last = play
        x = x+ 1










