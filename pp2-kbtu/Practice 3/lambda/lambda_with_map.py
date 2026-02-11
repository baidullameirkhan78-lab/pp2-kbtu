# 1) әр санды 2-ге көбейту
numbers = [1, 2, 3, 4]

result = list(map(lambda x: x * 2, numbers))
print(result)


# 2) квадрат
numbers = [1, 2, 3, 4]

result = list(map(lambda x: x * x, numbers))
print(result)


# 3) string ұзындығы
words = ["hi", "hello", "python"]

result = list(map(lambda w: len(w), words))
print(result)


# 4) int-ке айналдыру
nums = ["1", "2", "3"]

result = list(map(lambda x: int(x), nums))
print(result)


# 5) үлкен әріпке ауыстыру
names = ["ali", "madi"]

result = list(map(lambda x: x.upper(), names))
print(result)
