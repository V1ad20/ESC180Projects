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

# print(cosine_similarity({"a": 1, "b": 2, "c": 3}, {"b": 4, "c": 5, "d": 6}))

# dict = {"a": 1, "b": 2, "c": 3}
# print(list(dict.keys()))
# print(list(dict.values()))
# print(list(dict.items()))

def build_semantic_descriptors(sentences):
    d = {}
    # for sentence in sentences:
    #     for word in sentence:
    #         if not(word in list(d.keys())):
    #             d[word] = {}
    #         for sameword in sentence:
    #             if not(sameword == word):
    #                 if not(sameword in list(d[word].keys())):
    #                     d[word][sameword] = 1
    #                 else:
    #                     d[word][sameword] += 1
    # return d
    for sentence in sentences:
        for i in range(0, len(sentence)):
            if not(sentence[i] in list(d.keys())):
                d[sentence[i]] = {}

            for j in range(0, len(sentence)):
                if i != j:
                    if not(sentence[j] in list(d[sentence[i]].keys())):
                        d[sentence[i]][sentence[j]] = 1
                    else:
                        d[sentence[i]][sentence[j]] += 1
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
        text = open(filename, "r", encoding = "latin1").read()
        text = text.replace("!", ".").replace("?", ".").replace("\n"," ")
        sentences = text.split(". ")
        for sentence in sentences:
            filtered_sentences.append(sentence.replace(",","").replace(":","").replace(";","").replace("--","").replace("-","").replace("  "," ").split(" "))
    return build_semantic_descriptors(filtered_sentences)

# print(build_semantic_descriptors_from_files(["wp.txt"])["consequently"])

def most_similar_word(word, choices, semantic_descriptors, similarity_fn):
    similarity_scores = []
    for choice in choices:
        similarity_scores.append(similarity_fn(semantic_descriptors[word], semantic_descriptors[choice]))
    return choices[similarity_scores.index(max(similarity_scores))]

# print(most_similar_word("duty",["journey", "serious", "tidy"],build_semantic_descriptors_from_files(["test.txt"]), cosine_similarity))

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
        temp = line.split(" ")
        word = temp[0]
        answer = temp[1]
        choices = temp[2:]
        print(answer, answer, choices)

        questions += 1

        if answer == most_similar_word(word, choices, semantic_descriptors, similarity_fn):
            correct += 1
    
    return (correct / questions) * 100

sem_descriptors = build_semantic_descriptors_from_files(["wp.txt", "sw.txt"])
# print(sem_descriptors)
# res = run_similarity_test("test.txt", sem_descriptors, cosine_similarity)
# print(res, "of the guesses were correct")
        
# run_similarity_test("test.txt", 1, 1)

# L = build_semantic_descriptors_from_files(["wp.txt"])
# print(build_semantic_descriptors(L))




# def test_cosine_similarity(self):
#     self.assertAlmostEqual(syn.cosine_similarity({"a": 1, "b": 2, "c": 3}, {"b": 4, "c": 5, "d": 6}), 0.7, places = 2)


# def test_build_semantic_descriptors(self):
#     sentences = [["i", "am", "a", "sick", "man"],
#     ["i", "am", "a", "spiteful", "man"],
#     ["i", "am", "an", "unattractive", "man"],
#     ["i", "believe", "my", "liver", "is", "diseased"],
#     ["however", "i", "know", "nothing", "at", "all", "about", "my",
#     "disease", "and", "do", "not", "know", "for", "certain", "what", "ails", "me"]]
#     sem_desc = syn.build_semantic_descriptors(sentences)
#     self.assertEqual(sem_desc["man"], {"i": 3, "am": 3, "a": 2, "sick": 1, "spiteful": 1, "an": 1,"unattractive": 1})
#     self.assertEqual(sem_desc["liver"],  {"i": 1, "believe": 1, "my": 1, "is": 1, "diseased": 1})


# def test_build_semantic_descriptors_from_files(self):
#     f1 = open("text1.txt", "w")
#     f2 = open("text2.txt", "w")
#     f1.write("I am a sick man. I am a spiteful man. I am an unattractive man. I believe my liver is diseased.\n")
#     f2.write("However, I know nothing at all about my disease, and do not know for certain what ails me.")
#     f1.close()
#     f2.close()

#     sem_desc = syn.build_semantic_descriptors_from_files(["text1.txt", "text2.txt"])
#     self.assertEqual(sem_desc["man"], {"i": 3, "am": 3, "a": 2, "sick": 1, "spiteful": 1, "an": 1,
# "unattractive": 1})
#     self.assertEqual(sem_desc["liver"],  {"i": 1, "believe": 1, "my": 1, "is": 1, "diseased": 1})

#     self.assertEqual(sem_desc["nothing"]["ails"], 1)

# @weight(1)
# @visibility("visible")
# def test_most_similar_word(self):
#     sem_desc = {"dog": {"cat": 1, "food": 1},
#                 "cat": {"dog": 1}}
#     self.assertEqual(syn.most_similar_word("dog", ["cat", "rat"], sem_desc, syn.cosine_similarity), "cat")


# def test_run_similarity_test(self):
#     f1 = open("text1.txt", "w")
#     f2 = open("text2.txt", "w")
#     f1.write("I am a sick man. I am a spiteful man. I am an unattractive man. I believe my liver is diseased\n")
#     f2.write("However, I know nothing at all about my disease, and do not know for certain what ails me.")
#     f1.close()
#     f2.close()

#     f3 = open("test.txt", "w")
#     f3.write("man i liver i\nsick man certain man")
#     f3.close()
#     sem_desc = syn.build_semantic_descriptors_from_files(["text1.txt", "text2.txt"])
#     res = syn.run_similarity_test("test.txt", sem_desc, syn.cosine_similarity)
#     self.assertEqual(res, 100.0)