import shutil, os
# 1. Файлды көшіру
shutil.copy("example.txt","copy_example.txt")


# 2. Файлды көшіріп атын өзгерту
shutil.copy("example.txt","example_backup.txt")


# 3. Файлды өшіру
os.remove("copy_example.txt")


# 4. Файл бар-жоғын тексеру және өшіру
if os.path.exists("example_backup.txt"): os.remove("example_backup.txt")


# 5. Каталогтағы барлық файлдарды көшіру (мысалы, folder1 -> folder2)
if os.path.exists("folder2")==False: os.mkdir("folder2"); [shutil.copy(f"folder1/{f}", "folder2/") for f in os.listdir("folder1") if os.path.isfile(f"folder1/{f}")]