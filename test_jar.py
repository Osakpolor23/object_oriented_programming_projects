from jar import Jar
import pytest

def test_init():
    jar = Jar()
    assert jar.capacity == 12
    assert jar.size == 0

    jar = Jar(10)
    assert jar.capacity == 10
    assert jar.size == 0

    with pytest.raises(ValueError):
        Jar(-1)  # Negative capacity


def test_str():
    jar = Jar()
    assert str(jar) == "Jar is empty"
    jar.deposit(1)
    assert str(jar) == "🍪"
    jar.deposit(11)
    assert str(jar) == "🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪"


def test_deposit():
    jar = Jar()
    jar.deposit(0)
    assert jar.size == 0
    jar.deposit(1)
    assert jar.size == 1
    jar.deposit(11)
    assert jar.size == 12
    with pytest.raises(ValueError):
        jar.deposit(1)  # Exceeds capacity
    with pytest.raises(ValueError):
        jar.deposit(-1)  # Cannot deposit negative cookies


def test_withdraw():
    jar = Jar()
    jar.deposit(5)
    assert jar.size == 5
    jar.withdraw(2)
    assert jar.size == 3
    with pytest.raises(ValueError):
        jar.withdraw(4)  # Not enough cookies
    with pytest.raises(ValueError):
        jar.withdraw(-1)  # Cannot withdraw negative cookies