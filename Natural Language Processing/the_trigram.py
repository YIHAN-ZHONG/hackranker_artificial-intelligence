import re



def get_sentences(paragraph):

    pattern = re.compile(r'(?!\s)(\".*\")?(.{,3}[.]){0,}[^.!?]{4,}?([.]|[!]|[?])')
    matches = re.finditer(pattern, paragraph)#pattern.finditer(paragraph)
    sentences=[ ]
    for match in matches:
        sentences.append(match.group())

    
    return sentences




def pre_processing(x):
    x=x.replace('.','')
    x=x.replace(',','')
    x=x.strip()
    x=x.lower()
    return x 

someText = "I love to dance. I like to dance I. like to play chess."

def trigrams(someText): 
    sentences=get_sentences(someText)

    #sentences=list(filter(lambda x: len(x)>0 ,someText.split('.') )) #filtring the empty sentences. 
    sentences=list(map(pre_processing ,sentences))
    tokens=list(map(lambda x: x.split(' '), sentences ))
    tokens=list(filter(lambda x: len(x)>=3, tokens )) #filtre out the sentences with less then 3 grams
    n_grams={} #hash maping
    for t in tokens:
        for i in range(len(t)-2):
            keys=t[i:i+3]
            keys=" ".join(keys)
            if keys not in n_grams:

                n_grams[keys]=1
            else:
                n_grams[keys]+=1
    m=n_grams[max(n_grams)]
    candidates=list(filter(lambda x: n_grams[x]==m, n_grams))
    
    return candidates[0]         

if __name__ == '__main__':
    s = input()
    n_grams=trigrams(s)
    print(n_grams)

