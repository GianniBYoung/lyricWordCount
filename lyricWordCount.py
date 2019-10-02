# Author: Gianni Young 10/01/2019
import lyricsgenius
import string
from re import split
from trim import extraTrim
genius = lyricsgenius.Genius("Your Access Token Here")

print("Please provide an artist to search for:\n")
givenArtist = input()
print("Please provide an song to search for:\n\n")
givenSong = input()


song = genius.search_song(givenSong, givenArtist, get_full_info=False)
song.save_lyrics(filename='lyrics', extension='txt',
                 verbose=False, overwrite=True)

extraTrim("lyrics.txt")
lyricsList = open("lyrics.txt").readlines()
lyrics = ""
print("\n*********************************************************************************\n" +
      givenSong.title() + " by " + givenArtist.title() + " Lyrics:\n")
punctuation = """!"#$%&'()*+,./:;<=>?@[\]^_`{|}~"""
for line in lyricsList:
    lyrics += "".join(line)
    print(line.strip('\n'))
    for c in punctuation:
        lyrics = lyrics.replace(c, "")

print("\n*********************************************************************************\n\n" +
      "Occurences of each unique word:\n")

dict = {word: lyrics.count(
    word) + 1 for word in split(r'[,\s]\s*', lyrics.lower())}
if '' in dict:
    del dict['']
sorted_dict = sorted(dict.items(), key=lambda x: x[1])
sorted_dict = sorted_dict[::-1]
for x in range(len(sorted_dict)):
    print(sorted_dict[x])
