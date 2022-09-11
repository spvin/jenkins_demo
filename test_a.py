import os
import pytest

def test_print_user():
    print("User name is uday")

def test_count():
    for i in range(10):
        print("Number is "+str(i))

if __name__ == "__main__":
    test_print_user()
    test_count()
    print("Test Ended\n")
