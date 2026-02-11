# 1) тек жұп сандар
numbers = [1, 2, 3, 4, 5, 6]

result = list(filter(lambda x: x % 2 == 0, numbers))
print(result)


# 2) тақ сандар
numbers = [1, 2, 3, 4, 5, 6]

result = list(filter(lambda x: x % 2 != 0, numbers))
print(result)


# 3) ұзындығы 3-тен көп сөздер
words = ["hi", "hello", "cat", "python"]

result = list(filter(lambda w: len(w) > 3, words))
print(result)


# 4) 0-ден үлкен сандар
numbers = [-2, -1, 0, 1, 2]

result = list(filter(lambda x: x > 0, numbers))
print(result)


# 5) белгілі әріптен басталатын сөздер
names = ["Ali", "Madi", "Arman"]

result = list(filter(lambda name: name.startswith("A"), names))
print(result)
