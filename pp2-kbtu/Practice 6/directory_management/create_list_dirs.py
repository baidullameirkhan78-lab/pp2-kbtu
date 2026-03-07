import os
# 1. Жаңа каталог жасау
os.mkdir("new_folder") if not os.path.exists("new_folder") else None


# 2. Көп каталог жасау
for d in ["folder1","folder2","folder3"]: os.mkdir(d) if not os.path.exists(d) else None


# 3. Каталог ішінде файл жасау
with open("new_folder/file.txt","w") as f: f.write("Мәтін")


# 4. Каталогтағы барлық файлдар мен ішкі каталогтарды көрсету
print(os.listdir("new_folder"))


# 5. Барлық файлдар мен каталогтарды толық жолымен көрсету
print([os.path.join("new_folder", f) for f in os.listdir("new_folder")])
