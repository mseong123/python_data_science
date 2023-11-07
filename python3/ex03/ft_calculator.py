class calculator:
    def __init__(self, arr):
        self.arr = arr

    def __add__(self, object) -> None:
        self.arr = [i + object for i in self.arr]
        print(self.arr)

    def __mul__(self, object) -> None:
        self.arr = [i * object for i in self.arr]
        print(self.arr)

    def __sub__(self, object) -> None:
        self.arr = [i - object for i in self.arr]
        print(self.arr)

    def __truediv__(self, object) -> None:
        try:
            assert object != 0, "Cannot divide by zero"
        except Exception as e:
            print(f"Exception:{e}")
        else:
            self.arr = [i / object for i in self.arr]
            print(self.arr)
