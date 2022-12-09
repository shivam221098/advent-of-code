class Stack:
    def __init__(self):
        self.__stack = []

    def push(self, element):
        self.__stack.append(element)

    @property
    def pop(self):
        return self.__stack.pop()

    @property
    def top(self):
        if len(self.__stack) > 0:
            return self.__stack[-1]
        return None

    @property
    def height(self):
        return len(self.__stack)

    def __str__(self):
        return "[" + ", ".join(self.__stack) + "]"

    def __len__(self):
        return len(self.__stack)
