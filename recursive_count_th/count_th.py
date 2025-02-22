'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
def count_th(word):
    count = 0
    return _count_th(word, count)


def _count_th(word, count):
    if word[-2:] == 'th':
        count += 1
    if len(word) < 3:
        return count
    return _count_th(word[:-1], count)
