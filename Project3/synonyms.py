"""ESC180 Project 3
By: Vlad Surdu and Seok-Gyu (Brian) Kang
Due: 12/05/2022"""

import math


def norm(vec):
    '''Return the norm of a vector stored as a dictionary, as 
    described in the handout for Project 3.
    '''
    
    sum_of_squares = 0.0  
    for x in vec:
        sum_of_squares += vec[x] * vec[x]
    
    return math.sqrt(sum_of_squares)


def cosine_similarity(vec1, vec2):
    pass


# dict = {"a": 1, "b": 2, "c": 3}
# print(list(dict.keys()))
# print(list(dict.values()))
# print(list(dict.items()))


def build_semantic_descriptors(sentences):
    d = {}
    for sentence in sentences:
        for word in sentence:
            if not(word in list(d.keys())):
                d[word] = {}
            for sameword in sentence:
                if not(sameword == word):
                    if not(sameword in list(d[word].keys())):
                        d[word][sameword] = 1
                    else:
                        d[word][sameword] += 1
    return d

# L = [["i", "am", "a", "sick", "man"],
# ["i", "am", "a", "spiteful", "man"],
# ["i", "am", "an", "unattractive", "man"],
# ["i", "believe", "my", "liver", "is", "diseased"],
# ["however", "i", "know", "nothing", "at", "all", "about", "my",
# "disease", "and", "do", "not", "know", "for", "certain", "what", "ails", "me"]]
# print(build_semantic_descriptors(L))



def build_semantic_descriptors_from_files(filenames):
    filtered_sentences = []
    for filename in filenames:
        text = open(filename, "r", econding = "latin1").read()
        text = text.replace("!", ".").replace("?", ".")
        sentences = text.split(". ")
        for sentence in sentences:
            filtered_sentences.append(sentence.replace(",","").replace(":","").replace(";","").replace("--","").replace("-","").replace("  "," ").split(" "))
    return build_semantic_descriptors(filtered_sentences)

def most_similar_word(word, choices, semantic_descriptors, similarity_fn):
    pass

def run_similarity_test(filename, semantic_descriptors, similarity_fn):
    pass