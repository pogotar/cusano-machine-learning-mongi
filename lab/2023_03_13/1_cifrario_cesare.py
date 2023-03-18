# -*- coding: utf-8 -*-
"""
Created on Mon Mar 13 14:10:27 2023

@author: pmong
"""

# cifrario di cesare
# ASCII tells me how in binary is encoded every character

#   1   ###################################################
#  word  ,  how much to shift the letters

def encrypt(input_str, key):
    output_str = ''     # creo una stringa vuota (anche "  "  va bene)
    for c in input_str:     # prendo ogni carattere dell'input
        if c.isalpha(): # TRUE if all characters in the String is an alphabet.
            # shift the caracter to encrypt it, ORD mi da numeroASCII
            output_str += chr((ord(c) - ord('a') + key) % 26 + ord('a'))
            # ord('c') - ord('a')  per mettere a al valore 0
            # così se sforo oltre il 26 riparto da 0, il resto è sempre 0 se sforo mi dice di quanto
            # riaggiungo a
            # chr mi da il return del carattere
        else:
            output_str += c  
            """nel senso che aggiunge c alla fine (tipo append) 
            se carattere stranolo aggiunge senza fare niente"""
    return output_str


#   2   ###################################################
# decrypt function

def decrypt(input_str, key):
    return encrypt(input_str, -key)


#   MAIN   ###################################################
first_str = 'gallia'
key = 4

print('key = ', key)
first_enc_str = encrypt(first_str, key)
first_dec_str = decrypt(first_enc_str, key)
print(first_enc_str)
print(first_dec_str)

# RANGE    range(0) mi da una lista da 0 a 100
#          range(100,50, -1)  parte da 100 arriva a 50 con passo -1
# for i in range(5):
#     print(i)
#   
# printa 1  2  3  4  5

# SPLIT
# "hi people I'm Paolo"
# "hi people I'm Paolo".split()
# fa il return di una lista divisa dove ho lo spazio
# ('x') se voglio che vengalo separate ogni x

# IN
# lint = ["one", "ciao"]
# "ciao" in list
# fa il return True


# if I don't know the key do decryption by brute force knowing a dictionary
dictionary = []  # define a LIST

encrypted_str ="hvs aowb zsggcb ct hvwfhm-twjs msofg ct ow fsgsofqv wg hvoh hvs vofr dfcpzsag ofs sogm obr hvs sogm dfcpzsag ofs vofr. hvs asbhoz opwzwhwsg ct o tcif-msof-czr hvoh ks hoys tcf ufobhsr – fsqcubwnwbu o toqs, zwthwbu o dsbqwz, kozywbu oqfcgg o fcca, obgksfwbu o eisghwcb – wb toqh gczjs gcas ct hvs vofrsgh sbuwbssfwbu dfcpzsag sjsf qcbqswjsr... og hvs bsk usbsfohwcb ct wbhszzwusbh rsjwqsg oddsofg, wh kwzz ps hvs ghcqy obozmghg obr dshfcqvsawqoz sbuwbssfg obr dofczs pcofr asapsfg kvc ofs wb robusf ct pswbu fsdzoqsr pm aoqvwbsg. hvs uofrsbsfg, fsqsdhwcbwghg, obr qccyg ofs gsqifs wb hvswf xcpg tcf rsqorsg hc qcas."

with open('dictionary.txt') as dictionary_file:
    # you are using the open() function to open a file named dictionary.txt 
    # and assign it to a variable named dictionary_file.
    for line in dictionary_file:
        dictionary.append(line.rstrip()) # rstrip per rimuovere il \n nel file

max_correct_word_count = 0
for key_new in range(26):
    decrypted_str = decrypt(encrypted_str, key_new)
    splitted_decrypted_str = decrypted_str.split() # trasforma la stringa in una lista
    
    correct_word_count = 0
    for word in splitted_decrypted_str:
        if word in dictionary:
            correct_word_count += 1
    if correct_word_count > max_correct_word_count:
        max_correct_word_count = correct_word_count
        correct_key = key_new
    print(f'Possible decrypted text guess: {decrypted_str}; correct_word_guess:{(correct_word_count / len(splitted_decrypted_str)*100)}%') # f fa interpretare quello dentro {} come codice
            
print(f'final decrypted text guess: {decrypt(encrypted_str, correct_key)}')

# example = {letter: 0 for letter in 'abcde'}    # creo un dizionario a:0 b:0

import string # per usare .string sotto
letter_freq = {letter: 0 for letter in string.ascii_lowercase} # per non dover scrivere tutte le lettere

for word in dictionary:     
    for letter in word:
        if letter.isalpha():
            letter_freq[letter] += 1

# ho fatto il character count nella variabile chiamata dizionario            
print(letter_freq)


#   PLOT   #################################################################### 
import matplotlib.pyplot as plt

fig = plt.figure(figsize=(8,6))

plt.bar(list(letter_freq.keys()), list(letter_freq.values()), align ='center' )  # x, y, align
# to plot bar plots
# list creates a new list or if it has a parameter convert into a list the parameter
plt.title('Letter frequencies in dictionary file')
plt.show() # to display it, new window pops up

#########################################################################
# ora so che la lettera più comune è la e, posso provare a decriptare guardando
# la lettera più comune

last_enc_str = "fc vlrqe, qeolrdelrq xii efpqlov, exa exa x zexjmflk ql pqxka rm clo fq; ql pelt x alryqfkd tloia qexq x zefia zxk qefkh; xka, mlppfyiv, al fq moxzqfzxiiv; vlr tlriak’q zlkpqxkqiv ork xzolpp clihp qlaxv tel zixfj qexq “x zefia alk’q hklt xkvqefkd.” x zefia’p yoxfk pqxoqp crkzqflkfkd xq yfoqe; xka exp, xjlkdpq fqp jxkv fkcxkq zlkslirqflkp, qelrpxkap lc alojxkq xqljp, fkql tefze dla exp mrq x jvpqfz mlppfyfifqv clo klqfzfkd xk xariq’p xzq, xka cfdrofkd lrq fqp mromloq."
letter_freq2 = {letter: 0 for letter in string.ascii_lowercase}


for letter in last_enc_str:
    if letter.isalpha():
        letter_freq2[letter] += 1
        
plt.bar(list(letter_freq2.keys()), list(letter_freq2.values()), align ='center' )  # x, y, align
plt.title('Letter frequencies in second string')
plt.show() 

prob_key = ord("q") - ord("e")  # usando il più prob non viene, fatto apposta
# la e corrisponde alla b usata 0 volte
rigth_key = 23
last_decrypted_str = decrypt(last_enc_str, rigth_key)
print(last_decrypted_str)
        

 

