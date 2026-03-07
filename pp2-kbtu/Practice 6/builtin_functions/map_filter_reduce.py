from functools import reduce
# 1. map: әр санды квадраттау
nums = [1,2,3,4,5]; print(list(map(lambda x: x**2, nums)))


# 2. filter: жұп сандарды таңдау
nums = [1,2,3,4,5,6]; print(list(filter(lambda x: x%2==0, nums)))


# 3. reduce: сандардың қосындысы
nums = [1,2,3,4,5]; print(reduce(lambda x,y: x+y, nums))


# 4. map + filter бірге қолдану: жұп сандарды квадраттау
nums = [1,2,3,4,5,6]; print(list(map(lambda x: x**2, filter(lambda x: x%2==0, nums))))


# 5. reduce: ең үлкен санды табу
nums = [4,7,2,9,5]; print(reduce(lambda x,y: x if x>y else y, nums))
