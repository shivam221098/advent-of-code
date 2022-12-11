class Dir:
    def __init__(self, name: str):
        self.__name = name
        self.__files = []
        self.__size = 0

    @property
    def calculate_size(self):
        size = 0
        for file in self.__files:
            size += file.size

        return size

    def __iter__(self):
        return self.__files.__iter__()

    def __str__(self):
        return f"- {self.name} (dir)"

    @property
    def name(self):
        return self.__name

    def create_blob(self, blob):
        self.__files.append(blob)


class File:
    def __init__(self, name: str, size: int):
        self.__name = name
        self.__size = size

    @property
    def size(self):
        return self.__size

    @property
    def name(self):
        return self.__name

    def __str__(self):
        return f"- {self.name} (file, size={self.size})"


class Linux:
    def __init__(self):
        self.__base = Dir("/")
        self.__current_directory = self.__base
        self.__home = self.__base
        self.__dir_stack = [self.__base]

    def cd(self, arg: str):
        if arg == "/":
            self.__home = self.__base

        elif arg == "..":
            self.__dir_stack.pop()
            self.__current_directory = self.__dir_stack[-1]

        else:
            if len(arg) == 0:
                raise FileNotFoundError()

            required_dir = self.find_dir(arg)
            self.__current_directory = required_dir
            self.__dir_stack.append(required_dir)

    def find_dir(self, dir_name: str):
        """
        returns directory instance if found else returns raise Error
        :return: Dir
        """
        for blob in self.__current_directory:
            if blob.name == dir_name:
                return blob

        raise FileNotFoundError("%s not found" % dir_name)

    @property
    def current_path(self):
        return "/".join(map(lambda x: x.name, self.__dir_stack))

    @property
    def current_dir(self):
        return self.__current_directory.name

    @property
    def home(self):
        return self.__base

    def create_blob(self, blob):
        self.__current_directory.create_blob(blob)

    def pretty_print(self, current_dir: Dir, level: str = ""):
        tree = str(current_dir) + "\n"
        for blob in current_dir:
            if isinstance(blob, Dir):
                child = level + self.pretty_print(blob, level + "  ")
                tree += child
            else:
                tree += level + str(blob) + "\n"
        return tree
