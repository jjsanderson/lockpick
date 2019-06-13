import io
with io.open('1000english.txt', 'r', encoding='utf8') as f:
    english_words = set(word.strip().lower() for word in f)

with io.open('1000welsh.txt', 'r', encoding='utf8') as g:
    welsh_words = set(word.strip().lower() for word in g)

def is_english_word(word):
    return word.lower() in english_words
	
def is_welsh_word(word):
    return word.lower() in welsh_words

wheel1 = ('s', 't', 'd', 'm', 'r', 'f', 'b', 'l', 'p', 'w')
wheel2 = ('w', 'r', 'y', 'u', 'a', 'i', 'o', 'l', 'e', 'h')
wheel3 = ('r', 'm', 't', 'n', 's', 'k', 'o', 'a', 'l', 'e')
wheel4 = ('g', 'k', 'm', 's', 't', 'e', 'p', 'y', 'l', 'd')

i = 0

for w1 in wheel1:
    for w2 in wheel2:
        for w3 in wheel3:
            for w4 in wheel4:
                testword = w1+w2+w3+w4
                if (is_english_word(testword) or is_welsh_word(testword)):
                    print(i, testword)
                    i += 1
