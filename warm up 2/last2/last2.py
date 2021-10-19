"""
Given a string, return the count of the number of times that a substring length 2 appears in the string
and also as the last 2 chars of the string, so "hixxxhi" yields 1 (we won't count the end substring).

ast2('hixxhi') → 1
last2('xaxxaxaxx') → 1
last2('axxxaaxx') → 2

"""


def last2(word):
    count = 0
    search_string = word[-2:]  # as the last chars in the string
    first_search = 0
    last_search = -1
    if len(word) < 3:
        return 0
    else:
        while True:
            number = word.find(search_string, first_search, last_search)

            if number == -1:
                break
            count += 1
            first_search += number + 1

        return count




