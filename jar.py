class Jar:
    def __init__(self, capacity=12):
        self.capacity = capacity
        self.size = 0

    def __str__(self):
        # Return a string representation of the jar
        return "Jar is empty" if self.size == 0 else "🍪" * self.size

    def deposit(self, n):
        # Deposit cookies into the jar
        if n < 0:
            raise ValueError("Cannot deposit a negative number of cookies.")
        if self.size + n > self.capacity:
            raise ValueError("Exceeds jar capacity.")
        self.size += n

    def withdraw(self, n):
        # Withdraw cookies from the jar
        if n < 0:
            raise ValueError("Cannot withdraw a negative number of cookies.")
        if n > self.size:
            raise ValueError("Not enough cookies in the jar to withdraw.")
        self.size -= n

    
    @property # Getter for capacity
    def capacity(self):
        return self._capacity
    
    @capacity.setter # Setter for capacity
    def capacity(self, capacity):
        if capacity < 0:
            raise ValueError("Capacity must be a non-negative integer.")
        self._capacity = capacity

    @property # Getter for size
    def size(self):
        return self._size
    
    @size.setter # Setter for size
    def size(self, size):
        if size < 0:
            raise ValueError("Size must be a non-negative integer.")
        if size > self.capacity:
            raise ValueError("Size cannot exceed jar capacity.")
        self._size = size


def main():
    jar = Jar()
    jar.deposit(5) 
    print(jar)
    jar.withdraw(2)
    print(jar)


if __name__ == "__main__":
    main()