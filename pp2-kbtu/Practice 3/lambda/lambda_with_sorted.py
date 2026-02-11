# 1) санды өсу ретімен
numbers = [5, 2, 8, 1]

result = sorted(numbers, key=lambda x: x)
print(result)


# 2) кему ретімен
numbers = [5, 2, 8, 1]

result = sorted(numbers, key=lambda x: -x)
print(result)


# 3) сөз ұзындығы бойынша
words = ["hi", "hello", "python", "cat"]

result = sorted(words, key=lambda w: len(w))
print(result)


# 4) tuple ішіндегі екінші элемент бойынша
pairs = [(1, 3), (2, 1), (4, 2)]

result = sorted(pairs, key=lambda x: x[1])
print(result)


# 5) аты бойынша адамдарды сорттау
people = [
    {"name": "Ali", "age": 20},
    {"name": "Madi", "age": 18},
]

result = sorted(people, key=lambda p: p["age"])
print(result)
