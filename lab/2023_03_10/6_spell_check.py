# Spell checker
# spiegazione vecchia

# w   typed word      pyton
# c   correct word    phyton

"""
I want to 

max with respect to c  P(c|w) = p(w|C)*P(C) / p(w)

P(C)     language model   (pick lot of books and estimate p for every word)
p(w|C)   error model       scrivo c al posto di w   
p(w)     non mi cambia la mia massimizzazione rispetto a c quindi la tolgo

q        chance of making a mistake for every letter user type
if errora are independent has a binomial distribution  p(w|C) = (n   e)  q^e  (1-q)^(n-e)
n lunghezza della parola     e # di errori

"""
import math


# A simple spell corrector.  Inspired by the one found on Peter
# Norvig's page (https://norvig.com/spell-correct.html).
#
# It finds the corrcetion c maximizing the conditional probability
# P(c|w) that c is the "right" word given that the user entered w.
#
# By Bayes law:
#
# P(c|w) = P(w|c) P(c) / P(w)
#
# About these probabilities:
#
# - P(w|c) is modeled as a function of edits needed to tranform w into
#   c.  The number of edits is supposed to follow a binomial
#   distribution.
#
# - P(c) is the "language model", telling us how much c is likely to
#   occur.  This is estimated from data.
#
# - P(w) is the same for all c and can be ignored.
#
# The file big.txt is used to estimate P(c).  It can be downloaded
# from Norvig's page https://norvig.com/big.txt Any other large file
# of text could be used.


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


def binomial_coefficient(n, k):
    """Binomial coefficient 'n choose k'."""
    denominator = math.factorial(k) * math.factorial(n - k)
    return math.factorial(n) // denominator


# e # errori
# n length della parola
def error_probability(e, n, q):
    """Probability of e errors on a word of length n."""
    binc = binomial_coefficient(n, e)
    return binc * (q ** e) * ((1 - q) ** (n - e))


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


# cicla edit1 k volte in modo da avere anche le varianti con più di un errore
# per parola
def edit_k(word, k):
    """Set of editings obtained with k operations from the given word."""
    variations = {word} # set of word with 0 mistakes (the word we have digitated)
    for i in range(k):  # per ciclare edit1
        newvars = set() # set anche lui 
        for v in variations:
            newvars |= edit1(v)  # unione  unisce le vecchine newvars con quelle computate da edit1(v)
        variations = newvars
    return variations

# q prob of making mistake in a single position
def correct_word(word, maxerrors, q, top):
    """Correct the word.

    Return a list of possible corrections starting from the most
    likely.
    """
    candidates = []  # lista gli elementi solo ordinati
    for e in range(maxerrors + 1):
        variations = edit_k(word, e)
        for c in variations:
            if c in DICTIONARY:
                p_c = DICTIONARY[c]
                p_wc = error_probability(e, len(c), q)
                score = p_wc * p_c
                candidates.append((score, c))  # add a tuple containing the score and the candidate itself
    candidates.sort(reverse=True)  # we sort them in reverse order
    return candidates[:top]  # take first candidates from first to top


# Load the dictionary.
DICTIONARY = read_words("big.txt")

# Correct the word and print the corrections.
word = input("Enter the word: ")
candidates = correct_word(word, 2, 0.01, 5)  # max numb of errors, q, intrested in top 5 corrections
for score, c in candidates:
    print(c)        # print the corrections





