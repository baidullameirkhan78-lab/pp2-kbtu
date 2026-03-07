# 1. enumerate: тізімдегі индекстер мен элементтерді шығару
fruits = ["алма","банан","киви"]; print(list(enumerate(fruits)))


# 2. enumerate бастамасын 1-ден беру
print(list(enumerate(fruits, start=1)))


# 3. zip: екі тізімді жұптау
names = ["Мейірхан","Аян","Дана"]; ages = [17,18,16]; print(list(zip(names,ages)))


# 4. zip + loop: ат пен жас шығару
for name, age in zip(names, ages): print(f"{name} жасында {age} жаста")


# 5. enumerate + zip: индекс, ат және жас шығару
for i, (name, age) in enumerate(zip(names, ages), start=1): print(f"{i}. {name} - {age} жас")