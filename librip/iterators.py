class Unique:
    def __init__(self, lst, ignore_case = False):
        self.lst = list(lst)
        self.index = -1
        self.ignore = ignore_case

    def __next__(self):
        if self.index == len(self.lst)-1:
            raise StopIteration
        arr = set(self.lst)
        self.lst = list(arr)
        if self.ignore:
            self.lst = ''.join(self.lst)
            self.lst = (self.lst).lower()
        self.index += 1
        if self.index < len(self.lst):
            return self.lst[self.index]

    def __iter__(self):
        return self



