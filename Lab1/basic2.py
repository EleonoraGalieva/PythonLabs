def the_most_common_words(line):
    d = {}
    new_line = str()
    if line:
        line = ' '.join(line)
        words = line.split()
        for word in words:
            if d.get(word):
                d[word] += 1
            else:
                d[word] = 1
    else:
        print("Error")
    list_d = list(d.items())
    list_d.sort(key=lambda i: i[1], reverse=True)
    for word in list_d:
        i = 0
        new_line += word[0]+' '
        i += 1
        if i >= 10:
            break
    print(new_line)
