import re

# raw.txt файлын оқу
with open("raw.txt", "r", encoding="utf-8") as file:
    text = file.read()

# Продукт атауларын тек өнім жолынан табу
products = re.findall(r"^([A-Za-zА-Яа-я]+)\s+\d+", text, re.MULTILINE)

# Бағаларды тек өнім жолынан табу
prices = re.findall(r"^\w+\s+(\d+)", text, re.MULTILINE)
prices = list(map(int, prices))  # сандарды integer-ге айналдыру

# Жалпы сумма
total = sum(prices)

# Дата
date = re.search(r"\d{2}\.\d{2}\.\d{4}", text)

# Төлем түрі
payment = re.search(r"(Card|Cash)", text)

# Нәтижені экранға шығару
print("--- RECEIPT INFO ---")
print("Products:", products)
print("Prices:", prices)
print("Total:", total)
print("Date:", date.group() if date else "Not found")
print("Payment:", payment.group() if payment else "Not found")