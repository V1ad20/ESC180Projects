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
    numer = 0
    mag_val_vec1 = 0
    mag_val_vec2 = 0
    vec2_words = vec2.keys()
    for word, occurence in vec1.items():
        if word in vec2_words:
            numer += occurence * vec2[word]
        mag_val_vec1 += occurence ** 2
        
    for occurence in vec2.values():
        mag_val_vec2 += occurence ** 2
        
    if min(mag_val_vec1,mag_val_vec2) == 0:
        return -1
   
    return numer / math.sqrt(mag_val_vec1 * mag_val_vec2)


def build_semantic_descriptors(sentences):
    masterdict = {}
    for sentence in sentences:
        sentencedict = {}
        for word in sentence:
            if word in sentencedict:
                sentencedict[word] += 1
            else:
                sentencedict[word] = 1

        newdict = {}
        for word in sentencedict.keys():
            dict_copy = sentencedict.copy()
            dict_copy.pop(word)
            newdict[word] = dict_copy

        for word in newdict.keys():
            if word in masterdict:
                for possible_synonym in newdict[word]:
                    if possible_synonym in masterdict[word]:
                        masterdict[word][possible_synonym] += newdict[word][possible_synonym]
                    else:
                        masterdict[word][possible_synonym] = 1
            else:
                masterdict[word] = newdict[word]

    return masterdict


def build_semantic_descriptors_from_files(filenames):
    filtered_sentences = []
    for filename in filenames:
        text = open(filename, "r", encoding = "latin1").read()
        text = text.lower()
        text = text.replace("!", ".")
        text = text.replace("?", ".")
        text = text.replace("\n"," ")
        sentences = text.split(". ")
        for sentence in sentences:
            sentence = sentence.replace(","," ")
            sentence = sentence.replace(":"," ")
            sentence = sentence.replace(";"," ")
            sentence = sentence.replace("--"," ")
            sentence = sentence.replace("-"," ")
            sentence = sentence.replace("  "," ")
            filtered_sentences.append(sentence.split(" "))
    return build_semantic_descriptors(filtered_sentences)

def most_similar_word(word, choices, semantic_descriptors, similarity_fn):
    similarity_scores = []
    word_vec = {}
    if word in semantic_descriptors:
        word_vec = semantic_descriptors[word]

    for choice in choices:
        choice_vec = {}
        if choice in semantic_descriptors:
            choice_vec = semantic_descriptors[choice]
        
        similarity_scores.append(similarity_fn(word_vec, choice_vec))
    return choices[similarity_scores.index(max(similarity_scores))]


def run_similarity_test(filename, semantic_descriptors, similarity_fn):
    word = ""
    answer = ""
    choices = []
    temp = []

    questions = 0
    correct = 0

    text = open(filename, "r", encoding = "latin1")
    print("hi")
    for line in text.readlines():
        line = line.replace("\n","")
        temp = line.split(" ")
        word = temp[0]
        answer = temp[1]
        choices = temp[2:]
        print(answer, answer, choices)

        questions += 1

        if answer == most_similar_word(word, choices, semantic_descriptors, similarity_fn):
            correct += 1
    
    return (correct / questions) * 100

sem_descriptors = build_semantic_descriptors_from_files(["wp.txt","sw.txt"])
res = run_similarity_test("test.txt", sem_descriptors, cosine_similarity)
print(res, "of the guesses were correct")