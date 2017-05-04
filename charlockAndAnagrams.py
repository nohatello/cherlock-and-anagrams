number = int(input())
for numberOfCases in range(number):
    word = str(input())
    strength = len(word)
    count = 0
    for start in range (1, strength):
        cases = {}
        for end in range (strength - start +1):
            subs = list(word[end:end+start])
            subs.sort()
            subs = ".".join(subs)
            if subs in cases:
                cases[subs] +=1
            else:
                cases[subs]=1
            count  = count+ cases[subs]-1
    print(count)