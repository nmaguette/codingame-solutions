from collections import Counter

def wordfrequencies(text):
    text2 = ""
    for letter in text:  # suppression ponctuation
        if letter.isalpha():
            text2 += letter.lower()
        else:
            text2 += ' '

    list1 = text2.split()
    set1 = set(list1)  # suppression des occurences multiples d'un même mot

    # ---------------- resolution using the Counter module --------------
    count = Counter(list1)
    print("with counter :", count)
    count = list(count.items())
    print("with counter convert to list:", count)
    # ---------------- end of resolution using Counter -------------------

    list2 = sorted([(word, list1.count(word)/len(list1)) for word in set1], reverse=True)

    # print("result :", list2, type(list2))
    return list2


if __name__ == "__main__":
    text = "neural network deep learning neural deep network"
    print(wordfrequencies(text))

