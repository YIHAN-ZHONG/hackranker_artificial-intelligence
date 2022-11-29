#an introduction to sentence segmentation

import re
def get_sentences(paragraph):

    pattern = re.compile(r'(?!\s)(\".*\")?(.{,3}[.]){0,}[^.!?]{4,}?([.]|[!]|[?])')
    matches = re.finditer(pattern, paragraph)#pattern.finditer(paragraph)
    #matches = re.findall(pattern, paragraph)  # pattern.finditer(paragraph)
    return matches

if __name__ == '__main__':
    paragraph = input()
    sentences = get_sentences(paragraph)
    for sentence in sentences:
        print(sentence.group())
