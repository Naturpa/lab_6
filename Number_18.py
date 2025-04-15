class File:
    def __init__(self, name, content=''):
        self.name = name
        self.content = content

class Directory:
    def __init__(self, name):
        self.name = name
        self.subdirs = {}
        self.files = {}

    def get_dir(self, path_parts, create=False):
        curr = self
        for name in path_parts:
            if name not in curr.subdirs:
                if create:
                    curr.subdirs[name] = Directory(name)
                else:
                    return None
            curr = curr.subdirs[name]
        return curr

    def list_contents(self):
        return sorted(list(self.subdirs.keys()) + list(self.files.keys()))

class FileSystem:
    def __init__(self):
        self.root = Directory("")

    def mkdir(self, path):
        parts = [p for p in path.split("/") if p]
        self.root.get_dir(parts, create=True)
        print("Директория создана!")

    def ls(self, path):
        parts = [p for p in path.split("/") if p]
        dir_ = self.root.get_dir(parts)
        if dir_:
            print('\n'.join(dir_.list_contents()))
        else:
            print("Директория не найдена.")

    def write(self, path, content):
        parts = [p for p in path.split("/") if p]
        dir_path, file_name = parts[:-1], parts[-1]
        dir_ = self.root.get_dir(dir_path, create=True)
        dir_.files[file_name] = File(file_name, content)
        print("Файл записан.")

    def read(self, path):
        parts = [p for p in path.split("/") if p]
        dir_path, file_name = parts[:-1], parts[-1]
        dir_ = self.root.get_dir(dir_path)
        if dir_ and file_name in dir_.files:
            print(dir_.files[file_name].content)
        else:
            print("Файл не найден.")

fs = FileSystem()

help_text = """
Доступные команды:
mkdir [путь]  — создать директорию
ls [путь]     — вывести содержимое директории
write [путь к файлу] [строка] — записать строку в файл
read  [путь к файлу] — прочитать содержимое файла
exit           — выход
"""

print(help_text)
while True:
    command = input("> ").strip()
    if command == "exit":
        break
    if command.startswith("mkdir "):
        _, path = command.split(maxsplit=1)
        fs.mkdir(path)
    elif command.startswith("ls "):
        _, path = command.split(maxsplit=1)
        fs.ls(path)
    elif command.startswith("write "):
        parts = command.split(maxsplit=2)
        if len(parts) < 3:
            print("Неверный формат команды.")
            continue
        _, path, content = parts
        fs.write(path, content)
    elif command.startswith("read "):
        _, path = command.split(maxsplit=1)
        fs.read(path)
    else:
        print("Неизвестная команда.")