tmp = []

def anagram(word):
    if len(word) <= 1:
        return word
    else:
        for aux in anagram(word[1:]):
            for i in range(len(word)):
                tmp.append(aux[:i] + word[0:1] + aux[i:])
        return tmp


print(anagram('radio'))
print(len(tmp))
