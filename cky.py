from collections import defaultdict
import sys


def cky(grammer, words, vocab = None, lhs = 'TOP'):
    if len(words) == 1:
        trml = words[0]
        return max([(grammer[trml][lhs], lhs) for lhs in grammer[trml]])

    score = []
    for i in xrange(1, len(words)):
        lrhs_prob, lrhs = cky(grammer, words[:i], vocab, lhs)
        rrhs_prob, rrhs = cky(grammer, words[i:], vocab, lhs)
        rhs = lrhs + ' ' + rrhs
        score += [max([tuple(grammer[rhs][lhs]*lrhs_prob*rrhs_prob, lhs) for lhs in grammer[rhs]])]
    return max(score)

def build_grammer(filename):
    p_lhs_rhs = defaultdict(lambda:defaultdict(float))
    with open(filename, 'r') as fp:
        for line in fp:
            seg1 = line.split('->')
            seg2 = seg1[1].split('#')
            lhs = seg1[0].strip()
            rhs = seg2[0].strip()
            prob = float(seg2[1].strip())
            p_lhs_rhs[rhs][lhs] = prob
    return p_lhs_rhs




if __name__=='__main__':
    if len(sys.argv) < 2:
        print 'you need to provide a pcfg grammer as an input'        
    else:
        grammer_filename = sys.argv[1]
        if len(sys.argv) == 3:
            train_dict_filename = sys.argv[2]
            with open(train_dict_filename, 'r') as fp:
                vocab = fp.readlines()
        else:
            vocab = None

    p_lhs_rhs = build_grammer(grammer_filename)
    
    for line in sys.stdin:
        print cky(p_lhs_rhs, line.strip().split(), vocab)


    

