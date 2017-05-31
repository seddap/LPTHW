#Exercise 40: Modules, Classes and Objects

class Song(object):
    def __init__(self, lyrics):
        self.lyrics = lyrics

    def sing_me_a_song(self):
        for line in self.lyrics:
            print(line)

song_that_never_ends = Song(["This is the song that doesn't end",
                             "And it goes on and on my friend",
                             "Some people",
                             "started singing it",
                             "not knowing what it was"])

song_that_never_ends_ending = Song(["And they'll continue singing it",
                                    "Forever just because..."])

ending = input("Should it end? Yes or No? ")
if ending == "yes":
    song_that_never_ends.sing_me_a_song()
    song_that_never_ends_ending.sing_me_a_song()
elif ending == "no":
    while True:
        song_that_never_ends.sing_me_a_song()
        song_that_never_ends_ending.sing_me_a_song()
else:
    print ("This isn't an option you fool.")
