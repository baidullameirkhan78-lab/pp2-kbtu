# 1. Файлдан барлық жолдарды оқу
with open("example.txt", "r") as f: print(f.readlines())


# 2. Бірінші жолды оқу
with open("example.txt", "r") as f: print(f.readline())


# 3. Файлдың барлығын бір жолға оқу
with open("example.txt", "r") as f: print(f.read())


# 4. Сөздерді санау
with open("example.txt", "r") as f: print(len(f.read().split()))


# 5. Белгілі бір жолды таңдау (мысалы 3-ші жол)
with open("example.txt", "r") as f: lines = f.readlines(); print(lines[2] if len(lines)>2 else "Жол жоқ")
