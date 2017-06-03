from preprocess import *
from itertools import takewhile

def BinarizeTrees(trees):
    #
    new_trees = []
    for tree in trees:
        output = []
        tokens = ExtractWords(tree, LangChars + '()')
        tokens = ExtractPunct(tokens, '()')
        new_trees.append(BinarizeTree(tokens))

    return new_trees


def BinarizeTree(tree, name):
    if len(tree) <= 2:
        return tree

    # the stuff to binarize right now
    nodes = [n for n in takewhile(lambda x: x not in ['(', ')'], tree)]
    if len(nodes > 0):
        output = [nodes[0]]
    else:
        output = []

    if len(nodes) < len(tree):
        # there may be stuff we still have to binarize later
        rest = tree[len(nodes) :]

    if len(nodes) > 2:
        # insert new subtree
        output.append(name + '\'')
        output.append('(')
        output = output + BinarizeTree(nodes[1 :], name + '\'')
        output.append(')')

    if rest[0] == '(':
        output.append(rest[0])
        subtree = takewhile(lambda x: x != ')', rest[1 :])
        output = output + BinarizeTree(subtree)
        output.append(rest[len(subtree) :])

    return output


trees = sys.stdin.readlines()
