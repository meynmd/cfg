from collections import defaultdict
from tree import *
import sys

def LearnGrammar(trees):
    # count occurrences of each production
    counts = defaultdict(lambda: defaultdict(int))
    for tree in trees:
        CountProductions(tree, counts)

    # compute probabilities
    prob = defaultdict(lambda: defaultdict(float))
    for lhs, rhs_count in counts.items():
        total = float(sum(rhs_count.values()))
        for rhs, count in rhs_count.items():
            prob[lhs][rhs] = float(count) / total

    return prob


def CountProductions(tree, counts):
    if tree.subs == None:
        return
    rhs = tuple(s.label for s in tree.subs)
    counts[tree.label][rhs] += 1
    # for s in tree.subs:
    #     counts[tree.label][s.label] += 1
    for s in tree.subs:
        CountProductions(s, counts)


def PrintGrammar(grammar):
    for lhs, rhs_prob in grammar.items():
        for rhs, prob in rhs_prob.items():
            print '{} ->'.format(lhs),
            for r in rhs:
                print '{}'.format(r),
            print '# {}'.format(prob)


if __name__ == '__main__':
    #with open('train.trees', 'r') as fp:
    with sys.stdin as fp:
        lines = fp.readlines()
        trees = []
        for line in lines:
            trees.append(Tree.parse(line))
        g = LearnGrammar(trees)
        PrintGrammar(g)