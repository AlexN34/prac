#!/usr/bin/python3
import ipdb

# Not finished - TODO handle non alphanumerics
def palindrome(str):
    i = 0
    for char in reversed(str):
        # ipdb.set_trace()
        # print("orig: %d, rev: %d" % str[i], char)
        if char.lower() != str[i].lower():
            return False
        i = i+1
    return True

palindrome("RaceCar")
def removeSpec(str):


# Tests
def test_answer():
    assert palindrome("eye") == True
    assert palindrome("racecar") == True
    assert palindrome("RaceCar") == True
    assert palindrome("RaceCAR") == True
    assert palindrome("2A3*3a2") == True
    assert palindrome("2A3  3a2") == True
    assert palindrome("@_A3*3#A2") == True
    assert palindrome("alex") == False
