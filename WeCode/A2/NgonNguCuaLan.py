suffix_adjective = ['lios'  [::-1], 'liala' [::-1] ]
suffix_noun      = ['etr'   [::-1], 'etra'  [::-1] ]
suffix_verb      = ['initis'[::-1], 'inites'[::-1] ]

words = list(input().split())

def checkSF(a, b) :
    la = len(a)
    lb = len(b)
    
    if la < lb : return False
    
    for i in range(lb) :
        if a[i] != b[i] :
            return False

    return True

def check() :
    words[::-1]   = words[::]
    words_reverse = []

    for word in words :
        words_reverse.append(word[::-1])    
    
    id         = 0 
    n          = len(words)
    properties = [0] * n

    if n == 1 :
        gr_word = suffix_adjective +  suffix_noun + suffix_verb
        for w in gr_word :
            if checkSF(words_reverse[0], w) :
                return True
        return False 
    
    while (id < n) :
        if   checkSF(words_reverse[id], suffix_verb[0]) :
            properties[id] = 0
        elif checkSF(words_reverse[id], suffix_verb[1]) :
            properties[id] = 1
        else : break
        id += 1
    
    if id >= n : return False
    # print(1)

    if   checkSF(words_reverse[id], suffix_noun[0]) :
        properties[id] = 0
    elif checkSF(words_reverse[id], suffix_noun[1]) :
        properties[id] = 1
    else : return False

    id += 1

    # print(2)
    while (id < n) :
        if   checkSF(words_reverse[id], suffix_adjective[0]) :
            properties[id] = 0
        elif checkSF(words_reverse[id], suffix_adjective[1]) :
            properties[id] = 1
        else : return False
        id += 1
    # print(3)
    for i in range(1,n) :
        if properties[i] != properties[i-1] :
            return False
    # print(4)
    
    return True

if check() :
    print("YES")
else :
    print("NO")