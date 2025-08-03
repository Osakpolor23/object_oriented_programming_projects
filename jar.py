class Jar:
    def __init__(self, capacity=12):
        self.capacity = capacity
        self.size = 0

    def __str__(self):
        return "Jar is empty" if self.size == 0 else "🍪" * self.size

    def deposit(self, n):
        if n < 0:
            raise ValueError("Cannot deposit a negative number of cookies.")
        if self.size + n > self.capacity:
            raise ValueError("Exceeds jar capacity.")
        self.size += n

    def withdraw(self, n):
        if n < 0:
            raise ValueError("Cannot withdraw a negative number of cookies.")
        if n > self.size:
            raise ValueError("Not enough cookies in the jar to withdraw.")
        self.size -= n

    @property
    def capacity(self):
        return self._capacity
    
    @capacity.setter
    def capacity(self, capacity):
        if capacity < 0:
            raise ValueError("Capacity must be a non-negative integer.")
        self._capacity = capacity

    @property
    def size(self):
        return self._size
    
    @size.setter
    def size(self, size):
        if size < 0:
            raise ValueError("Size must be a non-negative integer.")
        if size > self.capacity:
            raise ValueError("Size cannot exceed jar capacity.")
        self._size = size


def main():
    jar = Jar()
    jar.deposit(0) 
    print(jar)
    jar.withdraw(0)
    print(jar)


if __name__ == "__main__":
    main()