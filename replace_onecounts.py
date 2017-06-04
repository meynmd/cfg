from __future__ import print_function
from collections import defaultdict
import sys

if __name__ == '__main__':
    words_freq = defaultdict(int)
    lines = []
    for line in sys.stdin:
        lines += [line]
        for seg in line.split():
            seg = seg.strip()
            if seg[-1] == ')':
                words_freq[seg.replace(')','')] += 1        

    for line in lines:
        mod_line = ''
        for seg in line.split():
            word = seg.replace(')','')
            if seg[-1] != ')' or words_freq[word] > 1:
                mod_line += seg + ' '
            else:                                
                n = seg.count(')')
                mod_line += '<unk>' + ')'*n + ' '
        print(mod_line)

    for wrd in words_freq:
        if words_freq[wrd] > 1:
            print(wrd, file = sys.stderr)






