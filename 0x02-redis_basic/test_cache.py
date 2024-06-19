#!/usr/bin/env python3
"""
Test script for the Cache class.
"""

Cache = __import__('exercise').Cache

# Create an instance of the Cache class
cache = Cache()

# Define test cases
TEST_CASES = {
    b"foo": None,
    123: int,
    "bar": lambda d: d.decode("utf-8")
}

# Test storing and retrieving values
for value, fn in TEST_CASES.items():
    key = cache.store(value)
    retrieved_value = cache.get(key, fn=fn)
    assert retrieved_value == value, f"Test failed for value: {value}, retrieved: {retrieved_value}"

print("All tests passed.")
