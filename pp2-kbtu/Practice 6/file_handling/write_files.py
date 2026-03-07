# 1. Жаңа файлға жазу
with open("output.txt", "w") as f: f.write("Сәлем, әлем!\n")


# 2. Файлға бірнеше жол жазу
with open("output.txt", "w") as f: f.writelines(["Бірінші\n","Екінші\n","Үшінші\n"])


# 3. Файлға қосу режимінде жазу
with open("output.txt", "a") as f: f.write("Қосымша жол\n")


# 4. Сандық деректерді файлға жазу
numbers = [1,2,3,4,5]; with open("numbers.txt","w") as f: f.write(",".join(map(str,numbers)))


# 5. Форматталған мәтінді жазу
name = "Мейірхан"; age = 17; with open("info.txt","w") as f: f.write(f"Менің атым {name}, жасым {age}\n")
