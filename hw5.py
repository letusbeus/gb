# Задача-1:
# Напишите скрипт, создающий директории dir_1 - dir_9 в папке,
# из которой запущен данный скрипт.
# И второй скрипт, удаляющий эти папки.
import os
import shutil
def create(dir_name):
    dir_path = os.path.join(os.getcwd(), dir_name)
    try:
        os.mkdir(dir_path)
        print(f"Directory {dir_name} has been created")
    except FileExistsError:
        print(f"Directory {dir_name} already exist")
def remove(dir_name):
    dir_path = os.path.join(os.getcwd(), dir_name)
    try:
        os.rmdir(dir_path)
        print(f"Directory {dir_name} has been removed")
    except FileNotFoundError:
        print(f"Directory {dir_name} doesn't exist")
for i in range(1, 10): create(f"dir_{i}")
for i in range(1, 10): remove(f"dir_{i}")
# Задача-2:
# Напишите скрипт, отображающий папки текущей директории.
def change_dir(new_path):
    os.chdir(new_path)
def show_content():
    infos = os.listdir(path=os.getcwd())
    print("List of oblects in the current directory")
    for info in infos:
        print(info)
change_dir("..")
show_content()
# Задача-3:
# Напишите скрипт, создающий копию файла, из которого запущен данный скрипт.
def copy_script():
    try:
        copy = __file__ + ".copy"
        shutil.copyfile(__file__, copy)
        print(f"Script {__file__} copied successfully")
    except Exception:
        print("An error occurred while copying")
copy_script()
