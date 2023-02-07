from collections import defaultdict


def count_lengths(text):
    """ Takes a string and returns a defaultdict with the frequency counts."""
    length_freq = defaultdict(int)
    for word in text.split():
        length_freq[len(word)] += 1
    return length_freq


def top5_word_lengths(text):
    """takes a string text and returns a list of the top five most frequent
    word lengths in text."""
    length_freq = count_lengths(text)

    # Store the word lengths and their frequency counts in the list
    # length_freq_list.
    length_freq_list = []
    for length, freq in length_freq.items():
        length_freq_list.append((freq, length))

    # Sort the frequency lengths and store them in top5.
    top5 = []
    for freq, length in sorted(length_freq_list, reverse=True)[:5]:
        top5.append(length)
    return top5

print(count_lengths("one one was a racehorse two two was one too"))
print(top5_word_lengths("one one was a racehorse two two was one too"))
print(top5_word_lengths("buffalo buffalo buffalo chicken buffalo"))
print(top5_word_lengths("the quick brown fox jumped over a lazy dog"))



# ----------
from collections import defaultdict

def count_lengths(text):
    """ Takes a string and returns a defaultdict with the frequency counts."""
    my_dd = defaultdict(int)
    for char in text.split():
        my_dd[len(char)] += 1
    print(my_dd)
    return my_dd

def top5_word_lengths(text):
    """takes a string text and returns a list of the top five most frequent
    word lengths in text."""

    # Store the word lengths and their frequency counts in the list
    word_dict = count_lengths(text)
    print('p1', word_dict)

    # Sort the frequency lengths and store them in top5.

print(count_lengths("one one was a racehorse two two was one too"))
print(top5_word_lengths("one one was a racehorse two two was one too"))
print(top5_word_lengths("buffalo buffalo buffalo chicken buffalo"))
print(top5_word_lengths("the quick brown fox jumped over a lazy dog"))








