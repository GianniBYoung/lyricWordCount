# Author: Gianni Young 10/01/2019
import lyricsgenius
import string
from re import split
from trim import extraTrim
genius = lyricsgenius.Genius("Your Access Token Here")

print("Please provide an artist to search for:\n")
givenArtist= input()
print("Please provide an song to search for:\n\n")
givenSong= input()


song = genius.search_song(givenSong, givenArtist, get_full_info=False)
song.save_lyrics(filename='lyrics',extension='txt',verbose=False,overwrite=True)

extraTrim("lyrics.txt")
lyricsList= open("lyrics.txt").readlines()
lyrics= ""
print("\n*********************************************************************************\n"+givenSong.title()+" by "+ givenArtist.title() +" Lyrics:\n")

for line in lyricsList:
    lyrics+= "".join(line)
    print(line.strip('\n'))
    # remove punctuation to reduce issues with the word occurence
    for c in string.punctuation:
        lyrics= lyrics.replace(c,"")

print("\n*********************************************************************************\n\n"+ "\nOccurences of each unique word:\n\n")

dict = {word: lyrics.count(word)+1 for word in split(r'[,\s]\s*', lyrics.lower())}

for key in dict:
    output= str(key)+": "+ str(dict[key])
    print(output)
# order descending
#issues with single char (x gon give it to ya)
