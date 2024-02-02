import random as rand
import math

def primitive_random_generator(vocab, text_len):
    text = []
    for i in range(text_len):
        r = rand.randint(0, len(vocab) - 1)
        text.append(vocab[r])
    return text

def p_count(text):
    pair = {}

    for i in range(text_len - 1):
        w_1 = text[i]
        w_2 = text[i + 1]
        if (w_1, w_2) in pair:
            pair[(w_1, w_2)] += 1
        else:
            pair[(w_1, w_2)] = 1
    return pair

def q_count(text):
    quadruple = {}
    for i in range(text_len - 4):
        w_1 = text[i]
        w_2 = text[i + 1]
        w_3 = text[i + 2]
        w_4 = text[i + 4]
        if (w_1, w_2, w_3, w_4) in quadruple:
            quadruple[(w_1, w_2, w_3, w_4)] += 1
        else:
            quadruple[(w_1, w_2, w_3, w_4)] = 1
    return quadruple



length = 100000
vocab = ["A", "C", "G", "T"]
text = primitive_random_generator(vocab, length)

#max_gram = math.floor(math.sqrt(text_len/len(vocab)))

#grams = []

#for gram in range(max_gram, 2, -1):
    #grams[]

    #for i in range(text_len - gram + 1):


#I think I only want (2^n)-grams for an integer n
#obtaining quantity of 2- and 4-grams
#pair = {}
#quadruple = {}
#hexadeciple = {}

print(text)
print("text:", len(text))
index = {}

index_size = 0

iter = 0
while len(text) > math.log2(length):
    text_len = len(text)
    pair = {}
    pair = p_count(text)



    #ok, now I can try to cover the text just with bigrams
    index = {}
    i = 0
    for k in pair.keys():
        #index[k] = "".join(k)
        index[k] = str(iter) + "_" + str(i)
        i += 1

    #print(index)


    print("index:", len(index))
    index_size += len(index)
    print(index)

    for i in range(text_len - 1):
        w_1 = text[i]
        w_2 = text[i + 1]
        if w_1 != "":
            if (w_1, w_2) in index:
                text[i] = index[(w_1, w_2)]
                text[i+1] = ""

    for i in text:
        if i == "":
            text.remove(i)

    print("text:", len(text))
    iter += 1

print("Index size:", index_size)
print("(Index+final_text)/original_text", (index_size + len(text))/length)
print(text)





















