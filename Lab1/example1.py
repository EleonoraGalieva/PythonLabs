def word_count(line):
    d = {}
    if line:
        for word in line:
            if d.get(word):
                d[word] += 1
            else:
                d[word] = 1
        print(d)
    else:
        print("Error")
