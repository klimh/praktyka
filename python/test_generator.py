import string
from main import generate_password

def test_password_length():
    """That test is checking if password has correct number of elements"""
    number = 23
    password = generate_password(number, True)
    assert len(password) == number

def test_special_characters_is_present():
    """That test is checking if password contain special characters"""
    password = generate_password(100, True)
    has_special_character = any(char in string.punctuation for char in password)
    assert has_special_character is True

def test_special_characters_is_absent():
    """That test is checking if password contain special characters"""
    password = generate_password(100, False)
    has_special_character = any(char in string.punctuation for char in password)
    assert has_special_character is False