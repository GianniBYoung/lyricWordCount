def extraTrim(fileName):
    f = open(fileName, "r")
    text = f.readlines()
    f = open(fileName, "w")

    for line in text:
        if ord(line[0]) != 91 and ord(line[0]) != 40:
            f.write(line)
    f.close()


def splittableLyrics():
    lyrics = ""
    lyricsList = open("lyrics.txt").readlines()
    punctuation = """!"#$%&'()*+,./:;<=>?@[\]^_`{|}~"""

    for line in lyricsList:
        lyrics += "".join(line.replace('\n'," ").lower())
        print(line.strip('\n'))
        for c in punctuation:
            lyrics = lyrics.replace(c, "")
    return lyrics


def removeBoringwords(string,  dict):
    boringWords = ['a', 'as', 'now', 'i', 'me', 'an', 'the', 'or', 'be', 'its', 'not', '', 'this', 'that', 'for', 'he', 'her', 'him', 'they', 'but', 'do', 'no', 'on', 'from', 'how',
                   'there', 'has', """i'm""", 'did', 'can', 'his', 'to', 'in', 'am', 'is', 'my', 'so', 'have', 'these', 'ya', 'too', 'with', 'hers', 'and', 'if', '-', 'it', 'at', 'im', 'oh', 'of']

    for x in range(len(boringWords)):
        if boringWords[x] in dict:
            del dict[boringWords[x]]

    return dict
