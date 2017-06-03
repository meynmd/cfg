import string
import sys
from collections import defaultdict

LangChars = string.ascii_letters + ',.?!\''

def ExtractPunct(words, punct_chars):
    result = []
    for word in words:
        t = [x for x in ExtractPunctFromWord(word, punct_chars) if len(x) > 0]
        result += t
    return result


def ExtractPunctFromWord(word, punct_chars):
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
    for t in trees:
        for w in ExtractWords(t, LangChars):
            counts[w] += 1
    singletons = [w for w in counts.keys() if counts[w] < 2]

    # rewrite the trees with <unk>
    new_trees = []
    for tree in trees:
        result = []
        tokens = ExtractWords(tree, LangChars + '()')
        tokens = ExtractPunct(tokens, '()')
        for t in tokens:
            if t not in singletons:
                result.append(t)
            else:
                result.append('<unk>')
        new_trees.append(result)

    return new_trees

if __name__ == '__main__':
    trees = sys.stdin.readlines()
    trees = RemoveSingletons(trees)
    for t in trees:
        print(t)