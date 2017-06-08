
from collections import defaultdict


def CKY(grammar,sentence):
    len_sentence = len(sentence)
    best_cky = defaultdict(lambda :defaultdict(float))


    for i,tup_word in enumerate(sentence):
        word = tuple([tup_word[1]])
        max_lhs = max(grammar[word], key=grammar[word].get)
        best_cky[max_lhs][(i,i+1)] = grammar[word][max_lhs]





    for diff in range(1,len_sentence):
        updated = False
        for i in range(len_sentence-diff):
            j=i+diff    ####
            best_val = float('-inf')
            for k in range(i + 1, j):

                for rhs in grammar:
                    for lhs,prob in grammar[rhs].items():
                        ############################
                        if len(rhs)==1:
                            continue
                            #temp_val = prob * best_cky[rhs][(i,j)]

                        else:
                            y = tuple([rhs[0]])
                            z = tuple([rhs[1]])
                            temp_val = prob * best_cky[y][(i, k)] * best_cky[z][(k, j)]

                        if temp_val>best_val:
                            best_val = temp_val
                            updated = True
            if updated:
                best_cky[lhs][(i,j)] = best_val


            #################################
            rhs=lhs
            best_val = best_cky[rhs][(i,j)]
            best_lhs = None
            for lhs in grammar[rhs]:
                if len(lhs)==1:
                    prob = best_cky[rhs][(i,j)] * grammar[rhs][lhs]
                    if prob > best_val:
                        best_val = prob
                        best_lhs = lhs


            best_cky[best_lhs][(i,j)] = best_val












    return best_cky












def build_grammar(filename):
    p_lhs_rhs = defaultdict(lambda: defaultdict(float))
    with open(filename, 'r') as fp:
        fp.readline()

        for line in fp:

            seg1 = line.split('->')
            seg2 = seg1[1].split('#')
            lhs = [seg1[0].strip()]
            lhs_tup = tuple(lhs)

            rhs = seg2[0].strip()
            rhs_tup = tuple(rhs.split(' '))
            prob = float(seg2[1].strip())
            p_lhs_rhs[rhs_tup][lhs_tup] = prob
    return p_lhs_rhs





if __name__=='__main__':

    grammar_filename ='toy.pcfg'#'grammar.pcfg.bin'
    lexicon ='train.dict'

    data = ['I need to arrive early today']
    #data = ['I would like to travel to Westchester']

    grammar = build_grammar(grammar_filename)

    #####
    fp=open(lexicon,'r')
    words =[]
    for line in fp.readlines():
        words+=[line[:-1]]

    words=['the','boy','saw','a','girl','I','need','to','arrive','early','today']

    ###############################
    data_list = []
    for line in data:
        temp_list = []
        for word in line.split(' '):
            if word in words:
                tup = (word, word)
            else:
                tup = (word, '<unk>')
            temp_list+=[tup]
        data_list+=[temp_list]



    for word_list in data_list:

        result=CKY(grammar,word_list)
        print('ldfjkdjfkdjf')







