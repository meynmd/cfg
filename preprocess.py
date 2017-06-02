import string
from collections import defaultdict

LangChars = string.ascii_letters + ',.?!\''

def ExtractPunct(words, punct_chars):
    result = []
    for word in words:
        t = [x for x in ExtractPunctFromWord(word, punct_chars) if len(x) > 0]
        result += t
    return result


def ExtractPunctFromWord(word, punct_chars):

    # if len(word) < 2:
    #     return word
    #
    for i in range(len(word)):
        if word[i] in punct_chars:
            break

    if i < len(word) - 1:
        return [word[: i]] + [word[i]] + ExtractPunctFromWord(word[i + 1:], punct_chars)
    elif i < len(word):
        if word[i] in punct_chars:
            return [word[: i]] + [word[i]]
        else:
            return [word]
    else:
        return [word]

    # if word[0] in punct_chars:
    #     return [word[0]] + ExtractPunctFromWord(word[1 :], punct_chars)
    # else:
    #     return [word[0] + ExtractPunctFromWord(word[1 :], punct_chars)]


def ExtractWords(line, word_chars):
    bad_chars = [
        c for c in list(string.printable)
        if c not in set(list(word_chars))
    ]
    if len(bad_chars) == 0:
        return line
    else:
        return RemoveChars(line, bad_chars)


def RemoveChars(line, to_remove):
    if len(to_remove) == 1:
        return line.split(to_remove[0])
    intermediate = line.split(to_remove[0])
    tokens = []
    for word in intermediate:
        tokens = tokens + RemoveChars(word, to_remove[1 :])
    if tokens.count('') > 0:
        tokens.remove('')
    return tokens


def RemoveSingletons(trees):
    # find words that occur only once
    counts = defaultdict(int)
    singletons = set()
    for t in trees:
        for w in ExtractWords(t, SemanticChars):
            counts[w] += 1





if __name__ == '__main__':
    w = ExtractWords('Hello! (Here, is a line)', string.ascii_letters + LangChars + '()')
    print ExtractPunct(w, '()')