# Spell checker
# snello nuovo

# scrivo parola
# mi da una lista di possibili parole corrette


import math

##########################################################################
def read_words(filename):
    """Read the content of a file.

    Return a dictionary mapping (lowercase) words to probabilities.

    """
    f = open(filename)
    counters = {}   # empty dictionary
    total = 0
    for line in f:
        for word in line.lower().split():   
            # lower per togliere il maiuscolo
            # slpit dove c'è lo spazio divide le parole


            # exclude strings including non-alphabetic characters 
            # example    power--ad lo toglie
            if word.isalpha():
                if word in counters:
                    counters[word] += 1
                else:
                    counters[word] = 1
                total += 1
    f.close()
    priors = {}
    for word in counters:
        priors[word] = counters[word] / total
    return priors


##########################################################################
def binomial_coefficient(n, k):
    """Binomial coefficient 'n choose k'."""
    denominator = math.factorial(k) * math.factorial(n - k)
    return math.factorial(n) // denominator


##########################################################################
# e # errori
# n length della parola
def error_probability(e, n, q):
    """Probability of e errors on a word of length n."""
    binc = binomial_coefficient(n, e)
    return binc * (q ** e) * ((1 - q) ** (n - e))


#   3   #########################################################################
# gli do una parola e crea una lista di parole simili che potrei aver digitato (1 errore)

def edit1(word):
    """Set of single editings starting from the given word."""
    n = len(word)
    letters = "abcdefghijklmnopqrstuvwxyz"  # for every letter in the alphabeth
    variations = set()

    # guardo tutte le possibili

    # Deletions
    for i in range(n):
        newword = word[:i] + word[(i + 1):]  # xk non posso modificare una lista
        variations.add(newword)
    # Substitutions
    for i in range(n):
        for l in letters:
            if l != word[i]:
                newword = word[:i] + l + word[(i + 1):]
                variations.add(newword)
    # Insertions
    for i in range(n + 1):  # n+1 position in wich insert a new letter
        for l in letters:
            newword = word[:i] + l + word[i:]
            variations.add(newword)
    # Inversions
    # invert two consecutive characters in a word
    for i in range(n - 1):
        newword = word[:i] + word[i + 1] + word[i] + word[(i + 2):]
        variations.add(newword)
    return variations


#   2   #########################################################################
# cicla edit1 k volte in modo da avere anche le varianti con più di un errore
# per parola

def edit_k(word, k):
    variations = {word} # set for now with the word
    # uso il set per non avere duplicati
    for i in range(k):  # per ciclare edit1 k volte
        newvars = set() 
        for v in variations: # v assume il valore di ogni elemento di variation
            # per mandare il set di variations che ho un'altra volta a edit1
            # per farlo modificare ancora
            # questo for di ogni singola variation che ho in memoria fa un'altra variante
            newvars |= edit1(v)  # unione  unisce le vecchine newvars con quelle computate da edit1(v)
        variations = newvars
    return variations


#   1   #########################################################################
# Return a list of possible corrections starting from the most likely.

def correct_word(word, maxerrors, q, top):
    candidates = []  # lista gli elementi solo ordinati
    for e in range(maxerrors + 1):
        variations = edit_k(word, e)    # <---------
        for c in variations:
            if c in DICTIONARY:
                p_c = DICTIONARY[c]
                p_wc = error_probability(e, len(c), q)
                score = p_wc * p_c
                candidates.append((score, c))  # add a tuple containing the score and the candidate itself
    candidates.sort(reverse=True)  # we sort them in reverse order
    return candidates[:top]  # take first candidates from first to top


##########################################################################
# Load the dictionary.
DICTIONARY = read_words("big.txt")

# Correct the word and print the corrections.
word = input("Enter the word: ")

# word, max numb of errors, q prob of typing wrong, intrested in top 5 corrections
candidates = correct_word(word, 2, 0.01, 5)   # <-----------------


for score, c in candidates:
    print(c)        # print the corrections





