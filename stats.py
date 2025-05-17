
def count_word(contents):
    return len(contents.split())

def count_char(contents):
    words = contents.split()
    d = {}
    for w in words:
        chars = list(w)
        for c in chars:
            key = c.lower()
            if key in d:
                d[key] += 1
            else:
                d[key] = 1


    return d

def sorted_dict(d):
    l = []

    def sort_on(dict):
        return dict["num"]

    for key in d:
        if key.isalpha():
            newdict = {
                "char": key,
                "num": d[key]
            }
            l.append(newdict)

    l.sort(key=sort_on, reverse=True)
    return l
