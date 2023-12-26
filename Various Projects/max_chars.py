def max_character(s):
    counts = {}
    for x in s:
        x = x.lower()
        if x in counts:
            counts[x] += 1
        else:
            counts[x] = 1
    print(counts)
    print(len(counts))
    char = max(counts, key=counts.get)
    return (char, counts[char])




test = "Bu yoğurdu sarımsaklasak da mı saklasak sarımsaklamasak da mı saklasak?"
x,c = max_character(test)
print("maximum character is " + x + " and it appeared " + str(c) + " times.")
