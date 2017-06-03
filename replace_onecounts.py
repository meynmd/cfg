from __future__ import print_function
from preprocess import *

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

    return new_trees, counts


def TreeToString(tree):
    # remove spaces between parentheses
    special = ['(', ')']
    output = ''
    for i in range(len(tree)):
        output += tree[i]
        if i == len(tree) - 1:
            continue
        else:
            if tree[i] in special and tree[i + 1] in special:
                continue
            if tree[i] == '(' or tree[i + 1] == ')':
                continue
            output += ' '

    return output


if __name__ == '__main__':
    trees = sys.stdin.readlines()
    trees, counts = RemoveSingletons(trees)

    for t in trees:
        line = TreeToString(t)
        # line = t[0]
        # for i in range(len(t)):
        #     line += t[i] + ' '
        #     # if t[i] == '(' or t[i] == ')':
        #     #     line += t[i]
        #     # else:
        #     #     line += t[i] + ' '
        print(line)

    for w, c in counts.items():
        if c > 1:
            print(w, file = sys.stderr)