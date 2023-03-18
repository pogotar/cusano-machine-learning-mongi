h =  "hello"
w = "word"

print(h+w)          # helloword
print(h+" " +w)     # hello word
print(4*w)          # wordwordwordword

#####

print(h[0])   # h
print(h[-1])  # o   va all'indietro
print(h[-2])  # l

#########

print(h[1:3]) # el
print(h[1:-1]) 
print(h[:3])    # from beginning up to the end
print(h[:])   # prendi tutto
print(len(h))  # length

# once I define a string I cn't change it   
# can't do h[0] = "H"
# devo fare

h = "H" + h[1:]
print(h)

##################################################################
# list instead of string are mutable

l = [2, 3, 5, 7, 11, 13, 17]
print(len(l))
print(l[0])

l[2] = -3
print(l)
l.append(100)
print(l)

m = l
# now if I change l also m changes

print(sum(l))
print(min(l))
print(max(l))

l.sort()    # works also for strings
print(l)

l.sort(reverse = True)
print(l)

S = ['coconut', 'apple']
S.sort()
print(S)

#####################################################################à
# tuple is the same as a list but once defined can't be changed

t = (19, 31, "hl", 3.1)

# se voglio fare cambiamenti trasformo un' altra variabile in lista

l = list(t)

print(l)



t = (2, 'hl')
a, b = t
print(a)
print(b)

a, b, c = 2, 3, 4

##############################################################ààà



