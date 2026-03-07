import shutil
# 1. Файлды бір каталогтан екінші каталогқа көшіру
shutil.move("new_folder/file.txt","folder1/file.txt")


# 2. Файл атын өзгертіп көшіру
shutil.move("folder1/file.txt","folder1/file_renamed.txt")


# 3. Бірнеше файлды көшіру
for f in ["file1.txt","file2.txt"]: open(f,"w").close(); shutil.move(f,"folder2/"+f)


# 4. Барлық файлдарды бір каталогтан екінші каталогқа көшіру
for f in os.listdir("folder1"): if os.path.isfile("folder1/"+f): shutil.move("folder1/"+f,"folder2/"+f)


# 5. Файлды бастапқы каталогта тексеру және қажет болса көшіру
src = "folder2/file1.txt"; dst = "folder1/file1.txt"; shutil.move(src,dst) if os.path.exists(src) else print("Файл жоқ")