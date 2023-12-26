from collections import OrderedDict

def word_occurrences(n, words):
    word_count = OrderedDict()

    for word in words:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1

    distinct_words = list(word_count.keys())
    occurrences = list(word_count.values())

    print(len(distinct_words))
    print(" ".join(map(str, occurrences)))

# Sample Input
n = int(input().strip())
words = [input().strip() for _ in range(n)]

# Sample Output
word_occurrences(n, words)
