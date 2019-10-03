# Author: Gianni Young 10/01/2019
import lyricsgenius
import string
from re import split
from trimTools import *
genius = lyricsgenius.Genius("Your Access Token Here")

print("Please provide an artist to search for:\n")
givenArtist = input()
print("Please provide an song to search for:\n\n")
givenSong = input()
print("Include boring words?:y/N")
includeBoringwords = input()

song = genius.search_song(givenSong, givenArtist, get_full_info=False)
song.save_lyrics(filename='lyrics', extension='txt',
                 verbose=False, overwrite=True)

extraTrim("lyrics.txt")

lyrics = splittableLyrics()
print("\n*********************************************************************************\n" +
      givenSong.title() + " by " + givenArtist.title() + " Lyrics:\n")
print("\n*********************************************************************************\n\n" +
      "Occurences of each unique word:\n")


dict = {word: lyrics.count(
    word) + 1 for word in split(r'[,\s]\s*', lyrics.lower())}

if includeBoringwords.lower() == 'n':
    dict = removeBoringwords(includeBoringwords, dict)
else:
    if '' in dict:
        del dict['']

sorted_dict = sorted(dict.items(), key=lambda x: x[1])
sorted_dict = sorted_dict[::-1]
for x in range(len(sorted_dict)):
    print(sorted_dict[x])
