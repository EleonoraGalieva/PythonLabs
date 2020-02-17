def word_count(line):
    d = {}
    if line:
        line = ' '.join(line)
        words = line.split()
        for word in words:
            if d.get(word):
                d[word] += 1
            else:
                d[word] = 1
        print(d)
    else:
        print("Error")
