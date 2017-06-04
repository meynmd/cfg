from tree import Tree
from collections import defaultdict
import sys

def binarize(tree): 
    # terminal
    if tree.word is not None:
        return tree
    if len(tree.subs) > 2:
        label = tree.label
        span = [tree.span[0]+1, tree.span[1]]
        if label[-1] != '\'':
            label += '\''         
        sub = Tree(label, span, subs = tree.subs[1:])        
        tree.subs = [tree.subs[0], sub]    
    for t in tree.subs:                
        binarize(t)
    return tree



if __name__=='__main__':    
    for i, line in enumerate(sys.stdin):
        print binarize(Tree.parse(line.strip(), trunc=True))
