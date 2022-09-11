import os
import pytest

def test_print_user():
    print("User name is uday")

def count_test():
    for i in range(10):
        print("Number is "+str(i))

if __name__ == "__main__":
    test_print_user()
    count_test()
    print("Test Ended\n")
