def tracklist(**kwargs):
    for musician, value in kwargs.items():
        print(musician)
        for album, song in value.items():
            print(f'ALBUM: {album}', f'TRACK: {song}')

tracklist(Woodkid={"The Golden Age": "Run Boy Run",
                   "On the Other Side": "Samara"},
          Cure={"Disintegration": "Lovesong",
                "Wish": "Friday I'm in love",
                "Seventeen Seconds": "A Forest"})